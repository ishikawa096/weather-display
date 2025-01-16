import os
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

def display_error_message(inky, message):
    if os.getenv('MOCK_MODE') == 'True':
        print("Error: " + message)
        return

    # エラーメッセージを含む画像を生成
    img = Image.new("P", (inky.WIDTH, inky.HEIGHT), color=inky.WHITE)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(os.getenv('FONT_PATH'), size=20)
    text_position = (10, 10)  # 文字の位置を指定
    draw.text(text_position, message, font=font, fill=inky.BLACK)

    # 画像をInkyに表示
    inky.set_image(img, saturation=0.5)
    inky.show()
