# signal_engine.py

import cv2
import numpy as np
import pytesseract
from utils import draw_markup, detect_candles, get_latest_price_zone, extract_text_data
from sniper_logics import apply_all_sniper_logics
from logic_utils import calculate_tp_sl, get_timeframe_from_filename

def analyze_chart_image(image_path):
    # Step 1: Load image and preprocess
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image could not be loaded.")

    # Step 2: Extract chart text using OCR
    ocr_text = extract_text_data(image)
    
    # Step 3: Detect candles and market structure from image
    candles = detect_candles(image)
    if not candles or len(candles) < 10:
        return None, None

    # Step 4: Get most recent price zone (last visible area)
    latest_price = get_latest_price_zone(candles)

    # Step 5: Detect timeframe (M15, M30, H1)
    timeframe = get_timeframe_from_filename(image_path)

    # Step 6: Apply full sniper logic system (36+ strategies)
    signal_data = apply_all_sniper_logics(candles, ocr_text, latest_price, timeframe)

    if not signal_data:
        return None, None

    # Step 7: Calculate TP & SL based on price action + fib + sniper system
    tp, sl = calculate_tp_sl(signal_data, candles)

    # Step 8: Draw markup (annotated image)
    annotated_image_path = draw_markup(image_path, signal_data, tp, sl)

    # Step 9: Prepare final output message
    signal_text = f"""
🔮 *Ghost X99 – Vortex Sniper Signal*

🕒 Timeframe: {timeframe}
📍 Entry: `{signal_data['entry']}`
🎯 TP: `{tp}`
🛑 SL: `{sl}`
📊 Type: *{signal_data['type']}*

🧠 Reason: {signal_data['reason']}

⚠️ Signal is based on screenshot's latest price action.
    """.strip()

    return signal_text, annotated_image_path
