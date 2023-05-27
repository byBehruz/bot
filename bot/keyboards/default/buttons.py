from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from api import *
from aiogram.utils.callback_data import CallbackData


choose_language = ReplyKeyboardMarkup(resize_keyboard=True)
choose_language.insert(KeyboardButton(text="🇺🇿 Ozbekcha")).insert(KeyboardButton(text='🇷🇺 Русский'))


main_uz = ReplyKeyboardMarkup(resize_keyboard=True)
main_uz.row(KeyboardButton(text='Menu')).row(
    KeyboardButton(text='Modelar')
).row(KeyboardButton(text='Comment'),KeyboardButton(text='Sozlamalar'))

main_ru= ReplyKeyboardMarkup(resize_keyboard=True)
main_ru.row(KeyboardButton(text='Mеню')).row(
    KeyboardButton(text='Модели'),
).row(KeyboardButton(text='Комент'),KeyboardButton(text='Настройки'))

 ###### categories button######
def categories(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    datas = get_categories(language)
    for data in datas:
        button.insert(KeyboardButton(text=data))
    if language=='uz':
        button.row(KeyboardButton(text='Orqaga'),KeyboardButton(text='Model'))
    if language=='ru':
        button.row(KeyboardButton(text='Назад'),KeyboardButton(text='Модель'))
    datas = get_categories(language)
    for data in datas:
        button.insert(KeyboardButton(text=data))
    return button
# ##### product #######
# def product(category, language product=None):
#     data= category