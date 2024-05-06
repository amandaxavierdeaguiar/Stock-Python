import flet as ft
from flet import (
    Container,
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    margin,
)

from shared.base.SharedControls import SharedControls


class AppHeader(SharedControls):
    """ """

    def __init__(self, page):
        super().__init__()
        self.page = page
        login_email = self.user.login
        self.appbar_items = [
            PopupMenuItem(text=login_email, data="login"),
            PopupMenuItem(),  # divider
            PopupMenuItem(
                text="Logout",
                data="logout",
                on_click=self.logout,
                disabled=False if self.user.is_login else True,
            ),
        ]
        self.appbar_logo = ft.Image(
            src="icons/logo-stock.png",
            width=30,
            height=30,
            fit=ft.ImageFit.CONTAIN,
            tooltip="Logo",
        )
        self.app_bar = self.get_app_bar()

    def change_btn_logout(self):
        self.appbar_items[0].text = self.user.login
        self.appbar_items[2].disabled = not self.appbar_items[2].disabled

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
                    padding=0,
                    content=PopupMenuButton(items=self.appbar_items),
                    margin=margin.only(left=50, right=25),
                ),
            ],
        )

    def logout(self, event):
        message = {"login": False}
        self.user.user_logout()
        self.page.pubsub.send_all(message)
