import asyncio

from handlers.picture import picture_router
from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.random import random_router
from bot_config import dispatcher, bot

async def main():
    dispatcher.include_router(start_router)
    dispatcher.include_router(picture_router)
    dispatcher.include_router(myinfo_router)
    dispatcher.include_router(random_router)
    # запустил бота
    await dispatcher.start_polling(bot)


# @dispatcher.message()
# async def echo_handler(message: types.Message):
#     name = message.from_user.first_name
#     txt = message.text
#     await message.answer(f'Привет, {name} \n {txt}!')


if __name__ == '__main__':
    asyncio.run(main())