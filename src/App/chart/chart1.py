import matplotlib
import matplotlib.pyplot as plt
from Views.Product.ListProduct import table_data
import flet as ft
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")

def graphic(page: ft.Page):
    fruits = list(set([item['name'] for item in table_data]))[:10]
    counts = list(set([item['quantity'] for item in table_data]))[:10]

    fig, ax = plt.subplots()
    ax.plot(fruits, counts, color='blue', linewidth=1.5, marker='o') #, alpha=0.3
    ax.grid()

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.spines['left'].set_color('grey')
    ax.spines['bottom'].set_color('grey')
    """ax.spines['top'].set_color('grey')
    ax.spines['right'].set_color('grey')"""

    plt.xticks(fontsize=8, rotation=90)
    fig.subplots_adjust(bottom=0.25)
    return MatplotlibChart(fig, expand=True)



