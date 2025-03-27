import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ChatMemberUpdated
from aiogram.filters import ChatMemberUpdatedFilter

# Замените на токен вашего бота
BOT_TOKEN = "7720705041:AAF_OhKsVZV1QGca-gh_kM0Lc90brfuDUF8"
# ID пользователя, сообщения которого нужно отслеживать
TARGET_USER_ID = 8166794940  # Укажите нужный user_id
TARGET_USER_ID2 = 642818159  # Укажите нужный user_id

# Список возможных ответов бота
RESPONSES = [
    "Иди нахер, даун",
    "И чё, долбаёб",
    "Нет, ты даун",
    "Иди нахер, долбаёб",
    "Ладно, даун, ладно",
    "Ты долбаёб просто",
    "А ты даун"
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
    """Отвечает на каждое сообщение определенного пользователя."""
    if message.from_user.id == TARGET_USER_ID:
        response = random.choice(RESPONSES)
        await message.reply(response)

    if message.from_user.id == TARGET_USER_ID2:
        await message.reply("йоу")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
