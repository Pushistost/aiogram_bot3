import asyncio
import logging


import betterlogging as bl
from aiogram import Bot, Dispatcher

from handlers.start import start_router


async def main():
    bl.basic_colorized_config(level=logging.INFO)
    bot = Bot("6390086062:AAFTUAyeCYwCbObH154bRRpsUYcGyNY1pI8")
    dp = Dispatcher()

    dp.include_router(start_router)

    await dp.start_polling(bot)
    await bot.session.close()


try:
    asyncio.run(main())
except KeyboardInterrupt:
    logging.info("Bot stopped!")
