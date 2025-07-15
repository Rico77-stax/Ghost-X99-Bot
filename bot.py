import logging
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from config import BOT_TOKEN, GROUP_ID
from signal_engine import analyze_chart
from utils import download_telegram_file

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ghost X99 Quantum Lion Vortex Bot Activated ⚡️")

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file_path = await download_telegram_file(context.bot, photo.file_id)
    
    try:
        signal_data, marked_path = analyze_chart(file_path)
        caption = (
            f"📊 *Ghost X99 Signal*\n"
            f"Signal: *{signal_data['signal']}*\n"
            f"Entry: `{signal_data['entry']}`\n"
            f"TP: `{signal_data['tp']}`\n"
            f"SL: `{signal_data['sl']}`"
        )
        with open(marked_path, 'rb') as img:
            await context.bot.send_photo(chat_id=GROUP_ID, photo=InputFile(img), caption=caption, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

def start_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    app.run_polling()
