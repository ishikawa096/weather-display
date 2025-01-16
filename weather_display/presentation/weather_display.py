from infrastructure.inky import display_image
from usecase.generate_weather_image import generate_weather_image


def weather_display():
    image = generate_weather_image()

    display_image(image)
