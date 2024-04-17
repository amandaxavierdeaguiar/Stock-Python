import flet as ft
from Views.Product.ListProduct import table_data

# x = 'coluna'
# y = 'linha'
def name_table():
    for item in table_data:
        return item['name']

def quantily_table():
    for item in table_data:
        return item['quantity']



def main(page: ft.Page):
    page.title = 'Gráficos'

    product_names = [item['name'] for item in table_data]
    product_quantity = [item['quantity'] for item in table_data]
    min_quantity = min(product_quantity)
    max_quantity = 5000 # max([item['quantity'] for item in table_data]) + 300
    table_data_sorted = sorted(table_data, key=lambda x: x['quantity'])
    # Ordenar a tabela pela quantidade

    # Pegar o nome da lista sortida


    # ft.LineChartDataPoint(name_table(), quantily_table())
    # ft.LineChartDataPoint(product_quantity.index(quantity), quantity) for quantity in product_quantity

    data_1 = [
        ft.LineChartData(
            data_points=[ft.LineChartDataPoint(i, quantity) for i, quantity in enumerate(product_quantity)],
            color = ft.colors.with_opacity(0.5, ft.colors.BLUE),
            below_line_bgcolor = ft.colors.with_opacity(0.1, ft.colors.BLUE),
            stroke_width = 4,
            curved = True,
            stroke_cap_round = True,
        )
    ]

    chart = ft.LineChart(
        data_series=data_1,
        border=ft.border.all(3, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)),
        left_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=value,
                    label=ft.Text(value=value, size=14, weight=ft.FontWeight.BOLD),
                ) for value in range(len(table_data))
            ],
            labels_size=50,
        ),

        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=i,
                    label=ft.Text((table_data[i]['name']), size=9, weight=ft.FontWeight.BOLD),
                ) for i in range(len(table_data))

            ],
            labels_size=20,
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        min_y=min_quantity,
        max_y=max_quantity,
        min_x=0,
        max_x=len(table_data),
        # animate=5000,
        expand=True,
    )

    def toggle_data(e):
        chart.update()

    page.add(chart)

ft.app(main)