import os
import re
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

INSTAGRAM_REGEX = re.compile(r'(https?://)?(www\.)?instagram\.com/\S+')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
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

    bot.reply_to(message, converted)

if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)
