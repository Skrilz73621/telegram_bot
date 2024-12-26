from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext
from bot_config import database
from pprint import pprint

admin_router = Router()
admin_router.message.filter(F.from_user.id == 1002180589)

class Dish(StatesGroup):
    name = State()
    price = State()
    description = State()
    picture = State()
    category = State()
    

@admin_router.message(Command('dish'), default_state)
async def start_adding_dish(message: types.Message, state: FSMContext):
    await message.answer('Введите имя нового блюда')
    await state.set_state(Dish.name)
    
@admin_router.message(Dish.name)
async def start_adding_price(message: types.Message, state:FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer('Введите цену нового блюда')
    await state.set_state(Dish.price)
    
    
@admin_router.message(Dish.price)
async def start_adding_picture(message: types.Message, state:FSMContext):
    price = message.text
    await state.update_data(price=price)
    await message.answer('Загрузите картинку блюда')
    await state.set_state(Dish.picture)
    
    
@admin_router.message(Dish.picture, F.photo)
async def start_adding_description(message:types.Message, state:FSMContext):
    picture = message.photo
    biggest_picture = picture[-1] 
    biggest_image_id  =biggest_picture.file_id
    await state.update_data(picture=biggest_image_id)
    await message.answer('Введите описание нового блюда')
    await state.set_state(Dish.description)
    
    
@admin_router.message(Dish.description)
async def start_adding_category(message:types.Message, state:FSMContext):
    description = message.text
    await state.update_data(description = description)
    
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Супы', callback_data = 'soup'),types.InlineKeyboardButton(text='Второе блюдо', callback_data = 'second_dish')],
            [types.InlineKeyboardButton(text='Холодные напитки', callback_data = 'cold_drinks'), types.InlineKeyboardButton(text='Горячие напитки', callback_data = 'hot_drinks')],
            [types.InlineKeyboardButton(text='Десерты', callback_data='deserts'), types.InlineKeyboardButton(text='Алкоголь', callback_data='alcohol')]
        ]
    )
    await message.answer('Выберите категорию блюда', reply_markup=kb)
    await state.set_state(Dish.category)

@admin_router.callback_query(StateFilter(Dish.category))
async def category_selected(callback_query:types.CallbackQuery, state:FSMContext):
    category = callback_query.data
    await state.update_data(category=category)
    data = await state.get_data()
    database.save_dish(data)
    await state.clear()
    await callback_query.message.edit_text(
        f"Блюдо добавлено:\nИмя: {data['name']}\nЦена: {data['price']}\nОписание: {data['description']}\nКатегория: {category}" 
    )
    await callback_query.answer()
    