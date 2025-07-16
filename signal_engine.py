from image_processor import extract_price_from_image
from sniper_logics import apply_sniper_logics

def analyze_image_and_generate_signal(image_path):
    """
    Process an image, extract price, apply sniper logic, and return signal data.
    Returns: signal_type (str), entry (float), tp (float), sl (float)
    """
    try:
        # Step 1: Extract the price using OCR
        price = extract_price_from_image(image_path)
        print(f"[Signal Engine] Extracted price: {price}")

        # Step 2: Apply sniper logic to determine signal
        signal, entry, tp, sl = apply_sniper_logics(price)
        print(f"[Signal Engine] Signal: {signal}, Entry: {entry}, TP: {tp}, SL: {sl}")

        return signal, entry, tp, sl

    except Exception as e:
        print(f"[Signal Engine] Error: {e}")
        return "ERROR", 0.0, 0.0, 0.0
