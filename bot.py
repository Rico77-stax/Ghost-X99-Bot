import telebot
import os
from signal_engine import analyze_chart

TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if message.chat.id != GROUP_ID:
        return

    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_path = f"temp/{file_info.file_id}.jpg"

    with open(file_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    result_text, marked_image_path = analyze_chart(file_path)

    bot.send_message(GROUP_ID, result_text)
    with open(marked_image_path, 'rb') as img:
        bot.send_photo(GROUP_ID, img)

    os.remove(file_path)
    os.remove(marked_image_path)

def start_bot():
    print("Bot running...")
    bot.polling()
