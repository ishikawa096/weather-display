# https: // github.com/pimoroni/inky/blob/v2.0.0/examples/7color/image.py
import os

from dotenv import load_dotenv
from add_text_to_image import add_text_to_image
from format_weather_text import format_weather_text
from get_random_image_url import get_random_image_url
from get_sensor_data import get_sensor_data
from get_weather import get_weather
from PIL import Image, ImageDraw, ImageFont

from inky.auto import auto

# .envファイルから環境変数を読み込む
load_dotenv()


saturation = 0.5


def display_error_message(inky, message):
    # エラーメッセージを含む画像を生成
    img = Image.new("P", (inky.WIDTH, inky.HEIGHT), color=inky.WHITE)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(os.getenv('FONT_PATH'), size=20)
    text_position = (10, 10)  # 文字の位置を指定
    draw.text(text_position, message, font=font, fill=inky.BLACK)

    # 画像をInkyに表示
    inky.set_image(img, saturation=saturation)
    inky.show()


inky = auto(ask_user=True, verbose=True)

weather_data = get_weather()
text = format_weather_text(weather_data)

sensor_data = get_sensor_data()
# sensor_data = {
#     "co2": 500,
#     "temperature": 20,
#     "humidity": 25
# }

image_url = get_random_image_url()

if not image_url:
    display_error_message(inky, "Error: image_url is None")
    exit()

image = add_text_to_image(image_url, text, sensor_data)

# image.save("image.png")

inky.set_image(image, saturation=saturation)
inky.show()
