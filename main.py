import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ChatMemberUpdated
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

GOOD_RESPONSES = [
    "Ты сегодня просто супер!",
    "Хорошего тебе дня)",
    "Держи котика для настроения 🐈",
    "Относить к другим так, как хочешь чтобы относились к тебе",
    "Лучше бы в казино депнули",
    "Дружеское напоминание: гордость - источник всех грехов",
    "И чё?",
    "В жизни нужно чтобы не всё было хорошо\n\n©Павел Ильич",

]

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.chat_member()
async def on_new_chat_member(update: ChatMemberUpdated):
    """Обработчик события добавления бота в чат."""
    if update.new_chat_member.user.id == (await bot.me()).id:
        await bot.send_message(update.chat.id, "Идите нахер")

@dp.message()
async def reply_to_target_user(message: types.Message):
    if message.from_user.id == PASHA_ID:
        is_answer = random.randint(0, 7)
        if is_answer == 1:
            response = random.choice(PASHA_RESPONSES)
            await message.reply(response)
    else:
        is_answer = random.randint(0, 10)
        if is_answer == 1:
            response = random.choice(GOOD_RESPONSES)
            await message.reply(response)

  #  if message.from_user.id == TARGET_USER_ID2:
   #     await message.reply("проверка")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
