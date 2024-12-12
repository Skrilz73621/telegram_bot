from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

opros_router = Router()

class Opros(StatesGroup):
    user_name = State()
    user_age = State()
    user_genre = State()


@opros_router.message(Command('opros'))
async def start_opros(message:types.Message, state:FSMContext):
    await message.answer('Как ваше имя?')
    await state.set_state(Opros.user_name)

@opros_router.message(Opros.user_name)
async def start_opros(message:types.Message, state:FSMContext):
    await message.answer('Ваш возраст?')
    await state.set_state(Opros.user_age)

@opros_router.message(Opros.user_age)
async def start_opros(message:types.Message, state:FSMContext):
    await message.answer('Ваш любимый жанр?')
    await state.set_state(Opros.user_genre)

@opros_router.message(Opros.user_genre)
async def start_opros(message:types.Message, state:FSMContext):
    await message.answer('Спасибо за пройденный опрос')
    await state.clear()