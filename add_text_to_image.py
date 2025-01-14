import os
from dotenv import load_dotenv
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from select_random_color import select_random_color

# .envファイルから環境変数を読み込む
load_dotenv()

# Example of sensor_data
# sensor_data = {
#     "co2": 500,
#     "temperature": 20,
#     "humidity": 25
# }


def get_font(size):
    return ImageFont.truetype(os.getenv('FONT_PATH'), size)


def add_text_to_image(image_url, text, sensor_data):
    # 画像を取得
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(image)

    # フォントファイルとサイズを指定
    font = get_font(20)

    # 画像に文字を追加
    color = select_random_color()
    text_position = (10, 350)  # 文字の位置を指定
    draw.text(text_position, text, font=font, fill=color)

    # センサーデータを画像に追加
    draw.text((200, 60), str(
        sensor_data['co2']), font=get_font(60), fill=color)
    draw.text((400, 100), 'ppm', font=get_font(16), fill=color)  # ppm

    draw.text((100, 130), str(sensor_data['temperature']),
              font=get_font(40), fill=color)
    draw.text((100, 180), '℃', font=get_font(16), fill=color)  # ℃

    draw.text((400, 130), str(sensor_data['humidity']),
              font=get_font(40), fill=color)
    draw.text((400, 180), '%rh', font=get_font(16), fill=color)  # %rh

    return image
