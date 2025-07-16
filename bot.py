from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os
from config import BOT_TOKEN
from image_processor import extract_price_from_image, annotate_image
from signal_engine import analyze_signal

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🚀 Ghost X99 Bot is online and ready to receive chart screenshots!")

def handle_photo(update: Update, context: CallbackContext):
    photo = update.message.photo[-1]
    file = photo.get_file()
    image_path = f"chart_{update.message.message_id}.png"
    file.download(image_path)

    try:
        current_price = extract_price_from_image(image_path)
        timeframe = "M15" if "15" in image_path else "H1"
        signal, entry, tp, sl, logic_used = analyze_signal(image_path, current_price, timeframe)

        annotated_image = annotate_image(image_path, signal, entry, tp, sl)

        message = (
            f"📊 Signal: {signal}\n"
            f"🔢 Entry: {entry}\n"
            f"🎯 TP: {tp}\n"
            f"🛡 SL: {sl}\n"
            f"📚 Logic: {logic_used}"
        )

        update.message.reply_photo(photo=open(annotated_image, "rb"), caption=message)

    except Exception as e:
        update.message.reply_text(f"❌ Error: {str(e)}")

    finally:
        if os.path.exists(image_path):
            os.remove(image_path)

def start_bot():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))

    updater.start_polling()
    updater.idle()
