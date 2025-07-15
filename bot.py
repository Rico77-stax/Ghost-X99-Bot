import os
import logging
from telegram import Update, InputFile
from telegram.ext import (
    ApplicationBuilder, MessageHandler, filters, ContextTypes
)
from config import BOT_TOKEN, GROUP_ID
from image_processor import extract_price_from_image, annotate_image
from signal_engine import generate_signal
import shutil

logging.basicConfig(level=logging.INFO)

# Store last annotated file to delete on next signal
LAST_IMAGE = None

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global LAST_IMAGE

    if update.effective_chat.id != GROUP_ID:
        return

    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    file_path = f"downloads/{photo.file_id}.png"
    await file.download_to_drive(file_path)

    try:
        current_price = extract_price_from_image(file_path)
        signal_data = generate_signal(file_path, current_price)

        if LAST_IMAGE:
            try:
                await context.bot.delete_message(chat_id=GROUP_ID, message_id=LAST_IMAGE)
            except:
                pass

        annotated_path = annotate_image(file_path, signal_data['signal'], signal_data['entry'], signal_data['tp'], signal_data['sl'])

        caption = f"""
📡 *Quantum Ghost X99 – Vortex Signal*

📈 *Signal:* {signal_data['signal']}
🎯 *Entry:* {signal_data['entry']}
🎯 *TP:* {signal_data['tp']}
🛡 *SL:* {signal_data['sl']}
🧠 *Reason:* {signal_data['reason']}
        """.strip()

        sent = await context.bot.send_photo(
            chat_id=GROUP_ID,
            photo=InputFile(annotated_path),
            caption=caption,
            parse_mode="Markdown"
        )

        LAST_IMAGE = sent.message_id

    except Exception as e:
        logging.error(f"Error processing image: {e}")
        await update.message.reply_text("⚠️ Error analyzing screenshot. Make sure it’s a clear MT4/MT5 chart.")

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(annotated_path):
            os.remove(annotated_path)

def start_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    logging.info("Bot is running...")
    app.run_polling()
