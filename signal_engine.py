from sniper_logics import apply_sniper_logics
from image_processor import extract_price_from_image, annotate_image

def generate_trade_signal(image_path):
    try:
        # Step 1: Extract price from chart screenshot using OCR
        current_price = extract_price_from_image(image_path)
        
        # Step 2: Analyze using sniper logic engine (all 36 logics included)
        signal_data = apply_sniper_logics(current_price)

        # Step 3: Annotate the chart with the signal and trade details
        annotated_path = annotate_image(
            image_path=image_path,
            signal=signal_data["signal"],
            entry=signal_data["entry"],
            tp=signal_data["tp"],
            sl=signal_data["sl"]
        )

        # Step 4: Return signal info and path to marked chart
        return {
            "signal": signal_data["signal"],
            "entry": signal_data["entry"],
            "tp": signal_data["tp"],
            "sl": signal_data["sl"],
            "annotated_image_path": annotated_path,
            "reasoning": signal_data["reasoning"]
        }

    except Exception as e:
        return {
            "error": str(e)
        }
