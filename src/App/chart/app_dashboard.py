from App.chart.chart1 import graphic
import flet as ft
from flet import UserControl
from flet.matplotlib_chart import MatplotlibChart
class AppDashborad(UserControl):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__()
        self.page = page
        self.app_dashboard = graphic(MatplotlibChart(expand=True))

        page.add(
            ft.Container(
                width=720,
                height=800,
                #padding=10,
                #border_radius=20,
                bgcolor="blue",
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Column(width=600, height=800,
                                          controls=[
                                              self.app_dashboard
                                          ],
                                          # spacing=20,
                                          alignment=ft.MainAxisAlignment.CENTER,
                                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                          ),
                            ],
                            alignment=ft.CrossAxisAlignment.CENTER,
                            # spacing=20,
                        ),
                    ],
                ),
            ),
        ),

        page.add()

ft.app(AppDashborad)