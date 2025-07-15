import pytesseract
from PIL import Image

def extract_price_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    # Extract price (custom logic here)
    lines = text.split('\n')
    for line in lines:
        if any(char.isdigit() for char in line):
            try:
                return float(line.replace(',', '').strip())
            except:
                continue
    return 0.0
