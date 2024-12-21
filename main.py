import asyncio
from aiogram import Router, F, types

from handlers.picture import picture_router
from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.random import random_router
from handlers.dialog import opros_router
from handlers.admin import admin_router
from handlers.review_dialog import rate_router
from handlers.dishes import show_dishes_router
from bot_config import dispatcher, bot, database


async def on_startup(bot):
    database.create_tables()

async def main():
    dispatcher.include_router(start_router)
    dispatcher.include_router(picture_router)
    dispatcher.include_router(myinfo_router)
    dispatcher.include_router(random_router)
    dispatcher.include_router(opros_router)
    dispatcher.include_router(rate_router)
    dispatcher.include_router(admin_router)
    dispatcher.include_router(show_dishes_router)
    dispatcher.startup.register(on_startup)
    # запустил бота
    await dispatcher.start_polling(bot)


# @dispatcher.message()
# async def echo_handler(message: types.Message):
#     name = message.from_user.first_name
#     txt = message.text
#     await message.answer(f'Привет, {name} \n {txt}!')


if __name__ == '__main__':
    asyncio.run(main())