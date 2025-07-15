from utils.ocr import extract_price_from_image
from utils.sniper_logic import detect_signals
from utils.annotate import annotate_chart

def analyze_chart(image_path):
    current_price = extract_price_from_image(image_path)
    signal, reasoning, tp, sl = detect_signals(image_path, current_price)
    result_text = f"📸 **Ghost X99 Signal**\n\n🔹 Signal: {signal}\n🔹 Price: {current_price}\n📈 TP: {tp}\n📉 SL: {sl}\n\n🧠 Reason: {reasoning}"
    marked_image_path = annotate_chart(image_path, signal, current_price, tp, sl)
    return result_text, marked_image_path
