from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

list_of_indexes = []

start_router = Router()

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Оставить отзыв', callback_data='review')
            ]
        ]
    )
    id = message.from_user.id
    if id not in list_of_indexes:
        list_of_indexes.append(id)
    users = len(list_of_indexes)
    name = message.from_user.first_name
    await message.answer(f'Привет ,{name}, наш бот обслуживает уже {users} пользователя', reply_markup=kb)


async def review_start(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer('Как вас зовут?')
    await state.set_state('RestourantReview:name')
    await callback_query.answer()