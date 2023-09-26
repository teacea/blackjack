import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message, User

import keyboard as kb

import random
import os

import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN=os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp= Dispatcher()

user = {'in_game': False,
        'total_games': 0,
        'wins': 0}

@dp.message(F.text == '/start')
async def cmd_start(message):
    await message.answer(f'Добро пожаловать!', reply_markup=kb.main)


def get_random_number() -> int:
    cards_list = [6,7,8,9,10,2,3,4,11]*4
    random.shuffle(cards_list)
    card=cards_list.pop(1)
    return card

card = get_random_number()

@dp.message(F.text == 'Новая игра')
async def cmd_start_game(message):
    user['in_game'] = True
    global card
    card_sum = 0
    card_sum+=card
    await message.answer(f'Вам выпало:{card}. Выберите действие:', reply_markup=kb.game)

card_sum=0
@dp.message(F.text == 'ещё карту')
async def cmd_game(message):
    card = get_random_number()
    
    while True:
        if user['in_game']:
            global card_sum
            card_sum+=card
            if card_sum<21:
                await message.answer(f'Вам выпало:{card}. Выберите действие:', reply_markup=kb.game)
                break
            
            elif card_sum == 21:
                user['total_games'] += 1
                user['wins'] += 1
                await message.answer(f'Вам выпало:{card}. и вы выйграли!', reply_markup=kb.main)
                card_sum=0
                user['in_game'] =False
                break
            elif card_sum>21:
                user['total_games'] += 1
                await message.answer(f'Вам выпало:{card}. и вы проиграли(', reply_markup=kb.main)
                card_sum=0
                user['in_game']=False
                break
        else:
            await message.answer(f'мне кажется, вы не в игре!', reply_markup=kb.main)
            break
@dp.message(F.text == 'достаточно!')
async def cmd_start_game(message):
    if user['in_game']:
        user['total_games'] += 1
        user['in_game']=False
        await message.answer(f'Ваша сумма:{card_sum}. К сожалению, вы проиграли(', reply_markup=kb.main)
   
    else:
            await message.answer(f'мне кажется, вы не в игре!', reply_markup=kb.main)
@dp.message(F.text == 'Назад')
async def cmd_game(message):
    await message.answer('Главное меню:', reply_markup=kb.main)

@dp.message(F.text == 'Выйти из игры')
async def cmd_cancel(message):
    if user['in_game']:
        user['in_game'] = False
        await message.answer(
            'Вы вышли из игры.', reply_markup=kb.main
        )
    else:
        await message.answer(
            'Нельзя выйти из игры, так как она не начата.'
        )

@dp.message(F.text == 'Профиль')
async def cmd_profile(message):
    await message.answer(
        f'Всего игр сыграно: {user["total_games"]}\n'
        f'Игр выиграно: {user["wins"]}',
          reply_markup=kb.cancel)


@dp.message(F.text == 'Описание игры')
async def cmd_cancel(message):
    await message.answer(f'Основная задача игры-набрать сумму карт, которя будет равна 21.\n'
                         f'Карты выдаются случайным образом от 2 до 4 и от 6 до 11.\n'
                         f'если сумма больше, чем 21- вы проиграли.\n',
                         reply_markup=kb.cancel)
    
@dp.message()
async def cmd_other(message):
    if user['in_game']:
        await message.answer(f'либо еще, либо достаточно- другого не дано...', reply_markup=kb.game)
    else:
        await message.answer(f'Выберите пункт ниже: ', reply_markup=kb.main)

if __name__ == '__main__':
    dp.run_polling(bot)
