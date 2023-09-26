from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton


game_kb = [[
    KeyboardButton(text='ещё карту'),
    KeyboardButton(text='достаточно!')]
]
main_kb = [[KeyboardButton(text='Новая игра')],
           [KeyboardButton(text='Описание игры')],
           [KeyboardButton(text='Профиль')]]

cancel_kb = [[KeyboardButton(text='Назад')]]

cancel = ReplyKeyboardMarkup(keyboard=cancel_kb,
                      resize_keyboard=True,
                      input_field_placeholder='Назад')


main = ReplyKeyboardMarkup(keyboard=main_kb,
                      resize_keyboard=True,
                      input_field_placeholder='Нажмите, чтобы начать')
game = ReplyKeyboardMarkup(keyboard=game_kb,
                      resize_keyboard=True,
                      input_field_placeholder='')