import cv2
from PIL import Image
import os

def overlay_fashion_item(image_path, category, item_filename):
    bg = cv2.imread(image_path)
    h, w = bg.shape[:2]

    # Load the fashion item
    item_path = f"app/static/{category}/{item_filename}"
    item_img = Image.open(item_path).convert("RGBA")

    if category == "shoes":
        item_img = item_img.resize((int(w * 0.4), int(h * 0.2)))
        x, y = int(w * 0.3), int(h * 0.7)
    elif category == "jewelry":
        item_img = item_img.resize((int(w * 0.2), int(h * 0.1)))
        x, y = int(w * 0.4), int(h * 0.25)
    elif category == "clothes":
        item_img = item_img.resize((int(w * 0.6), int(h * 0.5)))
        x, y = int(w * 0.2), int(h * 0.25)
    elif category == "accessories":
        item_img = item_img.resize((int(w * 0.3), int(h * 0.15)))
        x, y = int(w * 0.35), int(h * 0.2)

    bg_pil = Image.fromarray(cv2.cvtColor(bg, cv2.COLOR_BGR2RGB)).convert("RGBA")
    bg_pil.paste(item_img, (x, y), item_img)

    output_path = image_path.replace(".jpg", "_tryon.png").replace(".png", "_tryon.png")
    bg_pil.save(output_path)
    return output_path
