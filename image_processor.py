from PIL import Image
import pytesseract

def extract_price_from_image(image_path):
    """
    Extracts visible text (like price zones, asset names, levels) from the chart screenshot
    using OCR instead of OpenCV.
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)

        # Clean the output a bit
        cleaned = text.strip().replace('\n', ' ').replace('  ', ' ')
        return cleaned

    except Exception as e:
        return f"[Error extracting image text] {e}"
