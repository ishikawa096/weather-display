import io
import matplotlib.pyplot as plt

from select_random_color import select_random_color
from PIL import Image


def generate_pop_graph(hourlyPop, color):
    # hourlyPop = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80]
    # グラフを作成
    plt.figure(figsize=(4, 2))
    plt.bar(range(len(hourlyPop)), hourlyPop, color=color)

    # グラフのタイトルとラベルを設定
    plt.title('')
    plt.xlabel('')
    plt.ylabel('')

    plt.xticks([])  # x軸の目盛りを非表示
    plt.yticks([])  # y軸の目盛りを非表示

    # 枠線を非表示
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_color(color)
    plt.gca().spines['bottom'].set_linewidth(2)
    plt.gca().spines['left'].set_color(color)
    plt.gca().spines['left'].set_linewidth(2)

    # グラフをByteIOに保存
    pop_graph = io.BytesIO()
    plt.savefig(pop_graph, format='png', bbox_inches='tight', transparent=True)
    pop_graph.seek(0)

    # PILで画像として読み込む (RGBAモード)
    graph_image = Image.open(pop_graph).convert("RGBA")

    return graph_image
