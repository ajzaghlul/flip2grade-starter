from PIL import Image
import numpy as np

def analyze_card_image(image_file):
    try:
        img = Image.open(image_file)
        width, height = img.size
        centering = "50/50" if abs(width - height) < 10 else "Slightly off"
        grade_estimate = "9" if centering == "50/50" else "8"
        return grade_estimate, centering
    except Exception:
        return "Unknown", "Could not analyze"
