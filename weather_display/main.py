from presentation.weather_display import weather_display
import sys
import os

# プロジェクトのルートディレクトリをモジュール検索パスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == "__main__":
    weather_display()
