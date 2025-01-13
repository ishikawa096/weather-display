import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from select_random_color import select_random_color


def add_text_to_image(image_url, text):
    # 画像を取得
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(image)

    # フォントファイルとサイズを指定
    font_path = "./assets/fonts/Better VCR 9.0.1.ttf"  # フォントファイルのパス
    font_size = 20  # フォントサイズ
    font = ImageFont.truetype(font_path, font_size)

    # 画像に文字を追加
    color = select_random_color()
    text_position = (10, 350)  # 文字の位置を指定
    draw.text(text_position, text, font=font, fill=color)

    return image
