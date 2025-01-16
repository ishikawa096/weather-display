# https://github.com/adafruit/Adafruit_CircuitPython_SCD4X#usage-example
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

if os.getenv('MOCK_MODE') != 'True':
    import board
    import adafruit_scd4x


def sensor():
    if os.getenv('MOCK_MODE') == 'True':
        return None

    i2c = board.I2C()
    scd4x = adafruit_scd4x.SCD4X(i2c)

    return scd4x


def get_sensor_data():
    if os.getenv('MOCK_MODE') == 'True':
        # モックモードの場合は固定のセンサーデータを返す
        return {
            "co2": 500,
            "temperature": 20.9,
            "humidity": 25.3
        }
    sensor = sensor()
    sensor.measure_single_shot()

    if sensor.data_ready:
        return {
            "co2": sensor.CO2,
            "temperature": round(sensor.temperature, 1),
            "humidity": round(sensor.relative_humidity, 1)
        }
