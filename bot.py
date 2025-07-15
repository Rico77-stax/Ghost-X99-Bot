# import os
import telebot
from signal_engine import analyze_chart, annotate_chart
from PIL import Image
import time

# ✅ Your bot token and group ID (Already inserted)
BOT_TOKEN = "7974220853:AAE80t4o5-3UpZjRCaGDnnRcIMb0ZKbtXrk"
GROUP_ID = -1002824996503  # Your Telegram group

bot = telebot.TeleBot(BOT_TOKEN)

# 🔁 Track last message for deletion
last_msg_id = None
last_img_id = None

@bot.message_handler(content_types=['photo'])
def handle_chart(message):
    global last_msg_id, last_img_id

    if message.chat.id != GROUP_ID:
        bot.reply_to(message, "❌ Unauthorized. Only allowed in Ghost X99 group.")
        return

    # ⏳ Download image
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    img_path = f"screenshot_{int(time.time())}.png"
    with open(img_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    # 🧼 Delete old messages
    try:
        if last_msg_id:
            bot.delete_message(GROUP_ID, last_msg_id)
        if last_img_id:
            bot.delete_message(GROUP_ID, last_img_id)
    except:
        pass

    # 🔍 Analyze
    result = analyze_chart(img_path)
    annotated_path = annotate_chart(img_path, result)

    # 📤 Send annotated image
    sent_img = bot.send_photo(GROUP_ID, photo=open(annotated_path, 'rb'))
    last_img_id = sent_img.message_id

    # 📢 Send Signal Info
    text = (
        f"📸 *Ghost X99 – Sniper Signal*\n\n"
        f"🧭 Signal: *{result['signal']}*\n"
        f"🎯 Entry: `{result['entry']}`\n"
        f"🎯 TP: `{result['tp']}`\n"
        f"🛡️ SL: `{result['sl']}`\n\n"
        f"🧠 Reason: _{result['reason']}_"
    )
    sent_msg = bot.send_message(GROUP_ID, text, parse_mode="Markdown")
    last_msg_id = sent_msg.message_id

    # 🧼 Cleanup
    os.remove(img_path)
    os.remove(annotated_path)

# 🔁 Start polling
print("🤖 Ghost X99 – Vortex Sniper is now running...")
bot.infinity_polling()
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
