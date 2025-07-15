import os
import logging
from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from signal_engine import analyze_chart_and_generate_signal

# ✅ Your real bot credentials
TELEGRAM_BOT_TOKEN = "7974220853:AAE80t4o5-3UpZjRCaGDnnRcIMb0ZKbtXrk"
TELEGRAM_GROUP_ID = -1002824996503

# ✅ Logging for debug
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# ✅ This function is triggered when a screenshot/image is sent
def handle_image(update: Update, context: CallbackContext):
    try:
        photo_file = update.message.photo[-1].get_file()
        image_path = "latest_chart.png"
        photo_file.download(image_path)
        update.message.reply_text("🧠 Processing chart... Please wait ⏳")

        # Analyze chart
        signal_text, annotated_image_path = analyze_chart_and_generate_signal(image_path)

        # Send result
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(annotated_image_path, 'rb'), caption=signal_text)

    except Exception as e:
        logger.error(f"❌ Error handling image: {e}")
        update.message.reply_text("⚠️ An error occurred while analyzing the chart. Please try again.")

# ✅ Start the bot
def start_bot():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    updater = Updater(bot.token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.photo, handle_image))

    updater.start_polling()
    print("🤖 Ghost X99 Bot is now running...")
    updater.idle()
