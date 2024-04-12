import flet as ft
import hashlib
import os
import re
from flet import Text, Column, UserControl, icons, Control, IconButton, colors
import pandas as pd

from flet_core import Container
from Models.UserAuthentication import UserAuthentication
from Views.User.ListUser import table_data as db_user


class AuthRegister(UserControl):
    def __init__(self, page, var, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.auth = UserAuthentication()

        self._input_name = self.name()
        self._input_login = self.login()
        self._input_password = self.password()
        self._check_password = self.check_password()
        self._type_access = self.type_access()
        self.button_submit_register: ft.ElevatedButton = self.button_submit_signup(
            data="signup_submit", var_on_change=var, var_alert=self.show_password_alert)
        self.button_cancel: ft.ElevatedButton = self.create_button_cancel(
            data="signup_submit", var_on_change=var)
        self.content = self.create_register(self._input_name, self._input_login,
                                            self._input_password, self._check_password, self._type_access,
                                            self.button_submit_register, self.button_cancel)

    @classmethod
    def name(cls):
        return ft.TextField(label="Digite o Nome:", width=300, prefix_icon=ft.icons.PERSON)

    @classmethod
    def login(cls):
        return ft.TextField(label="Digite o Login:", width=300, prefix_icon=ft.icons.EMAIL)

    @classmethod
    def password(cls):
        return ft.TextField(label="Digite a Password:", width=300, password=True,
                            can_reveal_password=True, prefix_icon=ft.icons.LOCK)

    @classmethod
    def check_password(cls):
        return ft.TextField(label="Repita a Password:", width=300, password=True,
                            can_reveal_password=True, prefix_icon=ft.icons.LOCK)

    @classmethod
    def type_access(cls):
        return ft.Dropdown(
            options=[
                ft.dropdown.Option("Admin"),
                ft.dropdown.Option("Sub_Admin"),
                ft.dropdown.Option("User"),
            ],
            width=300,
        )

    @classmethod
    def button_submit_signup(cls, data, var_on_change=None, var_alert=None):
        return ft.ElevatedButton(text='Cadastro', width=140, on_click=var_alert,
                                 data=data, on_animation_end=var_on_change)

    @classmethod
    def create_button_cancel(cls, data, var_on_change=None):
        return ft.ElevatedButton(text='Voltar', width=140, on_click=var_on_change, data=data)

    @classmethod
    def create_register(cls, name, login, password, check_password, type_access, signup, cancel) -> Container:
        return ft.Container(
            width=400,
            height=450,
            padding=50,
            border_radius=20,
            bgcolor="white",
            content=ft.Column(
                controls=[ft.Column(
                    controls=[
                        name,
                        login,
                        password,
                        check_password,
                        type_access,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                    ft.Row(controls=[
                        cancel,
                        signup,
                    ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    )
                ],
            )
        )

    def show_password_alert(self):
        if self._input_password.value != self._check_password.value:
            dlg = ft.AlertDialog(
                title=ft.Text("As senhas não coincidem!"),
                content=ft.Text("Verifique as informações fornecidas."),
            )
            self.page.dialog = dlg
            dlg.open = True
            self.page.update()

        elif not self.auth.validate_password(self._input_password.value):
            alert = ft.AlertDialog(
                title=ft.Text("Senha Inválida"),
                content=ft.Text(
                    "A senha deve conter pelo menos 1 maiuscula, 1 caractere especial e ter no mínimo 8 caracteres!"),
            )
            self.page.dialog = alert
            alert.open = True
            self.page.update()

        else:
            salt = os.urandom(16)
            salt_hex = salt.hex()
            password_hash = hashlib.pbkdf2_hmac(
                'sha256', self._input_password.value.encode('UTF-8'), salt, 100000)
            password_hash_hex = password_hash.hex()
            new_data = {
                'name': self._input_name.value,
                'login': self._input_login.value,
                'password': password_hash_hex,
                'type_access': self._type_access.value
            }
            new_row = pd.DataFrame([new_data], columns=['name', "login", 'password', 'type_acess'])
            db_user_pd = pd.concat([db_user, new_row], ignore_index=True)

            # Clear form fields
            self._input_name.value = ''
            self._input_login.value = ''
            self._input_password.value = ''
            self._check_password.value = ''
            self._type_access.value = None

            dlg = ft.AlertDialog(
                title=ft.Text("Cadastro realizado com sucesso!"),
                content=ft.Text("Você já pode fazer o login!"),
            )
            self.page.dialog = dlg
            dlg.open = True
            self.page.update()
