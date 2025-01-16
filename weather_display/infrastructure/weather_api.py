import os
import requests


def get_weather():
    # OpenWeatherMap API情報を環境変数から取得
    base_url = os.getenv('OPENWEATHERMAP_BASE_URL')
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')

    # 緯度と経度を環境変数から取得
    lat = os.getenv('LAT')
    lon = os.getenv('LON')

    # APIエンドポイント
    url = f"{base_url}?lat={lat}&lon={
        lon}&units=metric&exclude=minutely,daily,alerts&appid={api_key}"

    response = requests.get(url)

    # レスポンスを表示
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: {response.status_code}")
        return None
