from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.buttons import *
from api import *
from states.languages import Language
from loader import dp
from aiogram.dispatcher import FSMContext


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    full_name= message.from_user.first_name
    telegram_id = message.from_user.id
    check = create(name=full_name, telegram_id=telegram_id)
    if check==400:
        language=language_info(telegram_id)
        if language=='uz':
            await message.answer('Bosh menyuga xush kelibsiz!\n'\
                f'Boshlaysizmi ishni ?',reply_markup=main_uz)
        if language=='ru':
            await message.answer(f'добро пожаловать в меню!\n'\
                f'Начнем работу?', reply_markup=main_ru)
    else:
        await message.answer(f' 🇺🇿 Botdan foydalanish uchun tilni tanlang.\n'\
            f'🇷🇺 Выберите удобный язык для вас', reply_markup=choose_language)
        create(full_name,telegram_id=telegram_id)
    await Language.language.set()


@dp.message_handler(state=Language.language)
async def set_language_system(message:types.Message, state:FSMContext):
    if message.content_type=='text':
        if message.text in ["🇺🇿 O'zbekcha", "🇷🇺 Русский"]:
            if message.text=="🇺🇿 O'zbekcha":
                change_language(telegram_id=message.from_user.id, language='uz')
                await message.answer('Bosh menyuga xush kelibsiz!', reply_markup=main_uz)
            else: 
                change_language(telegram_id=message.from_user.id, language='ru')
                await message.answer('Добро пожаловать в главное меню', reply_markup=main_ru)
            await state.finish()
        else:
            await message.answer(f"🇺🇿 Botdan foydalanish uchun o'zingizga qulay tilni tanlang. \n"\
                                f"🇷🇺 Выберите удобный для вас язык для использования бота.",
                                reply_markup=choose_language)
            await Language.language.set()
    else:
        await message.answer("🇺🇿 Botdan foydalanish uchun o'zingizga qulay tilni tanlang.\n"\
                            f"🇷🇺 Выберите удобный для вас язык для использования бота.", reply_markup=choose_language)
        await state.finish()



