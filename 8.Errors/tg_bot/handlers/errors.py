import logging

from aiogram import Router, F, Bot
from aiogram.types import ErrorEvent, Message

from tg_bot.config import Config

error_router = Router()


@error_router.error(F.update.message.as_("message"))
async def handler_error(error_event: ErrorEvent, message: Message, bot: Bot, config: Config):
    logging.error(error_event.exception, exc_info=True)
    await bot.send_message(
        config.tg_bot.error_chat_id,
        f"Error: {error_event.exception.__class__.__name__}: {error_event.exception.__traceback__}"
    )
