import os
import glob

def calculate_tp_sl(entry, direction, spread=0.0, pip_size=0.01, reward=2, risk=1):
    """
    Calculates TP and SL based on standard R:R ratio logic.
    Automatically adapts to instrument pip size.
    """
    if direction.lower() in ["buy", "buy stop", "buy limit"]:
        sl = round(entry - (risk * pip_size), 2)
        tp = round(entry + (reward * pip_size), 2)
    else:
        sl = round(entry + (risk * pip_size), 2)
        tp = round(entry - (reward * pip_size), 2)

    return tp, sl

def get_pip_size(symbol_name):
    """
    Assigns pip size based on instrument class.
    """
    symbol_name = symbol_name.lower()
    if "gold" in symbol_name or "xau" in symbol_name:
        return 1.0
    elif "us30" in symbol_name or "nas100" in symbol_name or "ger30" in symbol_name:
        return 10.0
    elif "btc" in symbol_name or "eth" in symbol_name:
        return 5.0
    else:  # Forex pairs like EURUSD, GBPUSD, etc.
        return 0.0001

def clear_old_images(directory="./", extension="png"):
    """
    Automatically deletes previously analyzed images to prevent duplicate signals.
    """
    files = glob.glob(os.path.join(directory, f"*.{extension}"))
    for file in files:
        if "_marked" not in file:  # Preserve marked results
            os.remove(file)
