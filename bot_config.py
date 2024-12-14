from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values
from database import Database

token = dotenv_values('.env')['BOT_TOKEN']
bot = Bot(token=token)
dispatcher = Dispatcher()
database = Database('db.sqlite3')
