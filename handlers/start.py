from aiogram import types, Router
from aiogram.filters import Command
list_of_indexes = []

start_router = Router()

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    id = message.from_user.id
    if id not in list_of_indexes:
        list_of_indexes.append(id)
    users = len(list_of_indexes)
    name = message.from_user.first_name
    await message.answer(f'Привет ,{name}, наш бот обслуживает уже {users} пользователя')