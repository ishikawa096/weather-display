# https: // github.com/pimoroni/inky/blob/v2.0.0/examples/7color/image.py
import os

from dotenv import load_dotenv
from core.image import draw_contents_to_image
from core.weather import format_weather_text, get_weather
from core.pop_graph import generate_pop_graph
from core.random_image import get_random_image_url
from infrastructure.sensor import get_sensor_data
from PIL import Image, ImageDraw, ImageFont

from core.color import select_random_color

if os.getenv('MOCK_MODE') != 'True':
    from inky.auto import auto


def display_error_message(inky, message):
    if os.getenv('MOCK_MODE') == 'True':
        print("Error: " + message)
        return

    # エラーメッセージを含む画像を生成
    img = Image.new("P", (inky.WIDTH, inky.HEIGHT), color=inky.WHITE)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(os.getenv('FONT_PATH'), size=20)
    text_position = (10, 10)  # 文字の位置を指定
    draw.text(text_position, message, font=font, fill=inky.BLACK)

    # 画像をInkyに表示
    inky.set_image(img, saturation=saturation)
    inky.show()


# .envファイルから環境変数を読み込む
load_dotenv()

if os.getenv('MOCK_MODE') == 'True':
    inky = None
else:
    inky = auto(ask_user=True, verbose=True)

saturation = 0.5

weather_data = get_weather()
formatted_weather_data = format_weather_text(weather_data)
color = select_random_color()
pop_graph = generate_pop_graph(formatted_weather_data['pop'], color)

sensor_data = get_sensor_data()

image_url = get_random_image_url(formatted_weather_data['description'])

if not image_url:
    display_error_message(inky, "Error: image_url is None")
    exit()

image = draw_contents_to_image(
    image_url, formatted_weather_data, sensor_data, pop_graph, color)

if os.getenv('MOCK_MODE') == 'True':
    image.save("image.png")
    exit()

inky.set_image(image, saturation=saturation)
inky.show()
