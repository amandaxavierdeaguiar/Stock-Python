import flet as ft

from shared.base.SharedControls import SharedControls


class InsertSupplier(SharedControls):
    title_supplier: ft.Text
    txt_name_supplier: ft.TextField
    txt_address_supplier: ft.TextField
    txt_phone_supplier: ft.TextField
    txt_email_supplier: ft.TextField
    button_enter: ft.ElevatedButton
    image_supplier: ft.Image
    btn_close_supplier: ft.IconButton
    container: ft.Container

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def get_content(cls, show=None):
        cls.title_supplier = ft.Text("Insira o Fornecedor", size=30, color=ft.colors.BLUE_900)

        cls.txt_name_supplier = ft.TextField(label="Nome do Fornecedor: ", width=300)
        cls.txt_address_supplier = ft.TextField(label="Morada do Fornecedor: ", width=300)
        cls.txt_phone_supplier = ft.TextField(label="Telefone do Fornecedor: ", width=300)
        cls.txt_email_supplier = ft.TextField(label="Email", width=300)
        cls.button_enter = ft.ElevatedButton("Insira o produto")
        # on_click=self.insert_supplier

        cls.image_supplier = ft.Image(src=f"icons/supplier2.png", width=200, height=200, fit=ft.ImageFit.CONTAIN)

        cls.btn_close_supplier = ft.IconButton(
            bgcolor=ft.colors.BLACK26,
            icon=ft.icons.CLOSE, icon_color=ft.colors.WHITE54, selected=True,
            selected_icon=ft.icons.CLOSE, visible=True)

        container = ft.Container(
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
                                          ft.Row(
                                              controls=[cls.btn_close_supplier],
                                              alignment=ft.MainAxisAlignment.START,
                                          ),
                                          cls.image_supplier,
                                      ],
                                      spacing=20,
                                      alignment=ft.MainAxisAlignment.CENTER,
                                      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                      ),
                        ],
                        # alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    ft.Column(width=30,
                              controls=[
                              ],
                              # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                              ),
                    ft.Column(

                        controls=[
                            cls.title_supplier,
                            cls.txt_name_supplier,
                            cls.txt_address_supplier,
                            cls.txt_phone_supplier,
                            cls.txt_email_supplier,
                            cls.button_enter,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    ),

                ],
                # alignment=ft.MainAxisAlignment.CENTER,
                # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
        return container

    """def insert_supplier(self, e):
        self.email = self.txt_email_supplier.value
        if not self.validate_email(self.email):
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
            return False"""
