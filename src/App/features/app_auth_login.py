import flet as ft
import hashlib
import re
from flet import Text, Column, UserControl, TextField, Image
from flet_core import Container

from Views.User.ListUser import table_data as db_user


class AuthLogin(UserControl):
    def __init__(self, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page

        self._image: Image = self.image()
        self._input_login: TextField = self.login()
        self._input_login.on_change = self.validate

        self._input_password: TextField = self.password()
        self._input_password.on_change = self.validate

        self._checkbox_signup = self.checkbox_signup()
        self._checkbox_signup.on_change = self.validate
        self._button_submit: ft.ElevatedButton = self.button_submit()
        self.button_register: ft.ElevatedButton = self.button_register()

    def validate(self, e: ft.ControlEvent) -> None:
        if all([self._input_login.value, self._input_password.value, self._checkbox_signup.value]):
            self.button_submit.disabled = False
        else:
            self.button_submit.disabled = True

        self.page.update()

    @classmethod
    def image(cls):
        return ft.Image(src="icons/login.png", width=150, height=150)

    @classmethod
    def login(cls):
        return ft.TextField(label="Digite seu email", width=300, prefix_icon=ft.icons.EMAIL)

    @classmethod
    def password(cls):
        return ft.TextField(label="Digite sua Password", width=300, password=True,
                                       can_reveal_password=True,
                                       prefix_icon=ft.icons.LOCK)

    @classmethod
    def checkbox_signup(cls):
        return ft.Checkbox(label='Aceito os termos de uso', value=False)

    @classmethod
    def button_submit(cls):
        return ft.ElevatedButton(text='Entre', width=140, disabled=True, on_click=cls.login_alert)

    @classmethod
    def button_register(cls):
        return ft.ElevatedButton(text='Cadastra-se', width=140)

    @classmethod
    def get_login(cls):
        return ft.Container(
            width=400,
            height=450,
            padding=20,
            border_radius=20,
            bgcolor="white",
            content=ft.Column(
                controls=[ft.Column(
                    controls=[
                        cls.image(),
                        cls.login(),
                        cls.password(),
                        cls.checkbox_signup(),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                    ft.Row(controls=[
                        cls.button_register(),
                        cls.button_submit(),
                    ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    )
                ],
            )
        )

    def login_alert(self):
        user = next((item for item in db_user if item['login'] == self._input_login.value), None)

        if user is None:
            dlg = ft.AlertDialog(
                title=ft.Text("Email Inválido"),
                content=ft.Text("Digite novamente os dados!"),
            )
            self.page.dialog = dlg
            dlg.open = True
            self.page.update()
        else:
            print(f'ENTRAR NO SISTEMA')
