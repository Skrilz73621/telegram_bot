from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from bot_config import database


class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()
    date = State()

rate_router = Router()


@rate_router.callback_query(F.data == 'review', default_state)
async def review_start(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer('Как вас зовут?')
    await state.set_state(RestourantReview.name)
    await callback_query.answer()


@rate_router.message(RestourantReview.name)
async def handle_name(message: types.Message, state: FSMContext):
    name = message.text
    if not isinstance(name, str) or len(name) > 20:
        await message.answer('Пожалуйста, введите корректное имя (не более 20 символов).')
        return
    await state.update_data(name = name)
    await message.answer('Напишите ваш номер телефона. Например: +996123456789')
    await state.set_state(RestourantReview.phone_number)

@rate_router.message(RestourantReview.phone_number)
async def handle_phone_number(message: types.Message, state: FSMContext):
    phone_number = message.text
    if not phone_number.startswith('+996') or len(phone_number) != 13:
        await message.answer('Введите корректный номер телефона в формате +996123456789.')
        return
    await state.update_data(phone_number=phone_number)

    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='1', callback_data='1')],
            [types.InlineKeyboardButton(text='2', callback_data='2')],
            [types.InlineKeyboardButton(text='3', callback_data='3')],
            [types.InlineKeyboardButton(text='4', callback_data='4')],
            [types.InlineKeyboardButton(text='5', callback_data='5')],
        ]
    )
    await message.answer('Оцените качество еды от 1 до 5.', reply_markup=kb)
    await state.set_state(RestourantReview.food_rating)


@rate_router.callback_query(StateFilter(RestourantReview.food_rating))
async def handle_food_rating(callback_query: types.CallbackQuery, state: FSMContext):
    food_rating = callback_query.data
    await state.update_data(food_rating=food_rating)

    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='1', callback_data='1')],
            [types.InlineKeyboardButton(text='2', callback_data='2')],
            [types.InlineKeyboardButton(text='3', callback_data='3')],
            [types.InlineKeyboardButton(text='4', callback_data='4')],
            [types.InlineKeyboardButton(text='5', callback_data='5')],
        ]
    )
    await callback_query.message.answer(f'Спасибо за вашу оценку еды: {food_rating}. Оцените чистоту.', reply_markup=kb)
    await state.set_state(RestourantReview.cleanliness_rating)


@rate_router.callback_query(StateFilter(RestourantReview.cleanliness_rating))
async def handle_cleanliness_rating(callback_query: types.CallbackQuery, state: FSMContext):
    cleanliness_rating = callback_query.data
    await state.update_data(cleanliness_rating=cleanliness_rating)

    await callback_query.message.answer(f'Спасибо за вашу оценку чистоты: {cleanliness_rating}.')
    await callback_query.answer()

    await callback_query.message.answer('Пожалуйста, напишите дополнительные комментарии, если есть.')
    await state.set_state(RestourantReview.extra_comments)


@rate_router.message(RestourantReview.extra_comments)
async def handle_extra_comments(message: types.Message, state: FSMContext):
    extra_comments = message.text
    await state.update_data(extra_comments=extra_comments)
    await message.answer('Введите пожалуйста дату сегодняшнего дня')
    await state.set_state(RestourantReview.date)
    
    
@rate_router.message(RestourantReview.date)
async def handle_date(message:types.Message, state:FSMContext):
    date = message.text.strip()    
    await state.update_data(date=date)
    data = await state.get_data()
    database.save_poll(data)
    await message.answer('Спасибо за ваш отзыв! Мы обязательно его учтем.')
    await message.answer(f'{data["name"]}\n{data["phone_number"]}\n{data["food_rating"]}\n{data["cleanliness_rating"]}\n{data["extra_comments"]}\n{data["date"]}')
    await state.clear()


