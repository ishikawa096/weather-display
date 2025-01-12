
# サンプルのweather_data
from datetime import datetime


weather_data = {
    'lat': 35.5297,
    'lon': 139.697,
    'timezone': 'Asia/Tokyo',
    'timezone_offset': 32400,
    'current': {
        'dt': 1736694725,
        'sunrise': 1736718623,
        'sunset': 1736754524,
        'temp': 279.69,
        'feels_like': 276.58,
        'pressure': 1013,
        'humidity': 71,
        'dew_point': 274.82,
        'uvi': 0,
        'clouds': 75,
        'visibility': 10000,
        'wind_speed': 4.63,
        'wind_deg': 330,
        'weather': [
            {
                'id': 803,
                'main': 'Clouds',
                'description': 'broken clouds',
                'icon': '04n'
            }
        ],
        'hourly': [{'dt': 1736704800,
                    'temp': 5.44, 'feels_like': 2.18, 'pressure': 1013, 'humidity': 64, 'dew_point': -0.72, 'uvi': 0, 'clouds': 19, 'visibility': 10000, 'wind_speed': 4.4, 'wind_deg': 342, 'wind_gust': 6.97,
                    'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}],
                    'pop': 0},
                   {'dt': 1736708400, 'temp': 5.01, 'feels_like': 1.52, 'pressure': 1013, 'humidity': 70, 'dew_point': 0, 'uvi': 0, 'clouds': 0, 'visibility': 10000,
                       'wind_speed': 4.66, 'wind_deg': 338, 'wind_gust': 7.27,
                       'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}],
                    'pop': 0}
                   ]

    }
}

weathers = {}


def format_weather_text(weather_data):
    print("format_weather_text")
    print(weather_data)
    formatted_text = ""
    try:
        currentDate = datetime.fromtimestamp(
            weather_data['current']['dt'] + weather_data['timezone_offset'])
        current = weather_data['current']
        currentWeather = current['weather'][0]

        hourly = [x for x in weather_data['hourly']
                  if current['dt'] < x['dt'] < current['dt'] + 24 * 60 * 60]

        hourlyPop = [x['pop'] for x in hourly]
        hourlyPop_str = '\n '.join([','.join(map(str, hourlyPop[i:i + 12]))
                                    # データをフォーマット
                                    for i in range(0, len(hourlyPop), 12)])

        hourlyMaxTemp = round(max([x['temp'] for x in hourly]))
        hourlyMinTemp = round(min([x['temp'] for x in hourly]))

        formatted_text = (
            f"{currentDate.strftime(
                '%m/%d %H:%M')} 》 {round(current['temp'])}℃ {currentWeather['main']} {hourlyMaxTemp}℃/{hourlyMinTemp}℃\n"
            f"☂{hourlyPop_str}\n"
        )
    except Exception as e:
        print(e)
        formatted_text = "Error: Something went wrong ☹"

    return formatted_text


# フォーマットした天気情報を表示
formatted_text = format_weather_text(weather_data)
print(formatted_text)
