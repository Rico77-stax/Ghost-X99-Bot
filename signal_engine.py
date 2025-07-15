from sniper_logics import apply_sniper_logics
from image_processor import extract_price_from_image
from utils import calculate_tp_sl

def generate_trade_signal(image_path):
    try:
        # Step 1: OCR to extract the current price near the end of screenshot
        current_price = extract_price_from_image(image_path)

        # Step 2: Analyze chart and run 36+ sniper logic confluences
        signal_result = apply_sniper_logics(image_path, current_price)

        if not signal_result or "signal" not in signal_result:
            return {
                "signal": "No valid signal",
                "entry": current_price,
                "tp": None,
                "sl": None,
                "reason": "No sniper logic confirmed at screenshot edge"
            }

        signal_type = signal_result["signal"]

        # Step 3: Generate dynamic TP and SL based on confluence zones
        tp, sl = calculate_tp_sl(current_price, signal_type)

        return {
            "signal": signal_type,
            "entry": current_price,
            "tp": tp,
            "sl": sl,
            "reason": signal_result.get("reason", "Sniper logic confirmed")
        }

    except Exception as e:
        return {
            "signal": "Error",
            "entry": None,
            "tp": None,
            "sl": None,
            "reason": str(e)
        }
