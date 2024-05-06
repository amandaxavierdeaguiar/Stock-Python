import flet as ft
from flet import Text, Column, Control

from app.page.features.app_auth_login import AuthLogin
from app.page.features.app_auth_registration import AuthRegister
from shared.base.SharedControls import SharedControls


class AppAuth(SharedControls):
    def __init__(self, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.auth_login = AuthLogin(self.page, select_page=self.select_page)
        self.auth_register = AuthRegister(self.select_page)
        self.default_page = 0
        self.btn_login_signup = self.auth_login.button_signup
        self.btn_signup_submit = self.auth_register.button_cancel

        self.pages = [
            (self.btn_signup_submit, self.auth_login.content),
            (self.btn_login_signup, self.auth_register.content),
        ]

        self.content_area = self.set_controllers(self.pages)

        self._active_view: Control = Column(
            controls=[Text("")],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        # self.set_content()
        self._change_displayed_page(self.default_page)

    @classmethod
    def button_register(cls, var):
        return ft.ElevatedButton(text="Cadastra-se", width=140, on_click=var)

    @classmethod
    def button_submit_register(cls, var):
        return ft.ElevatedButton(text="Cadastro", width=140, on_click=var)

    def select_page(self, event):
        if event.control.data == "login_signup":
            self.default_page = 1
            self._change_displayed_page(1)
        elif event.control.data == "signup_submit":
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
        return [self.active_view, self.content_area]

    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.update()


if __name__ == "__main__":
    ft.app(target=AppAuth, assets_dir="../../../assets")
