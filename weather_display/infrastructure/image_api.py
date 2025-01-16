import requests
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()


def get_random_image_url(query):
    # Unsplash APIのアクセストークン
    access_key = os.getenv('UNSPLASH_ACCESS_KEY')

    parameters = {
        # 'query': 'los-angeles-beach',
        'query': query.replace(' ', '-') + '-landscape',
        'orientation': 'landscape',
    }

    # ランダムな写真を取得するためのエンドポイント
    url = os.getenv('UNSPLASH_BASE_URL') + '/photos/random' + \
        '?query=' + parameters['query'] + \
        '&orientation=' + parameters['orientation']

    # リクエストヘッダーにアクセストークンを追加
    headers = {
        'Authorization': f'Client-ID {access_key}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        image_url = data['urls']['regular']

        #  サイズを変更
        image_url = image_url.replace(
            'w=1080', 'w=600&h=448'
        ).replace(
            'fit=max', 'fit=crop'
        )

        return image_url
    else:
        print(f"Error: {response.status_code}")
        return None
