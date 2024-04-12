import flet as ft
from flet import Row, Container, Column, UserControl

from App.app_auth import AppAuth
from App.features.app_header import AppHeader
from App.app_layout import AppLayout
from Models.UserAuthentication import UserAuthentication
from Views.Product.ListProduct import table_data as db_product
from Views.Supplier.ListSupplier import table_data as db_supplier
from Views.User.ListUser import table_data as db_user

list_tables = {
    0: db_product,
    1: db_supplier,
    2: db_user,
}


class AppWindow(UserControl):
    """A desktop app layout with a menu on the left."""

    def __init__(self, title, page, *args, window_size=(800, 600), **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.page.on_logout = self.change_page
        self.page.on_login = self.change_page
        self.user_Auth = UserAuthentication()
        self.expand = True

        self.page.on_resize = self.handle_resize

        self._was_portrait = self.is_portrait()
        self._panel_visible = self.is_landscape()

        self.appbar = AppHeader(page, user=self.user_Auth, var_on_click=self.change_page)
        self.page.appbar = self.appbar.app_bar

        self.app_page = AppLayout(page=self.page)
        self.app_auth = AppAuth(user=self.user_Auth, page=self.page)
        self.content_column = Column(controls=self.app_auth.content_area.controls,
                                     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                     alignment=ft.MainAxisAlignment.CENTER)
        self.content = Container(
            expand=True,
            content=self.content_column
        )
        # self.change_page()

        self.window_size = window_size
        self.page.window_width, self.page.window_height = self.window_size
        self.page.add(self.content)

    def change_page(self, event=None):
        if self.user_Auth.is_login and event is None:
            self.content_column.controls.clean()
            self.content_column.controls = self.app_page.set_content(self._panel_visible).copy()
            self.appbar.change_btn_logout()
            self.page.appbar.update()
            self.content.update()
        elif not self.user_Auth.is_login and event is None:
            # self.controls.clear()
            self.content_column.controls = self.app_auth.content_area.controls
            self.content.update()
        elif event is not None:
            if self.user_Auth.is_login and event.name == 'logout':
                self.content_column.controls.clear()
                self.content_column.controls = self.app_page.set_content(self._panel_visible)
                self.appbar.change_btn_logout()
                self.page.update()
                self.page.appbar.update()
            elif event.name == 'click' and event.control.data == 'logout' or event.control.text == 'Logout':
                self.content_column.controls.clear()
                self.content_column.controls = self.app_auth.content_area.controls
                self.appbar.change_btn_logout()
                self.page.appbar.update()
                self.update()
                self.page.login()

    def is_portrait(self) -> bool:
        # Return true if window/display is narrow
        # return self.page.window_height >= self.page.window_width
        return self.page.height >= self.page.width

    def is_landscape(self) -> bool:
        # Return true if window/display is wide
        return self.page.width > self.page.height

    def handle_resize(self, e):
        pass
