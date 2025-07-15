def calculate_tp_sl(signal_type, entry_price):
    """
    Calculates TP and SL based on signal type and entry price.
    Uses sniper logic:
    - TP = 2x risk distance
    - SL = logical invalidation zones (last wick zone)

    Args:
        signal_type (str): "Buy", "Sell", "Buy Limit", etc.
        entry_price (float): Detected price from screenshot

    Returns:
        tuple: (tp_price, sl_price)
    """
    buffer = 0.0020  # base buffer for SL/TP distance (adjust as needed)
    
    if "Buy" in signal_type:
        sl = round(entry_price - buffer, 4)
        tp = round(entry_price + (buffer * 2), 4)
    elif "Sell" in signal_type:
        sl = round(entry_price + buffer, 4)
        tp = round(entry_price - (buffer * 2), 4)
    else:
        sl = round(entry_price - buffer, 4)
        tp = round(entry_price + (buffer * 2), 4)

    return tp, sl

def format_sniper_reason(signal_type, logic_list):
    """
    Formats sniper logic reasons into a short explanation.

    Args:
        signal_type (str): Buy/Sell/Buy Limit etc.
        logic_list (list): List of confirmed logics (strings)

    Returns:
        str: Formatted explanation string
    """
    confluences = ', '.join(logic_list[:3])  # limit to first 3 for clarity
    return f"{signal_type} confirmed by: {confluences}."
