import asyncio
import logging

import betterlogging as bl
from aiogram import Bot, Dispatcher

from tg_bot.config import load_config
from tg_bot.handlers.start import start_router


async def main():
    bl.basic_colorized_config(level=logging.INFO)
    config = load_config()
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(start_router)

    await dp.start_polling(bot)
    await bot.session.close()


try:
    asyncio.run(main())
except KeyboardInterrupt:
    logging.info("Bot stopped!")
