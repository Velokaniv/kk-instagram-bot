import re
import os
from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

INSTAGRAM_REGEX = re.compile(r'(https?://)?(www\.)?instagram\.com/\S+')

@dp.message_handler()
async def handle_message(message: types.Message):
    text = message.text or ""
    match = INSTAGRAM_REGEX.search(text)

    if not match:
        return

    url = match.group(0)

    converted = (
        url
        .replace("https://", "")
        .replace("http://", "")
        .replace("www.", "kk")
    )

    await message.reply(converted)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
