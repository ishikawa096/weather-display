from PIL import Image, ImageDraw
from core.image import get_font


def generate_error_image(message):
    img = Image.new("P", (400, 300), color=255)
    draw = ImageDraw.Draw(img)
    font = get_font(20)
    text_position = (10, 10)  # 文字の位置を指定
    draw.text(text_position, message, font=font, fill=0)
    return img
