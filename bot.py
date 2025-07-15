# bot.py
import os
import telegram
from telegram.ext import Updater, MessageHandler, Filters
from signal_engine import analyze_chart_and_generate_signal
from utils import download_image
from config import BOT_TOKEN, GROUP_ID

def handle_image(update, context):
    try:
        chat_id = update.message.chat_id
        if str(chat_id) != GROUP_ID:
            return
        
        photo_file = update.message.photo[-1].get_file()
        image_path = download_image(photo_file)
        
        result = analyze_chart_and_generate_signal(image_path)
        context.bot.send_message(chat_id=chat_id, text=result["text"])
        context.bot.send_photo(chat_id=chat_id, photo=open(result["image_path"], "rb"))
        
    except Exception as e:
        context.bot.send_message(chat_id=chat_id, text=f"⚠️ Error: {str(e)}")

def start_bot():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.photo, handle_image))
    updater.start_polling()
    updater.idle()
