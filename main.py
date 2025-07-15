# main.py

from telegram.ext import ApplicationBuilder
from bot import setup_handlers
from config import BOT_TOKEN

def main():
    print("🧠 Starting Ghost X99 – Quantum Lion Vortex bot...")
    
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Setup message and image handlers
    setup_handlers(app)

    # Start polling
    print("🚀 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
