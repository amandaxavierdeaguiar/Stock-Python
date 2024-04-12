import flet as ft
from flet import Text, Column, UserControl, icons, Control, IconButton, colors

from flet_core import Container

from App.features.app_auth_login import AuthLogin
from App.features.app_auth_registration import AuthRegister
from Views.User.ListUser import table_data as db_user


class AppAuth(UserControl):
    def __init__(self, user, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.auth_login = AuthLogin(user=user, page=self.page, select_page=self.select_page)
        self.auth_register = AuthRegister(self.page, self.select_page)
        self.default_page = 0
        self.btn_login_signup = self.auth_login.button_signup
        self.btn_signup_submit = self.auth_register.button_cancel

        self.pages = [
            (
                self.btn_signup_submit,
                self.auth_login.content
            ),
            (
                self.btn_login_signup,
                self.auth_register.content
            ),
        ]

        self.content_area = self.set_controllers(self.pages)

        self._active_view: Control = Column(controls=[
            Text("")
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        self.set_content()
        self._change_displayed_page(self.default_page)

    @classmethod
    def button_register(cls, var):
        return ft.ElevatedButton(text='Cadastra-se', width=140, on_click=var)

    @classmethod
    def button_submit_register(cls, var):
        return ft.ElevatedButton(text='Cadastro', width=140, on_click=var)

    def select_page(self, event):
        if event.control.data == 'login_signup':
            self.default_page = 1
            self._change_displayed_page(1)
        elif event.control.data == 'signup_submit':
            self.default_page = 0
            self._change_displayed_page(0)

    @classmethod
    def set_controllers(cls, pages):
        page_contents = [page_content for _, page_content in pages]
        content_area = Column(controls=page_contents, expand=True)
        return content_area

    def _change_displayed_page(self, page_number):
        for i, content_page in enumerate(self.content_area.controls):
            content_page.visible = page_number == i
            self.page.update()

    def set_content(self):
        self.page.controls = [self.active_view,
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
