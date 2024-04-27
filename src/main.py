import flet
import flet as ft
from flet import Container, padding, margin

from app.app_window import AppWindow
from shared.Base.SharedControls import SharedControls


class App(SharedControls):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.app_view = Container(
            expand=True,
            expand_loose=True,
            padding=padding.all(0),
            margin=margin.all(0),
            alignment=ft.alignment.center,
            content=AppWindow(self.page),
        )
        self.page.add(self.app_view)
        self.page.update()


def main(page: ft.Page):
    page.title = "Stock Management"
    page.window_min_width = 600
    page.window_min_height = 400
    page.window_width = 856
    page.window_height = 645
    page.padding = padding.all(0)
    page.margin = margin.all(0)
    page.bgcolor = ft.colors.GREY_200

    app = App(page)
    page.add(app)


if __name__ == "__main__":
    ft.app(target=main, view=flet.FLET_APP_WEB, assets_dir="./assets")
