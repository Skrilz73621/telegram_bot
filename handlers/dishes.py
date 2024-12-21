from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from bot_config import database


show_dishes_router = Router()

@show_dishes_router.message(Command('showAllDishes'))
async def show_all_dishes(message: types.Message):
    dishes = database.show_all_dishes()
    for dish in dishes:
        await message.answer(f'Dish name: {dish["name"]}\nDish price: {dish["price"]}\nDish description: {dish["description"]}\nDish category: {dish["category"]}')