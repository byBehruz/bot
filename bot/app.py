from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.set_bot_commands import set_default_commands
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.buttons import *
from api import *
from states.languages import Language
from loader import dp
from aiogram.dispatcher import FSMContext







async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)




if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
