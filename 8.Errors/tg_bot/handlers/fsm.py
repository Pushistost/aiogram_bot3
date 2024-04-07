from aiogram.filters import Command, StateFilter

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from tg_bot.handlers.states import ChooseBudgetOption, SetIncomeExpenses, EnterBudget

budget_router = Router()


@budget_router.message(Command("budget"), StateFilter("*"))
async def cmd_budget(message: types.Message, state: FSMContext):
    """
    Обработчик команды /budget. Показывает приветственное сообщение и предлагает
    пользователю выбрать одну из опций для управления своим бюджетом.
    """
    await message.answer("""Welcome to the Personal Finance Tracker Bot.
    Choose an option:
    1. Add Income and Expenses
    2. Set Budget
    3. View Summary
    """)

    await state.set_state(ChooseBudgetOption)


@budget_router.message(ChooseBudgetOption,
                       F.text.startswith("1"))
async def choose_add_income_expenses(message: types.Message, state: FSMContext):
    """
    Переводит пользователя в режим добавления доходов и расходов.
    """
    await message.answer("Enter the amount of income")
    await state.set_state(SetIncomeExpenses.AddIncome)


@budget_router.message(
    SetIncomeExpenses.AddIncome,
    # F.text.isdigit(),
    F.text.as_("income"),
    )
async def enter_income(message: types.Message, state: FSMContext, income: int):
    """
    Принимает от пользователя сумму дохода и переводит его к вводу расходов.
    """
    await state.update_data(income=int(income))
    await message.answer("Enter the amount of expenses")
    await state.set_state(SetIncomeExpenses.AddExpenses)


@budget_router.message(
    SetIncomeExpenses.AddExpenses,
    # F.text.isdigit(),
    F.text.as_("expenses"),
)
async def enter_expenses(message: types.Message, state: FSMContext, expenses: int):
    """
    Принимает от пользователя сумму расходов и завершает ввод данных.
    """
    await state.update_data(expenses=int(expenses))
    await message.answer("Thank you for entering the data")
    await cmd_budget(message, state)


@budget_router.message(ChooseBudgetOption,
                       F.text.startswith("2"))
async def choose_set_budget(message: types.Message, state: FSMContext):
    """
    Переводит пользователя в режим установки общего бюджета.
    """
    await message.answer("Enter the amount of budget")
    await state.set_state(EnterBudget)


@budget_router.message(
    EnterBudget,
    # F.text.isdigit(),
    F.text.as_("budget"),
    )
async def enter_budget(message: types.Message, state: FSMContext, budget: int):
    """
    Принимает от пользователя сумму общего бюджета и завершает ввод данных.
    """
    await state.update_data(budget=int(budget))
    await message.answer("Thank you for entering the budget")
    await cmd_budget(message, state)


@budget_router.message(StateFilter(SetIncomeExpenses, EnterBudget))
async def enter_income_expenses_invalid(message: types.Message):
    """
    Обрабатывает невалидный ввод (не числовой) данных о доходах и расходах.
    """
    await message.reply("Invalid input, enter a number.")


@budget_router.message(ChooseBudgetOption,
                       F.text.startswith("3"))
async def choose_view_summary(message: types.Message, state: FSMContext):
    """
    Показывает пользователю сводку по его доходам, расходам и общему бюджету.
    """
    data = await state.get_data()
    income = data.get("income")
    expenses = data.get("expenses")
    budget = data.get("budget")
    if not data:
        await message.answer("No data entered yet")
        await cmd_budget(message, state)
        return

    if not income:
        await message.answer("No income entered yet. Please, enter the amount of income.")
        await choose_add_income_expenses(message, state)
        return

    if not expenses:
        await message.answer("No expenses data entered yet. Please, enter the amount of expenses.")
        await state.set_state(SetIncomeExpenses.AddExpenses)
        return

    if not budget:
        await message.answer("No budget entered yet.")
        await choose_set_budget(message, state)
        return

    balance = income - expenses
    summary = f"""
💰 Income: {income}
💸 Expenses: {expenses}
📊 Budget: {budget}
💼 Balance: {balance}
"""

    if balance < 0:
        summary += f"🚨 You are in debt by {abs(balance)}\n"
    if expenses > budget:
        summary += f"🚨 You are over budget by {expenses - budget}\n"

    summary += "If you want to clear the data, enter /clear\n"
    summary += "If you want to exit, enter /exit\n"

    await message.answer(summary)


# Обработчик для не реализованных функций
@budget_router.message(EnterBudget)
async def not_implemented(message, state: FSMContext):
    await message.answer("Not implemented")
    await state.clear()
