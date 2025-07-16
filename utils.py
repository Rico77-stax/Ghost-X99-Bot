import logging
from datetime import datetime

def setup_logging():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

def log_signal(signal_type, pair, timeframe, entry, tp, sl):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (
        f"[{now}] SIGNAL: {signal_type} | Pair: {pair} | Timeframe: {timeframe} | "
        f"Entry: {entry} | TP: {tp} | SL: {sl}"
    )
    logging.info(log_entry)
