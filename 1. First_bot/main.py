import asyncio

from aiogram import Bot, Dispatcher, types, F


async def echo(message: types.Message, bot: Bot):
    await bot.send_message(
        chat_id=message.chat.id,
        text=message.text
    )


async def main():
    bot = Bot("6390086062:AAFTUAyeCYwCbObH154bRRpsUYcGyNY1pI8")
    dp = Dispatcher()
    dp.message.register(echo, F.text)

    await dp.start_polling(bot)

    await bot.session.close()

asyncio.run(main())


