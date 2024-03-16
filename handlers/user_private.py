from random import randint
from pathlib import Path

from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import FSInputFile
from aiogram import types, Router, Bot, F
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter
from keyboards import reply
from keyboards.reply import get_keyboard

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


def choose_pic_Nikita_Igorevich():
    return FSInputFile(f'Cats/{randint(1, len(list(Path("Cats").iterdir())))}.jpg')


@user_private_router.message(CommandStart())
async def start_cmd_Nikita_Igorevich(message: types.Message):
    await message.answer('Привет, я бот отправляющий рандомных котиков! Напиши мне "Хочу котика" '
                         'и я покажу тебе котика!',
                         reply_markup=get_keyboard(
                             "Меню",
                             "О боте",
                             "Донат",
                             "GitHub",
                             placeholder="Что тебе нужно? Котика?",
                             sizes=(2, 2)
                         ),
    )


@user_private_router.message(or_f(Command('menu'), (F.text.lower() == 'меню')))
async def menu_cmd(message: types.Message):
    await message.answer('Вот меню')


@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f'Номер получен 😍')
    await message.answer(str(message.contact))


@user_private_router.message(F.location)
async def get_contact(message: types.Message):
    await message.answer(f'Локация получена 😍')
    await message.answer(str(message.location))


@user_private_router.message((F.text.lower() == "о нас") | (F.text.lower() == 'о боте'))
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer('Я бот! Я могу показать тебе котика и, возможно, что-то ещё, но мой кодер ленивый '
                         'и не написал об это тут. Я его обязательно пну на этот счёт! Посмотри пока котика!')


@user_private_router.message((F.text.lower().contains('донат')) | (F.text.lower() == 'донат'))
@user_private_router.message(Command('donate'))
async def donate_cmd(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold("Варианты доната:"),
            "Бусти",
            "Патреон",
            "На Каспи/СберОнлайн переведи, если кайф",
            marker='☑️ ',
        ),
        as_marked_section(
            Bold('Нельзя: '),
            'Закинуть на QIWI (RIP)',
            'Закинуть на СберКнижку',
            'Расплатиться натурой',
            marker='⛔️ ',
        ),
        sep='\n------------------\n'
    )
    await message.answer(text.as_html())


@user_private_router.message((F.text.lower() == 'гит') | (F.text.lower() == 'github'))
@user_private_router.message(Command('git'))
async def git_cmd(message: types.Message):
    await message.answer('https://github.com/LibinoNK/RandomCatBot-Fun-/blob/main/main.py')


@user_private_router.message(F.photo)
async def photo_cmd(message: types.Message, bot: Bot):
    await message.answer('Спасибо за фото! Если это котик и фотография понравится Богу котячьего рандома, '
                         'то он рано или поздно попадет в подборку!')
    await bot.download(
        message.photo[-1],
        destination=f"/Users/libino/Desktop/Учеба/EndProject/New_Cats/{message.photo[-1].file_id}.jpg"
    )


@user_private_router.message()
async def answer_Nikita_Igorevich(message: types.Message, bot: Bot):
    text: str | None = message.text
    if text.lower() in ['привет', 'hi', 'hello']:
        await message.answer('Здравствуй!')
    elif text.lower() in ['пока', 'bue', 'до свидания']:
        await message.answer('До встречи!')
    elif text.lower() in ['главный вопрос жизни, вселенной и вообще', 'смысл жизни']:
        await message.answer('42')
    elif text.lower() == 'хочу котика':
        await bot.send_photo(chat_id=message.chat.id, photo=choose_pic_Nikita_Igorevich())
    else:
        await message.answer('Извини, я тебя не понимаю! Попробуй написать что-то другое :3')
        # await message.answer(message.text) # echo
