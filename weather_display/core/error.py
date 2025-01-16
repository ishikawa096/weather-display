import os
from PIL import Image, ImageDraw, ImageFont


def generate_error_image(message):
    img = Image.new("P", (400, 300), color=255)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(os.getenv('FONT_PATH'), size=20)
    text_position = (10, 10)  # 文字の位置を指定
    draw.text(text_position, message, font=font, fill=0)
    return img
