import flet as ft

from shared.base.SharedControls import SharedControls


class Charts(SharedControls):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def create_chart(cls, data):
        data_1 = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(i, quantity)
                    for i, quantity in enumerate(data["values"])
                ],
                color=ft.colors.with_opacity(0.5, ft.colors.BLUE_900),
                below_line_bgcolor=ft.colors.with_opacity(0.2, ft.colors.BLUE),
                stroke_width=4,
                curved=True,
                stroke_cap_round=True,
            ),
        ]

        chart = ft.LineChart(
            data_series=data_1,
            border=ft.border.all(3, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)),
            left_axis=ft.ChartAxis(
                title=ft.Text(
                    value=data['name'],
                    size=14,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.BLUE,
                ),
                labels=cls.create_y(data),
                labels_interval=20,
                labels_size=30,
                title_size=30,
            ),
            bottom_axis=ft.ChartAxis(
                title=ft.Text(
                    "Datas", size=14, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE
                ),
                labels=cls.create_x(data),
                show_labels=True,
                labels_size=27,
                title_size=30,
                labels_interval=data["length"] // 6,
            ),
            right_axis=ft.ChartAxis(
                labels=[ft.ChartAxisLabel(value=0, label=ft.Text())],
                labels_size=30,
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
            min_y=data["min"],
            max_y=data["max"],
            min_x=0,
            max_x=data["length"],
            expand=True,
        )
        return chart

    @classmethod
    def create_y(cls, data):
        y = []
        for i, value in enumerate(data["y"]):
            y.append(
                ft.ChartAxisLabel(
                    value=value,
                    label=ft.Text(value=value, size=10, weight=ft.FontWeight.BOLD),
                )
            )
        return y

    @classmethod
    def create_x(cls, data):
        x = []
        for i, value in enumerate(data["x"]):
            date = f'{value.hour}:{value.minute}\n{value.year}-{value.month}-{value.day}'
            x.append(
                ft.ChartAxisLabel(
                    value=i,
                    label=ft.Text(value=date, size=10, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                )
            )
        return x
