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

    chat_id = message.chat.id

    try:
        # 1️⃣ видаляємо повідомлення користувача
        bot.delete_message(chat_id, message.message_id)
    except Exception:
        pass  # якщо не вийшло — просто ігноруємо

    # 2️⃣ надсилаємо НОВЕ повідомлення (без reply)
    bot.send_message(chat_id, converted)

if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)
