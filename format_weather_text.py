
# サンプルのweather_data
from datetime import datetime
import pytz


def format_weather_text(weather_data):
    try:
        tz = pytz.timezone('Asia/Tokyo')
        currentDate = datetime.fromtimestamp(
            weather_data['current']['dt'], tz=tz)
        current = weather_data['current']
        currentWeather = current['weather'][0]

        # 今後24時間分の天気を取得
        hourly = [x for x in weather_data['hourly']
                  if current['dt'] < x['dt'] < current['dt'] + 24 * 60 * 60]

        hourlyPop = [x['pop'] for x in hourly]
        hourlyPop_str = '\n '.join([','.join(map(str, hourlyPop[i:i + 12]))
                                    # データをフォーマット
                                    for i in range(0, len(hourlyPop), 12)])

        hourlyMaxTemp = round(max([x['temp'] for x in hourly]))
        hourlyMinTemp = round(min([x['temp'] for x in hourly]))

        formatted_text = (
            f"{currentDate.strftime('%m/%d %H:%M')} 》 {round(current['temp'])}℃ {currentWeather['description']} {hourlyMaxTemp}℃/{hourlyMinTemp}℃\n"
            f"☂{hourlyPop_str}\n"
        )
        return formatted_text
    except Exception as e:
        print(e)
    return "Error: Something went wrong ☹"
