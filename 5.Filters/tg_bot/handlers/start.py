from aiogram import Router, types, Bot
from aiogram.filters import CommandStart, CommandObject
from aiogram.utils.deep_linking import create_start_link, create_startgroup_link

start_router = Router()


@start_router.message(CommandStart(deep_link=True))
async def cmd_start_dl(message: types.Message, bot: Bot, command: CommandObject):
    await bot.send_message(message.chat.id, text=f"Hello, your args: {command.args}")


@start_router.message(CommandStart())
async def cmd_start(message: types.Message, bot: Bot):
    # deep link https://t.me/your_bot?start=our_arguments
    # deep link https://t.me/your_bot?startgroup=our_arguments
    link = await create_start_link(bot, payload=f"ref-{message.from_user.id}")
    group_link = await create_startgroup_link(bot, payload=f"ref-{message.from_user.id}")
    await bot.send_message(message.chat.id, text=f"Hello you can use this link {link}/n"
                                                 f"Or this: {group_link}")
