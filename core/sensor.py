# https://github.com/adafruit/Adafruit_CircuitPython_SCD4X#usage-example
import os
if os.getenv('MOCK_MODE') != 'True':
    import board
    import adafruit_scd4x
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()


def get_sensor_data():
    if os.getenv('MOCK_MODE') == 'True':
        return {
            "co2": 500,
            "temperature": 20.9,
            "humidity": 25.3
        }

    i2c = board.I2C()
    scd4x = adafruit_scd4x.SCD4X(i2c)

    scd4x.measure_single_shot()

    if scd4x.data_ready:
        # print("co2: %d PPM, temperature: %0.2f ℃, humidity: %0.2f %%" %
        #       (scd4x.CO2, scd4x.temperature, scd4x.relative_humidity))
        return {
            "co2": scd4x.CO2,
            "temperature": round(scd4x.temperature, 1),
            "humidity": round(scd4x.relative_humidity, 1)
        }
