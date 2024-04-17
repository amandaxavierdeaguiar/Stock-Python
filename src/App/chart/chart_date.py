import flet as ft
from datetime import datetime
from Views.Movements.ListMovements import movements

def main(page: ft.Page):
    page.title = 'Gráficos'

    quantity_movements = [item['quantity'] for item in movements]
    min_quantity = max([item['quantity'] for item in movements]) - 75
    max_quantity = max([item['quantity'] for item in movements])

    data_1 = [
        ft.LineChartData(
            data_points=[
                         ft.LineChartDataPoint(i, quantity) for i, quantity in enumerate(quantity_movements)
            ],
            color=ft.colors.with_opacity(0.5, ft.colors.BLUE_900),
            below_line_bgcolor=ft.colors.with_opacity(0.2, ft.colors.BLUE),
            stroke_width=4,
            curved=True,
            stroke_cap_round=True,
        )
    ]

    chart = ft.LineChart(
        data_series=data_1,
        border=ft.border.all(3, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)),
        left_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=quantity,
                    label=ft.Text(str(quantity), size=14, weight=ft.FontWeight.BOLD),
                ) for quantity in quantity_movements],
            labels_size=50,
        ),

        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=i,
                    label=ft.Text(movements[i]['date'], size=14, weight=ft.FontWeight.BOLD),
                ) for i in range(len(movements))],
            labels_size=20,
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        min_y=min_quantity,
        max_y=max_quantity,
        min_x=movements[0],
        max_x=len(movements)-1,
        # expand=True,
    )

    def toggle_data(e):
        chart.update()

    page.add(chart)

ft.app(main)