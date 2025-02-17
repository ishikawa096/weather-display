from datetime import datetime
import pytz


def parse_weather_response(weather_data):
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

        return {
            'date': currentDate.strftime('%m/%d'),
            'time': currentDate.strftime('%H:%M'),
            'temp': round(current['temp'], 1),
            'description': currentWeather['description'],
            'maxTemp': hourlyMaxTemp,
            'minTemp': hourlyMinTemp,
            'pop': hourlyPop
        }
    except Exception as e:
        print(e)
    return None
