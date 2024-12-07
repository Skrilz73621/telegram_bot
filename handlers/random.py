from aiogram import types, Router
from aiogram.filters import Command
import random

random_router = Router()

@random_router.message(Command('random'))
async def random_handler(message: types.Message):
    list_of_pizzas = [
        {
            'name':'Баварская',
            'description':'Охотничьи колбаски, маринованные огурчики, красный лук, томаты, горчичный соус, моцарелла, томатный соус',
            'img': 'images/Bavarskaya.jpeg'
        },
        {
            'name':'Чикке Бомбони',
            'description':'Куриные кусочки в панировке, сладкий перчик, сыры чеддер, пармезан и моцарелла, красный лук, соусы сладкий чили и альфредо',
            'img': 'images/Chiken_bomboni.jpeg'
        },
        {
            'name': 'Сырная',
            'description': 'Моцарелла, смесь сыров чеддер и пармезан, соус альфредо',
            'img': 'images/Surnaya.jpeg'
        },
        {
            'name': 'Ветчина и сыр',
            'description': 'Ветчина из цыпленка, увеличенная порция моцареллы, соус альфредо',
            'img': 'images/Vetchina_i_sir.jpeg'
        },
    ]
    random_pizza = random.choice(list_of_pizzas)
    pizza_name = random_pizza['name']
    pizza_description = random_pizza['description']
    pizza_img_path = random_pizza['img']
    pizza_img = types.FSInputFile(pizza_img_path)
    await message.answer_photo(photo=pizza_img, caption=pizza_name + '\n\n' + pizza_description)