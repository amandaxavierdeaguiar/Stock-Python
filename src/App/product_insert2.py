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
        self._product_name = self.name_product()
        self._product_photo = self.product_photo()
        self._product_description = self.product_description()
        self._product_price = self.product_price()
        self._product_brand = self.product_brand()
        self._product_category = self.product_category()
        self._product_bar_cod = self.product_bar_code()
        self.

        self.image_insert_product = ft.Image(src=f"icons/produtos.png", width=200, height=200, fit=ft.ImageFit.CONTAIN)
        self.title_product = ft.Text("Insira o produto", **title_pg())

        self.content = self.create_containers(self.image_insert_product,
                                              self.title_product, self._product_name,
                                              self._product_photo, self._product_description, self._product_price,
                                              self._product_brand, self._product_category, self._product_bar_cod)

    @classmethod
    def name_product(cls):
        return ft.TextField(label="Nome do Produto", width=300)

    @classmethod
    def product_photo(cls, page):
        file_picker = ft.FilePicker(on_result=cls.insert_img_product)
        page.overlay.append(file_picker)

        cls.button_image = ft.ElevatedButton(text='Insira a Imagem', **button(),
                                              on_click=lambda _: file_picker.pick_files(allow_multiple=False,
                                                                                        allowed_extensions=['jpg',
                                                                                                            'jpeg',
                                                                                                            'png']))

    @classmethod
    def insert_img_product(cls, e: ft.FilePickerResultEvent, page):
        print(e.files)
        if e.files and len(e.files):
            with open(e.files[0].path, 'rb') as r:
                cls.img.src_base64 = base64.b64encode(r.read()).decode('utf-8')

                cls.img_Container.visible = True
                cls.btn_close_img.visible = True
                cls.img.visible = True
                # cls.image_insert_product.visible = False
                # cls.button_image.visible = False

                page.update()
    @classmethod
    def product_description(cls):
        return ft.TextField(label="Descrição do produto", multiline=True, max_lines=3)

    @classmethod
    def product_price(cls):
        return ft.TextField(label="Valor do produto", width=300, )  # ver como fica para ser float

    @classmethod
    def product_brand(cls):
        # Criando a lista Marca
        brand_list = db_brands

        # Puxando cada item da lista Marca
        cls.b = ft.Dropdown(label="Marca", width=300)
        for brand in brand_list:
            cls.b.options.append(ft.dropdown.Option(brand))

        return cls.b

    @classmethod
    def product_category(cls):
        # Criando uma lista para o box da Categoria
        category_list = db_category

        # Puxando cada item da lista Categoria
        cls.c = ft.Dropdown(label="Categoria", width=300)
        for category in category_list:
            cls.c.options.append(ft.dropdown.Option(category))

        return cls.c

    @classmethod
    def product_bar_code(cls):
        return ft.TextField(label="Código de Barras", width=300)

    @classmethod
    def button_enter(cls):
        return ft.ElevatedButton("Insira o produto", **button(),
                                 on_click=lambda _: print("Insiriu o produto na Base de Dados"))

    @classmethod
    def img(cls):
        return ft.Image(visible=False, fit=ft.ImageFit.CONTAIN)
    @classmethod
    def img_Container(cls):
        return ft.Stack([
                cls.img,
                cls.btn_close_img,
            ],
            width=300,
            height=300,
            visible=False
        )


    @classmethod
    def btn_close_img(cls):
        return IconButton(
            bgcolor=colors.BLACK26,
            top=10, right=10,
            icon=icons.CLOSE, icon_color=colors.WHITE54, selected=True,
            selected_icon=icons.CLOSE, on_click=cls.close_img, visible=False)

    @classmethod
    def create_containers(cls):
        return ft.Container(
                width=650,
                height=480,
                padding=10,
                border_radius=20,
                bgcolor="white",
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Column(width=200, height=400,
                                          controls=[
                                              cls.image_insert_product,
                                              cls.img_Container,
                                              cls.button_image,
                                              cls.button_enter
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
                                cls.title_product,
                                cls.txt_name_product,
                                cls.txt_price,
                                cls.txt_cod_bar,
                                cls.b,
                                cls.c,
                                cls.description_product,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                        ),

                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            )



if __name__ == '__main__':
    ft.app(target=ProductNew, assets_dir="./assets")
