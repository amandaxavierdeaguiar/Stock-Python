import flet as ft
from flet import Row, Column, Control, Text, IconButton, icons, colors

from App.app_header import AppHeader
from App.app_layout import AppLayout
from Views.Product.ListProduct import table_data as db_product
from Views.Supplier.ListSupplier import table_data as db_supplier
from Views.User.ListUser import table_data as db_user

list_tables = {
    0: db_product,
    1: db_supplier,
    2: db_user,
}


class AppWindow(Row):
    """A desktop app layout with a menu on the left."""

    def __init__(self, title, page, *args, window_size=(800, 600), **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page

        self.expand = True

        self.page.on_resize = self.handle_resize

        self._was_portrait = self.is_portrait()
        self._panel_visible = self.is_landscape()

        self.appbar = AppHeader(page)
        self.page.appbar = self.appbar.get_app_bar()

        self.app_page = AppLayout(page=self.page)
        self.controls = self.app_page.set_content(self._panel_visible)

        self.window_size = window_size
        self.page.window_width, self.page.window_height = self.window_size

    def is_portrait(self) -> bool:
        # Return true if window/display is narrow
        # return self.page.window_height >= self.page.window_width
        return self.page.height >= self.page.width

    def is_landscape(self) -> bool:
        # Return true if window/display is wide
        return self.page.width > self.page.height

    def handle_resize(self, e):
        pass
