import os
from dotenv import load_dotenv
from domain.random_image import get_random_image_url
from usecase.display_error_message import display_error_message

# .envファイルから環境変数を読み込む
load_dotenv()

def get_image_data(formatted_weather_data, inky):
    image_url = get_random_image_url(formatted_weather_data['description'])

    if not image_url:
        display_error_message(inky, "Error: image_url is None")
        exit()

    return image_url
