import requests
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()


def get_weather():
    # OpenWeatherMap APIキーを環境変数から取得
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')

    # 東経139度41分49秒、北緯35度31分47秒を度に変換
    lat = 35.5297
    lon = 139.6970

    # APIエンドポイント
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={
        lon}&units=metric&exclude=minutely,daily,alerts&appid={api_key}"

    # APIリクエストを送信
    response = requests.get(url)

    # レスポンスを表示
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: {response.status_code}")
