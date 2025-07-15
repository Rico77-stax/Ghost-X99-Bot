import cv2 import pytesseract from PIL import Image import numpy as np

def preprocess_image(image_path): image = cv2.imread(image_path) if image is None: raise ValueError(f"Failed to load image: {image_path}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
denoised = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(denoised, 150, 255, cv2.THRESH_BINARY_INV)
return image, thresh

def extract_price_from_image(image_path): _, thresh = preprocess_image(image_path) data = pytesseract.image_to_string(thresh, config='--psm 6')

lines = data.splitlines()
prices = []
for line in lines:
    line = line.strip().replace(',', '.')
    try:
        numbers = [float(word) for word in line.split() if word.replace('.', '', 1).isdigit()]
        prices.extend(numbers)
    except:
        continue
if not prices:
    raise ValueError("No price found in OCR result.")

return prices[-1]  # Assume last price near bottom is current

def annotate_image(image_path, signal, entry, tp, sl): image = cv2.imread(image_path) if image is None: raise ValueError(f"Cannot load image: {image_path}")

h, w, _ = image.shape

cv2.putText(image, f"Signal: {signal}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
cv2.putText(image, f"Entry: {entry}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(image, f"TP: {tp}", (10, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
cv2.putText(image, f"SL: {sl}", (10, 190), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

marked_path = image_path.replace(".png", "_marked.png").replace(".jpg", "_marked.jpg")
cv2.imwrite(marked_path, image)
return marked_path

