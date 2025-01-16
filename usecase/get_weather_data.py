import os
from dotenv import load_dotenv
from domain.weather import get_weather, format_weather_text

# .envファイルから環境変数を読み込む
load_dotenv()

def get_weather_data():
    weather_data = get_weather()
    formatted_weather_data = format_weather_text(weather_data)
    return formatted_weather_data
