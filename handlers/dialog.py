from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext
from bot_config import database


opros_router = Router()

class Opros(StatesGroup):
    name = State()
    age = State()
    genre = State()

@opros_router.message(Command('stop'))
@opros_router.message(F.text == 'stop')
async def stop_dialog(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Опрос остановлен")


@opros_router.message(Command('opros'), default_state)
async def start_opros_name(message: types.Message, state: FSMContext):
    await message.answer('Для остановки напишите слово: "stop"')
    await message.answer('Как ваше имя?')
    await state.set_state(Opros.name)

@opros_router.message(Opros.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Ваш возраст?')
    await state.set_state(Opros.age)

@opros_router.message(Opros.age)
async def get_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Ваш любимый жанр?')
    await state.set_state(Opros.genre)

@opros_router.message(Opros.genre)
async def get_genre(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)
    data = await state.get_data()
    await message.answer('Спасибо за пройденный опрос!')
    database.save_poll(data)
    await state.clear()

