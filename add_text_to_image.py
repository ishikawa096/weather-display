import os
from dotenv import load_dotenv
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from select_random_color import select_random_color

# .envファイルから環境変数を読み込む
load_dotenv()


def add_text_to_image(image_url, text):
    # 画像を取得
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(image)

    # フォントファイルとサイズを指定
    font = ImageFont.truetype(os.getenv('FONT_PATH'), size=20)

    # 画像に文字を追加
    color = select_random_color()
    text_position = (10, 350)  # 文字の位置を指定
    draw.text(text_position, text, font=font, fill=color)

    return image
