from aiogram import Router, types, F, Bot

start_router = Router()


@start_router.message(F.text)
async def start_handler(message: types.Message, bot: Bot):
    response_text = f"Сам ты {message.text}"
    await bot.send_message(
        chat_id=message.chat.id,
        text=response_text
    )
