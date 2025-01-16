import os
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests
from domain.image import draw_contents_to_image
from domain.weather import format_weather_text, get_weather
from domain.pop_graph import generate_pop_graph
from domain.random_image import get_random_image_url
from infrastructure.sensor import get_sensor_data
from domain.color import select_random_color
from usecase.display_error_message import display_error_message

# .envファイルから環境変数を読み込む
load_dotenv()

def draw_image(inky):
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
