import os
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()


def get_font(size):
    return ImageFont.truetype(os.getenv('FONT_PATH'), size)


def draw_contents_to_image(image_url, weather_data, sensor_data, pop_graph, color):
    # 画像を取得
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(image)

    # 画像に文字を追加
    draw.text((10, 10), weather_data['description'],
              font=get_font(20), fill=color)
    draw.text((270, 10), weather_data['time'], font=get_font(20), fill=color)
    draw.text((520, 10), weather_data['date'], font=get_font(20), fill=color)

    # センサーデータを画像に追加
    draw.text((200, 70), str(
        sensor_data['co2']), font=get_font(60), fill=color)
    draw.text((400, 110), 'ppm', font=get_font(16), fill=color)  # ppm

    draw.text((100, 140), str(sensor_data['temperature']),
              font=get_font(40), fill=color)
    draw.text((100, 190), '℃', font=get_font(16), fill=color)  # ℃

    draw.text((400, 140), str(sensor_data['humidity']),
              font=get_font(40), fill=color)
    draw.text((400, 190), '%rh', font=get_font(16), fill=color)  # %rh

    # 天気情報を画像に追加
    draw.text((70, 260), str(
        weather_data['temp']), font=get_font(35), fill=color)
    draw.text((70, 300), '℃', font=get_font(16), fill=color)  # ℃

    draw.text((50, 350), f"↑{weather_data['maxTemp']}",
              font=get_font(30), fill=color)
    draw.text((50, 380), f"↓{weather_data['minTemp']}",
              font=get_font(30), fill=color)
    draw.text((145, 370), '℃', font=get_font(16), fill=color)  # ℃

    image.paste(pop_graph, (220, 250), mask=pop_graph)
    draw.text((200, 380), '☂', font=get_font(30), fill=color)

    return image
