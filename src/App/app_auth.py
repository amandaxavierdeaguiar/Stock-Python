import flet as ft
from flet import Text, Column, UserControl, icons, Control, IconButton, colors

from flet_core import Container

from App.features.app_auth_login import AuthLogin
from App.features.app_auth_registration import AuthRegister
from Views.User.ListUser import table_data as db_user


class AppAuth(UserControl):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.auth_login = AuthLogin(self.page)
        self.auth_register = AuthRegister(self.page)
        self.default_page = 0

        pages = [
            (
                self.auth_login.button_register,
                self.auth_login.get_login()
            ),
            (
                self.auth_login.button_register,
                self.auth_register.create_register()
            ),
        ]

        self.navigation_items = [navigation_item for navigation_item, _ in pages]

        page_contents = [page_content for _, page_content in pages]
        self.content_area = Column(controls=page_contents, expand=True)

        self._active_view: Control = Column(controls=[
            Text("")
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        self.set_content()
        self._change_displayed_page(self.default_page)

    def select_page(self, page_number):
        self.default_page = page_number
        self._change_displayed_page(page_number)

    def _change_displayed_page(self, page_number):
        for i, content_page in enumerate(self.content_area.controls):
            # update selected page
            content_page.visible = page_number == i

    def set_content(self, panel_=None):
        self.controls = [self.active_view,
                         self.content_area]
        return self.controls

    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.update()


if __name__ == '__main__':
    ft.app(target=AppAuth, assets_dir="../assets")
