import cv2
from image_processor import preprocess_image
from sniper_logics import apply_all_sniper_logics

def is_valid_image(path):
    try:
        img = cv2.imread(path)
        return img is not None
    except:
        return False

def process_image(image_path):
    if not is_valid_image(image_path):
        print("❌ Invalid image file.")
        return None

    img = cv2.imread(image_path)
    if img is None:
        print("❌ Failed to load image.")
        return None

    processed_img = preprocess_image(img)
    signal = apply_all_sniper_logics(processed_img)

    return signal
