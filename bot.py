# bot.py

import logging
from telegram import Update, InputFile
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from signal_engine import analyze_image_and_generate_signal
from config import BOT_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👻 Ghost X99 is online and ready!")

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    photo_file = await photo.get_file()
    image_path = f"downloads/{photo.file_id}.jpg"
    await photo_file.download_to_drive(image_path)

    try:
        signal, entry, tp, sl, marked_image_path = analyze_image_and_generate_signal(image_path)
        with open(marked_image_path, "rb") as image_file:
            await update.message.reply_photo(
                photo=InputFile(image_file),
                caption=f"""
📡 Signal: {signal}
🎯 Entry: {entry}
✅ TP: {tp}
❌ SL: {sl}
"""
            )
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error processing image:\n{e}")

def start_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    app.run_polling()
