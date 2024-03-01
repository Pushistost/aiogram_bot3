from aiogram import Router, types, F

magic_router = Router()


@magic_router.message(F.photo[-1].as_("photo"))
async def accept_photo(message: types.Message, photo: types.PhotoSize):
    await message.answer(f"Photo: {photo}")
