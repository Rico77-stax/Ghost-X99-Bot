from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN, GROUP_ID
from signal_engine import process_image
import os
import asyncio

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != GROUP_ID:
        return

    photo_file = await update.message.photo[-1].get_file()
    image_path = "latest_chart.jpg"
    
    if os.path.exists(image_path):
        os.remove(image_path)

    await photo_file.download_to_drive(image_path)
    await asyncio.sleep(3)

    signal = process_image(image_path)
    if signal:
        await context.bot.send_message(chat_id=GROUP_ID, text=signal)
    else:
        await context.bot.send_message(
            chat_id=GROUP_ID,
            text="No sniper setup found. Drop another screenshot in 20 minutes.\n\n🧠 *Analysis Done By Ghost X99*",
            parse_mode="Markdown"
        )

def start_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    print("🤖 Ghost X99 Bot is live!")
    app.run_polling()
