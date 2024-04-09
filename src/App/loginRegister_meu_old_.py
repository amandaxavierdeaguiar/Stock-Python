import flet as ft
import hashlib
import re
import pandas as pd
from Views.User.ListUser import table_data as db_user


class Login:

    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        page.title = 'Cadastro'
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.bgcolor = ft.colors.BLUE_100

        image = ft.Image(src="icons/login.png", width=150, height=150)
        txt_username = ft.TextField(label="Digite seu email", width=300, prefix_icon=ft.icons.EMAIL)
        txt_password = ft.TextField(label="Digite sua Password", width=300, password=True, can_reveal_password=True,
                                    prefix_icon=ft.icons.LOCK)

        checkbox_signup: ft.Checkbox = ft.Checkbox(
            label='Aceito os termos de uso',
            value=False
        )

        button_submit: ft.ElevatedButton = ft.ElevatedButton(
            text='Entre',
            width=140,
            disabled=True,
        )

        button_register: ft.ElevatedButton = ft.ElevatedButton(
            text='Cadastra-se',
            width=140,
        )

        create_user = ft.TextField(label="Digite o Nome:", width=300, prefix_icon=ft.icons.PERSON)
        create_login = ft.TextField(label="Digite o Login:", width=300, prefix_icon=ft.icons.EMAIL)
        create_password = ft.TextField(label="Digite a Password:", width=300, password=True, can_reveal_password=True,
                                       prefix_icon=ft.icons.LOCK)
        check_password = ft.TextField(label="Repita a Password:", width=300, password=True, can_reveal_password=True,
                                      prefix_icon=ft.icons.LOCK)

        create_type_acess = ft.Dropdown(
            options=[
                ft.dropdown.Option("Admin"),
                ft.dropdown.Option("Sub_Admin"),
                ft.dropdown.Option("User"),
            ],
            width=300,
        )

        button_register_user: ft.ElevatedButton = ft.ElevatedButton(
            text='Cadastro',
            width=140,
        )

        self.table_data = pd.DataFrame(columns=['name', "login", 'password', 'type_acess'])

        def validate(e: ft.ControlEvent) -> None:
            if all([txt_username.value, txt_password.value, checkbox_signup.value]):
                button_submit.disabled = False
            else:
                button_submit.disabled = True

            page.update()

        def submit(e: ft.ControlEvent) -> None:
            hashed_password = hashlib.sha256(txt_password.value.encode()).hexdigest()

            print(f'{txt_username.label}: {txt_username.value}')
            print(f'{txt_username.label}: {hashed_password}')
            print(f'{checkbox_signup.label}: {checkbox_signup.value}')

        def register(e: ft.ControlEvent) -> None:
            page.clean()
            page.add(
                ft.Container(
                    width=400,
                    height=450,
                    padding=50,
                    border_radius=20,
                    bgcolor="white",
                    content=ft.Column(
                        controls=[ft.Column(
                            controls=[
                                create_user,
                                create_login,
                                create_password,
                                check_password,
                                create_type_acess,
                                button_register_user,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        ],
                    )
                )
            )

        def login_alert(e: ft.ControlEvent):
            user = next((item for item in db_user if item['login'] == txt_username.value), None)

            if user is None:
                dlg = ft.AlertDialog(
                    title=ft.Text("Email Inválido"),
                    content=ft.Text("Digite novamente os dados!"),
                )
                page.dialog = dlg
                dlg.open = True
                page.update()
            else:
                print(f'Inseriu para o Banco de Dados.')

        def show_password_alert(e: ft.ControlEvent):
            if create_password.value != check_password.value:
                dlg = ft.AlertDialog(
                    title=ft.Text("As senhas não coincidem!"),
                    content=ft.Text("Verifique as informações fornecidas."),
                )
                page.dialog = dlg
                dlg.open = True
                page.update()

            elif not validate_password(create_password.value):
                alert = ft.AlertDialog(
                    title=ft.Text("Senha Inválida"),
                    content=ft.Text(
                        "A senha deve conter pelo menos 1 maiuscula, 1 caractere especial e ter no mínimo 8 caracteres!"),
                )
                page.dialog = alert
                alert.open = True
                page.update()

            else:
                new_data = {
                    'name': create_user.value,
                    'login': create_login.value,
                    'password': hashlib.sha256(create_password.value.encode()).hexdigest(),
                    'type_acess': create_type_acess.value
                }
                new_row = pd.DataFrame([new_data], columns=['name', "login", 'password', 'type_acess'])
                db_user_pd = pd.concat([db_user, new_row], ignore_index=True)

                # Clear form fields
                create_user.value = ''
                create_login.value = ''
                create_password.value = ''
                check_password.value = ''
                create_type_acess.value = None

                dlg = ft.AlertDialog(
                    title=ft.Text("Cadastro realizado com sucesso!"),
                    content=ft.Text("Você já pode fazer o login!"),
                )
                page.dialog = dlg
                dlg.open = True
                page.update()

        txt_username.on_change = validate
        txt_password.on_change = validate
        checkbox_signup.on_change = validate
        button_submit.on_click = login_alert
        button_register.on_click = register
        button_register_user.on_click = show_password_alert

        page.add(
            ft.Container(
                width=400,
                height=450,
                padding=20,
                border_radius=20,
                bgcolor="white",
                content=ft.Column(
                    controls=[ft.Column(
                        controls=[
                            image,
                            txt_username,
                            txt_password,
                            checkbox_signup
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                        ft.Row(controls=[
                            button_register,
                            button_submit,
                        ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=20,
                        )
                    ],
                )
            )
        )


def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@+$%&#/€?*.-])[a-zA-Z\d!@+$%&#/€?*.-]{8,16}$'

    if re.match(pattern, password):
        return True
    else:
        return False


if __name__ == '__main__':
    ft.app(target=Login, assets_dir="../assets")
