from aiogram.filters import Command, StateFilter

from aiogram import Router, types, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from tg_bot.handlers.states import ChooseBudgetOption, SetIncomeExpenses, EnterBudget

budget_router = Router()


@budget_router.message(Command("budget"), StateFilter())
async def cmd_budget(message: types.Message, state: FSMContext):
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
    await message.answer("Enter the amount of income")
    await state.set_state(SetIncomeExpenses.AddIncome)


@budget_router.message(ChooseBudgetOption,
                       F.text.startswith("2"))
async def choose_set_budget(message: types.Message, state: FSMContext):
    await message.answer("Enter the amount of budget")
    await state.set_state(EnterBudget)


@budget_router.message(ChooseBudgetOption,
                       F.text.startswith("3"))
async def choose_view_summary(message: types.Message, state: FSMContext):
    pass