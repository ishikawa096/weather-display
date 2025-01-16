import io
import matplotlib.pyplot as plt
from PIL import Image

def generate_pop_graph(hourlyPop, color):
    plt.figure(figsize=(4, 2))
    plt.bar(range(len(hourlyPop)), hourlyPop, color=color)

    plt.title('')
    plt.xlabel('')
    plt.ylabel('')

    plt.xticks([])  
    plt.yticks([])  

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_color(color)
    plt.gca().spines['bottom'].set_linewidth(2)
    plt.gca().spines['left'].set_color(color)
    plt.gca().spines['left'].set_linewidth(2)

    pop_graph = io.BytesIO()
    plt.savefig(pop_graph, format='png', bbox_inches='tight', transparent=True)
    pop_graph.seek(0)

    graph_image = Image.open(pop_graph).convert("RGBA")

    return graph_image
