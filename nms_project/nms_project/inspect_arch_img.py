import pymupdf
from PIL import Image

img_path = "C:/Users/sameeha/.gemini/antigravity/brain/f5bcc397-1c93-4dea-a554-e17384fffa82/.user_uploaded/media_1791295323651.png"
with Image.open(img_path) as im:
    print(f"Image dimensions: {im.size[0]} x {im.size[1]}, aspect ratio: {im.size[0]/im.size[1]:.3f}")
