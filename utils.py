import os import logging from datetime import datetime

def create_directory(path): if not os.path.exists(path): os.makedirs(path)

def setup_logger(): log_dir = "logs" create_directory(log_dir) log_file = os.path.join(log_dir, f"log_{datetime.now().strftime('%Y%m%d')}.log")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

return logging.getLogger("GhostX99Bot")

def format_signal_message(signal_data): return ( f"\u2728 Ghost X99 Signal \u2728\n" f"Signal: {signal_data['signal']}\n" f"Entry: {signal_data['entry']}\n" f"TP: {signal_data['tp']}\n" f"SL: {signal_data['sl']}\n" f"Timeframe: {signal_data['timeframe']}\n" f"Reason: {signal_data['reason']}\n" )

