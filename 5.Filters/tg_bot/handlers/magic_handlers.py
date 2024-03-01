from aiogram import Router, types, F

magic_router = Router()


@magic_router.message(F.photo[-1].as_("photo"))
async def accept_photo(message: types.Message, photo: types.PhotoSize):
    await message.answer(f"Photo: {photo}")


@magic_router.message(F.from_user.id.in_([258829722, 32332323, 62789002, 312313412, 24241244]))
async def accept_from_user(message: types.Message):
    await message.answer(f"Hello my creator!")