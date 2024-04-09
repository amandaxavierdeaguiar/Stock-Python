import flet as ft
from flet import (Container, UserControl, Text, AppBar, PopupMenuButton, PopupMenuItem, colors, margin)


class AppHeader(UserControl):
    """

    """
    def __init__(self, page):
        super().__init__()
        self.appbar_items = [
            PopupMenuItem(text="Login"),
            PopupMenuItem(),  # divider
            PopupMenuItem(text="Settings")
        ]
        self.appbar_logo = ft.Image(src="icons/logo-stock.png",
                                    width=30, height=30, fit=ft.ImageFit.CONTAIN, tooltip="Logo")

    def get_app_bar(self):
        """

        :return: AppBar
        """
        return AppBar(
            leading=self.appbar_logo,
            leading_width=50,
            title=Text("Stock Management", size=30, text_align=ft.TextAlign.CENTER),
            center_title=False,
            toolbar_height=65,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=margin.only(left=50, right=25)
                ),
            ],
        )

