import os


def get_inky():
    if os.getenv('MOCK_MODE') == 'True':
        return None

    from inky.auto import auto
    return auto(ask_user=True, verbose=True)


def display_image(image):
    if os.getenv('MOCK_MODE') == 'True':
        image.save("image.png")
        return

    inky = get_inky()
    inky.set_image(image)
    inky.show()
