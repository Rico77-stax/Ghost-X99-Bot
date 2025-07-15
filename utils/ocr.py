import re

def clean_text(text):
    """Remove unwanted characters and normalize whitespace."""
    return re.sub(r'\s+', ' ', text).strip()

def detect_asset_class(pair_name):
    pair_name = pair_name.upper()
    if any(x in pair_name for x in ["GOLD", "XAU", "SILVER"]):
        return "metals"
    elif any(x in pair_name for x in ["NAS", "SPX", "DJ", "US30", "GER", "DE30"]):
        return "indices"
    elif any(x in pair_name for x in ["BTC", "ETH", "CRYPTO"]):
        return "crypto"
    elif any(x in pair_name for x in ["USD", "EUR", "GBP", "JPY", "AUD", "NZD", "CAD", "CHF"]):
        return "forex"
    else:
        return "unknown"

def get_pip_size(asset_class):
    """Define pip size by asset class."""
    if asset_class == "forex":
        return 0.0001
    elif asset_class == "metals":
        return 0.10
    elif asset_class == "indices":
        return 1.0
    elif asset_class == "crypto":
        return 1.0
    else:
        return 0.01

def calculate_tp_sl(entry, direction, pip_size, risk_ratio=2):
    """Auto calculate TP and SL based on direction and pip size."""
    sl_pips = 20 * pip_size
    tp_pips = sl_pips * risk_ratio

    if direction.lower() == "buy":
        tp = round(entry + tp_pips, 2)
        sl = round(entry - sl_pips, 2)
    else:
        tp = round(entry - tp_pips, 2)
        sl = round(entry + sl_pips, 2)

    return tp, sl
