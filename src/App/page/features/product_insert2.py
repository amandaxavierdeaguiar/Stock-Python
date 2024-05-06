import base64
import os

import flet as ft
from PIL import Image
from flet import colors, icons, IconButton

from app.app_style import title_pg, button
from views.Product.ProductView import ProductView


class ProductNew():
    product_view = ProductView()
    img: ft.Image
    title_product: ft.Text
    txt_name_product: ft.TextField
    txt_price: ft.TextField
    _product_brand_input: ft.Dropdown
    _product_category_input: ft.Dropdown
    description_product: ft.TextField

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

        self.title_product = ft.Text("Insira o produto", **title_pg())
        self.txt_name_product = ft.TextField(label="Nome do Produto", width=300)
        self.txt_price = ft.TextField(label="Valor do produto", width=300, )  # TRANSFORMAR DEPOIS PARA FLOAT

        self._product_category_input = self.product_category()
        self._product_brand_input = self.product_brandy()

        self.button_enter = ft.ElevatedButton("Insira o produto", **button(), icon=icons.SAVE, on_click=self.on_submit)

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

        self.file_picker = ft.FilePicker(data=self.txt_name_product.value, on_result=self.insert_img_product)
        page.overlay.append(self.file_picker)

        self.button_image = ft.ElevatedButton(text='Insira a Imagem', data='button_image', **button(),
                                              icon=icons.UPLOAD_FILE,
                                              on_click=lambda _: self.file_picker.pick_files
                                              (allow_multiple=False, allowed_extensions=['jpg', 'jpeg', 'png']))

        self.description_product = ft.TextField(label="Descrição do produto", multiline=True, max_lines=3)

        # Funcao que deixa a foto e caso adicione uma imagem, tira ela
        self.image_insert_product = ft.Image(src=f"icons/products.png", width=200, height=200, fit=ft.ImageFit.CONTAIN)

        self.page.add(
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
                                    ],

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
                            spacing=20,
                        ),
                        ft.Column(width=30,
                                  controls=[
                                  ],
                                  ),
                        ft.Column(
                            controls=[
                                self.title_product,
                                self.txt_name_product,
                                self.txt_price,
                                self._product_brand_input,
                                self._product_category_input,
                                self.description_product,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                        ),

                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            )
        )

    def insert_img_product(self, e: ft.FilePickerResultEvent):
        BASE_DIR = os.path.dirname(os.path.abspath('../../../'))
        path = e.files[0].path
        print(e.control.data)
        if e.files and len(e.files):
            with open(os.path.join(os.path.dirname(_file_), "assets", e.files[0].name), 'ab+') as r:
                self.img.src_base64 = base64.b64encode(r.read()).decode('utf-8')

                im1 = Image.open(path)

                # Obtenha a extensão do arquivo usando o método os.path.splitext
                file_name, file_extension = os.path.splitext(e.files[0].path)
                file_name = self.txt_name_product.value + file_extension
                BASE_DIR = os.path.dirname(os.path.abspath('../../../'))
                path = f'{BASE_DIR}\\src\\assets\\products\\{file_name}'
                im1.save(path)
                self.img_Container.visible = True
                self.btn_close_img.visible = True
                self.img.visible = True
                self.image_insert_product.visible = False
                self.button_image.visible = False

            self.page.update()

    @classmethod
    def product_brandy(cls):
        brandy = cls.product_view.get_all_brands()
        brandy_all = ft.Dropdown(label="Marca", width=300)
        for brandy in brandy:
            brandy_all.options.append(ft.dropdown.Option(brandy))

        return brandy_all

    @classmethod
    def product_category(cls):
        category = cls.product_view.get_all_categories()
        category_all = ft.Dropdown(label="Categoria", width=300)
        for category in category:
            category_all.options.append(ft.dropdown.Option(category))
        return category_all

    @classmethod
    def on_submit(cls, e):
        new_data = {
            'name': cls.txt_name_product.value,
            'photo': cls.img.src_base64,  # tem que ver
            'Description': cls.description_product.value,
            'price': float(cls.txt_price.value),
            'brand_name': cls._product_brand_input.value,
            'category_name': cls._product_category_input.value,
        }

        cls.product_view.new_product(new_data)


if __name__ == '__main__':
    ft.app(target=ProductNew, assets_dir="../../../assets", upload_dir="../../../assets/products")
