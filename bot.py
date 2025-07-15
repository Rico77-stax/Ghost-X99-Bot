# bot.py

import os
import telebot
from config import BOT_TOKEN, TELEGRAM_GROUP_ID, SCREENSHOT_DIR
from signal_engine import analyze_chart_image
from utils import cleanup_old_images

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# Ensure screenshot directory exists
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# 🖼️ Handle incoming photo messages
@bot.message_handler(content_types=["photo"])
def handle_screenshot(message):
    chat_id = message.chat.id
    if chat_id != TELEGRAM_GROUP_ID:
        bot.reply_to(message, "⚠️ Sorry, this bot only works in the authorized group.")
        return

    cleanup_old_images()

    # Save the image
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    filename = os.path.join(SCREENSHOT_DIR, f"chart_{message.message_id}.jpg")
    with open(filename, 'wb') as f:
        f.write(downloaded_file)

    # Analyze and get signal
    try:
        signal_result, annotated_image_path = analyze_chart_image(filename)
        if signal_result:
            with open(annotated_image_path, 'rb') as photo:
                bot.send_photo(chat_id, photo, caption=signal_result)
        else:
            bot.send_message(chat_id, "📉 No valid signal found based on the sniper logics.")
    except Exception as e:
        bot.send_message(chat_id, f"❌ Error processing screenshot: {str(e)}")

# ✅ Start bot polling
def run_bot():
    print("🤖 Ghost X99 Bot is running...")
    bot.infinity_polling()
