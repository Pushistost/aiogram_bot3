from aiogram import Router, types, Bot, F
from aiogram.enums import ChatType
from aiogram.filters import CommandStart, CommandObject
from aiogram.utils.deep_linking import create_start_link, create_startgroup_link

start_router = Router()


@start_router.message(
    CommandStart(deep_link=True,
                 deep_link_encoded=True,
                 magic=F.args.regexp(r"^ref-(\d+)$").group(1).cast(int).as_("ref_id")
                 ),
    F.chat.type == ChatType.PRIVATE)
async def cmd_start_dl(message: types.Message, bot: Bot, ref_id: int):
    await bot.send_message(message.chat.id, text=f"Hello, your args: {ref_id}, type: {type(ref_id)}")


@start_router.message(CommandStart())
async def cmd_start(message: types.Message, bot: Bot):
    # deep link https://t.me/your_bot?start=our_arguments
    # deep link https://t.me/your_bot?startgroup=our_arguments
    link = await create_start_link(bot, payload=f"ref-{message.from_user.id}", encode=True)
    group_link = await create_startgroup_link(bot, payload=f"ref-{message.from_user.id}", encode=True)
    await bot.send_message(message.chat.id, text=f"Hello you can use this link {link} \n"
                                                 f"Or this for invite: {group_link}")
