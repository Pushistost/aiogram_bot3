from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, Update

from typing import Union


class MyMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler,
                       event: Update,
                       data: dict
                       ):

        if isinstance(event, Message):
            data["some_variable"] = "some_value"
        elif isinstance(event, CallbackQuery):
            data["some_other_variable"] = "some_other_value"

        result = await handler(event, data)

        return result
