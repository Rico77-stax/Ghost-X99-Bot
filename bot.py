import logging
from telegram import Update, InputFile
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    filters,
    ContextTypes,
)
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_GROUP_ID
from image_processor import annotate_image
from signal_engine import analyze_chart

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != TELEGRAM_GROUP_ID:
        return

    photo_file = await update.message.photo[-1].get_file()
    photo_path = f"{photo_file.file_id}.jpg"
    await photo_file.download_to_drive(photo_path)

    try:
        signal_data = analyze_chart(photo_path)
        annotated_path = annotate_image(
            photo_path,
            signal=signal_data["signal"],
            entry=signal_data["entry"],
            tp=signal_data["tp"],
            sl=signal_data["sl"],
        )

        await context.bot.send_photo(
            chat_id=TELEGRAM_GROUP_ID,
            photo=InputFile(annotated_path),
            caption=(
                f"📡 *Ghost X99 Signal*\n\n"
                f"*Type:* {signal_data['signal']}\n"
                f"*Entry:* {signal_data['entry']}\n"
                f"*TP:* {signal_data['tp']}\n"
                f"*SL:* {signal_data['sl']}"
            ),
            parse_mode="Markdown"
        )

    except Exception as e:
        await context.bot.send_message(
            chat_id=TELEGRAM_GROUP_ID,
            text=f"⚠️ Error processing image: {str(e)}"
        )

def start_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.run_polling()
