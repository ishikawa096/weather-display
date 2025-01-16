import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz

# .envファイルから環境変数を読み込む
load_dotenv()

def get_weather():
    # OpenWeatherMap API情報を環境変数から取得
    base_url = os.getenv('OPENWEATHERMAP_BASE_URL')
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')

    # 緯度と経度を環境変数から取得
    lat = os.getenv('LAT')
    lon = os.getenv('LON')

    # APIエンドポイント
    url = f"{base_url}?lat={lat}&lon={lon}&units=metric&exclude=minutely,daily,alerts&appid={api_key}"

    # APIリクエストを送信
    response = requests.get(url)

    # レスポンスを表示
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: {response.status_code}")

def format_weather_text(weather_data):
    try:
        tz = pytz.timezone('Asia/Tokyo')
        currentDate = datetime.fromtimestamp(
            weather_data['current']['dt'], tz=tz)
        current = weather_data['current']
        currentWeather = current['weather'][0]

        # 今後12時間分の天気を取得
        hourly = [x for x in weather_data['hourly']
                  if current['dt'] < x['dt'] < current['dt'] + 12 * 60 * 60]

        hourlyPop = [x['pop'] for x in hourly]
        hourlyMaxTemp = round(max([x['temp'] for x in hourly]), 1)
        hourlyMinTemp = round(min([x['temp'] for x in hourly]), 1)

        weather_text = {
            'date': currentDate.strftime('%m/%d'),
            'time': currentDate.strftime('%H:%M'),
            'temp': round(current['temp'], 1),
            'description': currentWeather['description'],
            'maxTemp': hourlyMaxTemp,
            'minTemp': hourlyMinTemp,
            'pop': hourlyPop
        }
        return weather_text
    except Exception as e:
        print(e)
    return "Error: Something went wrong ☹"
