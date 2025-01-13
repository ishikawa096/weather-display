# https: // github.com/pimoroni/inky/blob/v2.0.0/examples/7color/image.py
from add_text_to_image import add_text_to_image
from format_weather_text import format_weather_text
from get_random_image_url import get_random_image_url
from get_weather import get_weather
from inky.auto import auto

inky = auto(ask_user=True, verbose=True)

saturation = 0.5

image_url = get_random_image_url()

if not image_url:
    print("Error: image_url is None")
    exit()

weather_data = get_weather()
text = format_weather_text(weather_data)
image = add_text_to_image(
    # image_url, "☂☁☀☃★☽\n(12/30 15:00)☀18℃_30℃/13℃_18:00☂20%\n20℃_25%rh_500ppm")
    image_url, text)

try:
    inky.set_image(image, saturation=saturation)
except TypeError:
    inky.set_image(image)

inky.show()
