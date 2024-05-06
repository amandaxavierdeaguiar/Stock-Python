import flet as ft
import base64
from flet import Text, Column, colors, icons, IconButton, Control, Row, Container, Image, ImageFit
import re


class SupplierInsert:
    def __init__(self, page: ft.Page):
        self.page = page
        page.title = 'Fornecedores'
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.bgcolor = ft.colors.BLUE_500

        # Colocar título
        self.title_supplier = ft.Text("Insira o Fornecedor", size=30, color=colors.BLUE_900)

        self.txt_name_supplier = ft.TextField(label="Nome do Fornecedor: ", width=300)
        self.txt_address_supplier = ft.TextField(label="Morada do Fornecedor: ", width=300)
        self.txt_phone_supplier = ft.TextField(label="Telefone do Fornecedor: ", width=300)
        self.txt_email_supplier = ft.TextField(label="Email", width=300)
        self.button_enter = ft.ElevatedButton("Insira o produto", on_click=self.insert_supplier)

        self.image_supplier = ft.Image(src=f"icons/supplier2.png", width=200, height=200, fit=ft.ImageFit.CONTAIN)

        page.add(
            ft.Container(
                width=600,
                height=400,
                padding=10,
                border_radius=20,
                bgcolor="white",
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Column(width=200, height=400,
                                          controls=[
                                              self.image_supplier,
                                          ],
                                          spacing=20,
                                          alignment=ft.MainAxisAlignment.CENTER,
                                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                          ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=20,
                        ),
                        ft.Column(width=30,
                                  controls=[
                                  ],
                                  # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                  ),
                        ft.Column(
                            controls=[
                                self.title_supplier,
                                self.txt_name_supplier,
                                self.txt_address_supplier,
                                self.txt_phone_supplier,
                                self.txt_email_supplier,
                                self.button_enter,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),

                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        )

    def insert_supplier(self, e):
        email = self.txt_email_supplier.value
        if not validate_email(email):
            alert = ft.AlertDialog(
                title=ft.Text("Email Inválido"),
                content=ft.Text("Favor insira novamente!"),
            )
            self.page.dialog = alert
            alert.open = True
            self.page.update()
        else:
            print("Insiriu o produto na Base de Dados")


def validate_email(email):
    pattern = r'^[a-zA-Z]+[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,7}$'

    if re.match(pattern, email):
        return True
    else:
        return False


if __name__ == '__main__':
    ft.app(target=SupplierInsert, assets_dir="./assets")
