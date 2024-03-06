import asyncio
import os
from pathlib import Path

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from random import randint
from aiogram.types import FSInputFile
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()


def choose_pic_Nikita_Igorevich():
    return FSInputFile(f'Cats/{randint(1, len(list(Path("Cats").iterdir())))}.jpg')


@dp.message(CommandStart())
async def start_cmd_Nikita_Igorevich(message: types.Message):
    await message.answer('Напиши мне "Хочу котика" и я покажу тебе котика!')


@dp.message()
async def answer_Nikita_Igorevich(message: types.Message, bot: Bot):
    text: str | None = message.text
    if text.lower() in ['привет', 'hi', 'hello']:
        await message.answer('Здравствуй!')
    elif text.lower() in ['пока', 'bue', 'до свидания']:
        await message.answer('До встречи!')
    elif text.lower() in ['Главный вопрос жизни, вселенной и вообще', 'смысл жизни']:
        await message.answer('42')
    elif text.lower() == 'хочу котика':
        await bot.send_photo(chat_id=message.chat.id, photo=choose_pic_Nikita_Igorevich())
    else:
        await message.answer(message.text)


async def main_Nikita_Igorevich():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main_Nikita_Igorevich())
