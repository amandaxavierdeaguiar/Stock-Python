import flet as ft
from flet import Container, Column, Row

from app.app_layout import AppLayout
from app.page.app_header import AppHeader
from app.page.url.app_auth import AppAuth
from shared.base.SharedControls import SharedControls


class AppWindow(SharedControls):
    """A desktop app layout with a menu on the left."""

    def __init__(self, page, *args, **kwargs):
        super().__init__(page, *args, **kwargs)
        self.init_page = page
        self.page = page
        self.page.pubsub.subscribe(self.change_page)

        self.page.on_resize = self.handle_resize

        self._was_portrait = self.is_portrait()
        self._panel_visible = self.is_landscape()

        self.appbar = AppHeader(self.page)
        self.page.appbar = self.appbar.app_bar

        if self.user.is_login:
            self.app_page = AppLayout(self.page)
            new = self.app_page.set_content(self._panel_visible)
            self.set_controllers(new=new, type_page="table")
        else:
            self.app_auth = AppAuth(self.page)
            new = self.app_auth.set_content()
            self.set_controllers(new=new, type_page="login")

    def set_controllers(self, new, type_page):
        self.page.controls.clear()
        if type_page == "login":
            content_column = Column(controls=new)
            content = Container(
                expand=True,
                content=content_column,
                alignment=ft.alignment.bottom_center,
            )
            self.page.controls = [content]
        else:
            content_column = Row(controls=new, expand=True)
            content = Container(expand=True, content=content_column)
            self.page.controls = [content]
            self.page.update()
        # try:
        #     self.page.update()
        # except Exception as e:
        #     print(e)

    def change_page(self, event=None):
        if event["login"]:
            self.__init__(self.init_page)
        elif not event["login"]:
            self.__init__(page=self.init_page, user=self.user)

    def is_portrait(self) -> bool:
        # Return true if window/display is narrow
        # return self.page.window_height >= self.page.window_width
        return self.page.height >= self.page.width

    def is_landscape(self) -> bool:
        # Return true if window/display is wide
        return self.page.width > self.page.height

    def handle_resize(self, e):
        pass
