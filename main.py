import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ChatMemberUpdated
from datetime import datetime
import os

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# Замените на токен вашего бота
BOT_TOKEN = "7720705041:AAF_OhKsVZV1QGca-gh_kM0Lc90brfuDUF8"
TOKEN = os.environ.get("7720705041:AAF_OhKsVZV1QGca-gh_kM0Lc90brfuDUF8")

# ID пользователя, сообщения которого нужно отслеживать
PASHA_ID = 722401589  # Паша
SASHA_ID = 1038044523  # Саша
#TARGET_USER_ID2 = 642818159  # Укажите нужный user_id

# Список возможных ответов бота
PASHA_RESPONSES = [
    "Иди нахер, даун",
    "И чё, долбаёб",
    "Нет, ты даун",
    "Иди нахер, долбаёб",
    "Ладно, даун, ладно",
    "Ты долбаёб просто",
    "А ты даун"
]

SASHA_RESPONSES = [
    "Ладно, Саша, ладно",
    "Свинье слово не давали",
    "Как же ты заебал спамить хуйню",
    "Как же ты заебал спамить хуйню",
    "Как же ты заебал спамить хуйню"
]

GOOD_RESPONSES = [
    "Ты сегодня просто супер!",
    "Хорошего тебе дня)",
    "Держи котика для настроения 🐈",
    "Оно тебе надо?",
    "Лучше бы в казино депнули",
    "Слова моей подружки",
    "Ахахахаахах",
    "АХАХАХАХАХАХААХ",
    "Ладно",
    "Без личностей",
    "В жизни нужно чтобы не всё было хорошо\n\n© Павел Ильич"

]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def calculate_days_to_may():
    today = datetime.now()
    may_first = datetime(2025, 5, 1)
    delta = may_first - today
    return delta.days

@dp.message_handler(commands=['mayskie'])
async def send_days_to_may(message: types.Message):
    days_left = calculate_days_to_may()
    await message.reply(f"До майских осталось {days_left} дней ☀️")


@dp.chat_member()
async def on_new_chat_member(update: ChatMemberUpdated):
    """Обработчик события добавления бота в чат."""
    if update.new_chat_member.user.id == (await bot.me()).id:
        await bot.send_message(update.chat.id, "Идите нахер")


@dp.message_handler(lambda message: "иди" in message.text.lower())
async def reply_idi(message: types.Message):
    # Разделяем текст на части после "иди" (регистронезависимо)
    text_after_idi = message.text.lower().split("иди", 1)[-1].strip()

    # Формируем ответ: "иди..." + остальной текст (в оригинальном регистре)
    reply_text = f"Сам(а) иди{text_after_idi}"
    await message.reply(reply_text)


@dp.message()
async def reply_to_target_user(message: types.Message):
    if message.from_user.id == PASHA_ID:
        is_answer = random.randint(0, 8)
        if is_answer == 1:
            response = random.choice(PASHA_RESPONSES)
            await message.reply(response)
    if message.from_user.id == SASHA_ID:
        is_answer = random.randint(0, 13)
        if is_answer == 1:
            response = random.choice(SASHA_RESPONSES)
            await message.reply(response)
    if message.from_user.id != SASHA_ID and message.from_user.id != PASHA_ID:
        is_answer = random.randint(0, 15)
        if is_answer == 1:
            response = random.choice(GOOD_RESPONSES)
            await message.reply(response)
  #  if message.from_user.id == TARGET_USER_ID2:
   #     await message.reply("проверка")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
