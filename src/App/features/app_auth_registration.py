import flet as ft
import hashlib
import re
from flet import Text, Column, UserControl, icons, Control, IconButton, colors

from flet_core import Container

from Views.User.ListUser import table_data as db_user


class AuthRegister(UserControl):
    def __init__(self, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page

        self.create_user = ft.TextField(label="Digite o Nome:", width=300, prefix_icon=ft.icons.PERSON)
        self.create_login = ft.TextField(label="Digite o Login:", width=300, prefix_icon=ft.icons.EMAIL)
        self.create_password = ft.TextField(label="Digite a Password:", width=300, password=True,
                                            can_reveal_password=True, prefix_icon=ft.icons.LOCK)
        self.check_password = ft.TextField(label="Repita a Password:", width=300, password=True,
                                           can_reveal_password=True, prefix_icon=ft.icons.LOCK)

        self.create_type_acess = ft.Dropdown(
            options=[
                ft.dropdown.Option("Admin"),
                ft.dropdown.Option("Sub_Admin"),
                ft.dropdown.Option("User"),
            ],
            width=300,
        )

        self.button_register_user: ft.ElevatedButton = ft.ElevatedButton(text='Cadastro', width=140, )

        self.button_register_user.on_click = self.show_password_alert

    def create_register(self) -> Container:
        return ft.Container(
            width=400,
            height=450,
            padding=50,
            border_radius=20,
            bgcolor="white",
            content=ft.Column(
                controls=[ft.Column(
                    controls=[
                        self.create_user,
                        self.create_login,
                        self.create_password,
                        self.check_password,
                        self.create_type_acess,
                        self.button_register_user,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ],
            )
        )

    @classmethod
    def show_password_alert(cls):
        if cls.create_password.value != cls.check_password.value:
            dlg = ft.AlertDialog(
                title=ft.Text("As senhas não coincidem!"),
                content=ft.Text("Verifique as informações fornecidas."),
            )
            cls.page.dialog = dlg
            dlg.open = True
            cls.page.update()

        elif not validate_password(cls.create_password.value):
            alert = ft.AlertDialog(
                title=ft.Text("Senha Inválida"),
                content=ft.Text(
                    "A senha deve conter pelo menos 1 maiuscula, 1 caractere especial e ter no mínimo 8 caracteres!"),
            )
            cls.page.dialog = alert
            alert.open = True
            cls.page.update()

        else:
            new_data = {
                'name': cls.create_user.value,
                'login': cls.create_login.value,
                'password': hashlib.sha256(cls.create_password.value.encode()).hexdigest(),
                'type_acess': cls.create_type_acess.value
            }
            new_row = pd.DataFrame([new_data], columns=['name', "login", 'password', 'type_acess'])
            cls.table_data = pd.concat([cls.table_data, new_row], ignore_index=True)

            # Clear form fields
            cls.create_user.value = ''
            cls.create_login.value = ''
            cls.create_password.value = ''
            cls.check_password.value = ''
            cls.create_type_acess.value = None

            dlg = ft.AlertDialog(
                title=ft.Text("Cadastro realizado com sucesso!"),
                content=ft.Text("Você já pode fazer o login!"),
            )
            cls.page.dialog = dlg
            dlg.open = True
            cls.page.update()