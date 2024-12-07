from aiogram import types, Router
from aiogram.filters import Command

picture_router = Router()

@picture_router.message(Command('picture'))
async def picture_handler(message: types.Message):
    photo = types.FSInputFile('images/Bavarskaya.jpeg')
    await message.answer_photo(photo=photo, caption='huynya')