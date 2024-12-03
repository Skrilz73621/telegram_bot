import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values
import random

token = dotenv_values('.env')['BOT_TOKEN']
bot = Bot(token=token)
dispatcher = Dispatcher()
list_of_indexes = []


@dispatcher.message(Command('start'))
async def start_handler(message: types.Message):
    id = message.from_user.id
    if id not in list_of_indexes:
        list_of_indexes.append(id)
    users = len(list_of_indexes)
    name = message.from_user.first_name
    await message.answer(f'Привет ,{name}, наш бот обслуживает уже {users} пользователя')


@dispatcher.message(Command('myinfo'))
async def myinfo_handler(message: types.Message):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(f'Ваш id: {id}\nВаше имя: {name}\nВаш никнейм: {username}')


@dispatcher.message(Command('random'))
async def random_handler(message: types.Message):
    list_of_names = ["Алексей", "Дарья", "Максим", "Екатерина", "Иван", "Мария", "Сергей", "Ольга", "Андрей", "Анна"]
    random_name = random.choice(list_of_names)
    await message.answer(f'Случайное имя из списка: {random_name}')

@dispatcher.message()
async def echo_handler(message: types.Message):
    name = message.from_user.first_name
    txt = message.text
    await message.answer(f'Привет, {name} \n {txt}!')



async def main():
    # запустил бота
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())