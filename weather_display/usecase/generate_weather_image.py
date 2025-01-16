from core.error import generate_error_image
from core.image import draw_contents_to_image
from core.weather import parse_weather_response
from core.pop_graph import generate_pop_graph
from infrastructure.image_api import get_random_image_url
from infrastructure.sensor import get_sensor_data
from core.color import select_random_color
from infrastructure.weather_api import get_weather


def generate_weather_image():
    # 天気予報を取得
    weather_response = get_weather()
    weather_data = parse_weather_response(weather_response)
    color = select_random_color()
    # 降水確率のグラフを生成
    pop_graph = generate_pop_graph(weather_data['pop'], color)

    # CO2センサーデータを取得
    sensor_data = get_sensor_data()

    # 背景画像を取得
    image_url = get_random_image_url(weather_data['description'])

    if not image_url:
        return generate_error_image("Image not found")

    # 背景画像に情報を描画
    image = draw_contents_to_image(
        image_url, weather_data, sensor_data, pop_graph, color
    )

    return image
