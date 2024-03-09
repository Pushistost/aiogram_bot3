import re

from aiogram import Router, types, F
from aiogram.types import CallbackQuery

magic_router = Router()


@magic_router.message(F.photo[-1].as_("photo"))
async def accept_photo(message: types.Message, photo: types.PhotoSize):
    await message.answer(f"Photo: {photo}")


@magic_router.message(F.from_user.id.in_([32332323, 62789002, 312313412, 24241244]))
async def accept_from_user(message: types.Message):
    await message.answer(f"Hello my creator!")


@magic_router.message(F.chat.type.in_(["group", "supergroup"]))
async def accept_group(message: types.Message):
    await message.answer("Hello group")


@magic_router.callback_query(F.data == "test")
async def test_callback(callback_query: CallbackQuery):
    await callback_query.answer("test callback_query")


@magic_router.message(F.text.regexp(re.compile(r"^ref-(\d+)$")).group(1).cast(int).as_("ref_id"))
# @magic_router.message(F.text.regexp(re.compile(r"^ref-(\d+)$")).as_("ref_match"))
async def accept_reg(message: types.Message, ref_match: re.Match):
    ref_id = ref_match.group(1)
    await message.answer(f"Hello, ref-{ref_id} {type(ref_id)}!")
