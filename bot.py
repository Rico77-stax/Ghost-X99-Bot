from telegram.ext import Updater, MessageHandler, Filters
from signal_engine import process_image
import os

BOT_TOKEN = "7974220853:AAE80t4o5-3UpZjRCaGDnnRcIMb0ZKbtXrk"

def handle_photo(update, context):
    photo = update.message.photo[-1].get_file()
    file_path = "latest_chart.jpg"
    photo.download(file_path)

    update.message.reply_text("📥 Image received. Running Ghost X99 sniper scan...")

    signal = process_image(file_path)
    
    if signal:
        update.message.reply_text(f"✅ Signal Found:\n{signal}\n\nAnalysis Done By Ghost X99.")
    else:
        update.message.reply_text("⚠️ No sniper setup found. Drop another chart after 20 minutes.\n\nAnalysis Done By Ghost X99.")

    os.remove(file_path)

def start_bot():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.photo, handle_photo))

    updater.start_polling()
    updater.idle()
