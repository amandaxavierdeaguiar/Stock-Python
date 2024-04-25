import base64

import flet as ft
from flet import colors, icons, IconButton

from Views_Amanda.Product.ListProduct import brand_list as db_brands
from Views_Amanda.Product.ListProduct import category_list as db_category
from app.app_style import title_pg, button

class ProductNew:
    def close_img(self, e):
        self.img_Container.visible = not self.img_Container.visible
        self.btn_close_img.visible = not self.btn_close_img.visible
        self.page.update()

    def __init__(self, page: ft.Page):
        self.page = page
        page.title = 'Produtos'
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.bgcolor = ft.colors.GREY_400

        

        # Colocar título
        self.title_product = ft.Text("Insira o produto", **title_pg())  # ADD
        # Pedindo para inserir os dados:
        self.txt_name_product = ft.TextField(label="Nome do Produto", width=300)
        self.txt_price = ft.TextField(label="Valor do produto", width=300, )  # ver como fica para ser float

        self.txt_cod_bar = ft.TextField(label="Código de Barras", width=300)

        # Criando uma lista para o box da Categoria
        category_list = db_category

        # Puxando cada item da lista Categoria
        self.c = ft.Dropdown(label="Categoria", width=300)
        for category in category_list:
            self.c.options.append(ft.dropdown.Option(category))

        # Criando a lista Marca
        brand_list = db_brands

        # Puxando cada item da lista Marca
        self.b = ft.Dropdown(label="Marca", width=300)
        for brand in brand_list:
            self.b.options.append(ft.dropdown.Option(brand))

        self.button_enter = ft.ElevatedButton("Insira o produto",**button(),
                                              on_click=lambda _: print("Insiriu o produto na Base de Dados"))

        self.btn_close_img = IconButton(
            bgcolor=colors.BLACK26,
            top=10, right=10,
            icon=icons.CLOSE, icon_color=colors.WHITE54, selected=True,
            selected_icon=icons.CLOSE, on_click=self.close_img, visible=False)
        self.img = ft.Image(visible=False, fit=ft.ImageFit.CONTAIN)
        self.img_Container = ft.Stack(
            [
                self.img,
                self.btn_close_img,
            ],
            width=300,
            height=300,
            visible=False
        )

        def insert_img_product(e: ft.FilePickerResultEvent):
            print(e.files)
            if e.files and len(e.files):
                with open(e.files[0].path, 'rb') as r:
                    self.img.src_base64 = base64.b64encode(r.read()).decode('utf-8')

                    self.img_Container.visible = True
                    self.btn_close_img.visible = True
                    self.img.visible = True
                    self.image_insert_product.visible = False
                    self.button_image.visible = False

                    page.update()
                # importar base 64

        # inserir imagem
        # aparecer a imagem  na tela
        # image_holder = ft.Image(visible=False, fit=ft.ImageFit.CONTAIN, width=30, height=30)

        file_picker = ft.FilePicker(on_result=insert_img_product)
        page.overlay.append(file_picker)

        self.button_image = ft.ElevatedButton(text='Insira a Imagem', **button(),
                                              on_click=lambda _: file_picker.pick_files(allow_multiple=False,
                                                                                        allowed_extensions=['jpg',
                                                                                                            'jpeg',
                                                                                                            'png']))

        # Scrollable description box
        self.description_product = ft.TextField(label="Descrição do produto", multiline=True, max_lines=3)

        # Funcao que deixa a foto e caso adicione uma imagem, tira ela
        self.image_insert_product = ft.Image(src=f"icons/produtos.png", width=200, height=200, fit=ft.ImageFit.CONTAIN)

        page.add(
            ft.Container(
                width=650,
                height=480,
                padding=10,
                border_radius=20,
                bgcolor="white",
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Column(
                                    controls=[
                                        # image_holder,
                                    ],
                                    # alignment=ft.MainAxisAlignment.CENTER,
                                    # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=5,
                                ),
                                ft.Column(width=200, height=400,
                                          controls=[
                                              self.image_insert_product,
                                              self.img_Container,
                                              self.button_image,
                                              self.button_enter
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
                                self.title_product,
                                self.txt_name_product,
                                self.txt_price,
                                self.txt_cod_bar,
                                self.b,
                                self.c,
                                self.description_product,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                        ),

                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        )


if __name__ == '__main__':
    ft.app(target=ProductNew, assets_dir="./assets")
