from aiogram import BaseMiddleware
from aiogram.types import Update

from tg_bot.config import Config


class MyMiddleware(BaseMiddleware):
    def __init__(self, config: Config):
        self.config = config
        super().__init__()

    async def __call__(self, handler, event: Update, data: dict):
        data["config"] = self.config
        print("Heu bitches")
        return await handler(event, data)


