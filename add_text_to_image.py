import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from format_weather_text import format_weather_text
from get_random_image_url import get_random_image_url
from get_weather import get_weather
from select_random_color import select_random_color


def add_text_to_image(image_url, text):
    # 画像を取得
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(image)

    # フォントファイルとサイズを指定
    font_path = "./assets/fonts/Better VCR 9.0.1.ttf"  # フォントファイルのパス
    font_size = 20  # フォントサイズ
    font = ImageFont.truetype(font_path, font_size)

    # 画像に文字を追加
    color = select_random_color()
    text_position = (10, 350)  # 文字の位置を指定
    draw.text(text_position, text, font=font, fill=color)

    # 画像を保存または表示
    image.show()  # 画像を表示
    image.save("output_image.png")  # 画像を保存


if __name__ == "__main__":
    image_url = get_random_image_url()
    weather_data = get_weather()
    text = format_weather_text(weather_data)
    if image_url:
        add_text_to_image(
            # image_url, "☂☁☀☃★☽\n(12/30 15:00)☀18℃_30℃/13℃_18:00☂20%\n20℃_25%rh_500ppm")
            image_url, text)
