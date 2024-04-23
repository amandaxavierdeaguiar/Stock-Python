import flet as ft
from flet import (Container, UserControl, Text, AppBar, PopupMenuButton,
                  PopupMenuItem, colors, margin)

from shared.Base.SharedControls import SharedControls


class AppHeader(SharedControls):
    """

    """

    def __init__(self, page, var_on_click):
        super().__init__()
        self.page = page
        self.appbar_items = [
            PopupMenuItem(text="Login" if self.user.login is None else f'{self.user.login}', on_click=var_on_click, data='login'),
            PopupMenuItem(),  # divider
            PopupMenuItem(text="Logout", data='logout', on_click=self.logout,
                          disabled=False if self.user.is_login else True)
        ]
        self.appbar_logo = ft.Image(src="icons/logo-stock.png",
                                    width=30, height=30, fit=ft.ImageFit.CONTAIN, tooltip="Logo")
        self.app_bar = self.get_app_bar()

    def change_btn_logout(self):
        self.appbar_items[0] = self.user.login
        self.appbar_items[2].disabled = not self.appbar_items[2].disabled

    def get_app_bar(self):
        """

        :return: AppBar
        """
        return AppBar(
            leading=self.appbar_logo,
            leading_width=50,
            title=Text("stock Management", size=30, text_align=ft.TextAlign.CENTER),
            center_title=False,
            toolbar_height=65,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                Container(
                    padding=0,
                    content=PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=margin.only(left=50, right=25)
                ),
            ],
        )

    def logout(self, event):
        self.page.logout()
