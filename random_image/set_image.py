# https: // github.com/pimoroni/inky/blob/v2.0.0/examples/7color/image.py
from io import BytesIO
from get_random_image_url import get_random_image_url
from PIL import Image
import requests

from inky.auto import auto

inky = auto(ask_user=True, verbose=True)

saturation = 0.5

imageUrl = get_random_image_url()
imageResponse = requests.get(imageUrl)
image = Image.open(BytesIO(imageResponse.content))

try:
    inky.set_image(image, saturation=saturation)
except TypeError:
    inky.set_image(image)

inky.show()
