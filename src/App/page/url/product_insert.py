import base64
import os

import flet as ft
from flet import colors, icons, IconButton

from app.app_style import title_pg, button
from app.page.features.fields_product import get_text_field, get_dropdown, get_text
from shared.Enums.QuantityType import QuantityType
from shared.base.SharedControls import SharedControls
from views.Product.ProductView import ProductView


class ProductNew(SharedControls):
    product_view = ProductView()
    txt_name_product: ft.TextField
    txt_price: ft.TextField
    category_dropdown: ft.Dropdown
    brand_dropdown: ft.Dropdown
    description_text: ft.TextField
    image_insert_product: ft.Image
    btn_close_img: IconButton
    button_image: ft.ElevatedButton
    button_enter: ft.ElevatedButton
    img_Container: ft.Stack
    quantity_dropdown: ft.Dropdown

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def get_content(cls, file_picker, show=None):
        # Colocar título
        title_product = ft.Text("Insira o produto", **title_pg())

        # ADD
        # Pedindo para inserir os dados:
        cls.txt_name_product = get_text_field(txt_label='Nome do Produto', write=True)
        cls.txt_price = get_text_field(txt_label="Valor do Produto", size=True, write=True)

        # Puxando cada item da lista Categoria
        category = cls.product_view.get_all_categories()
        cls.category_dropdown = get_dropdown("Categoria", list=category)

        # Puxando cada item da lista Marca
        brand = cls.product_view.get_all_brands()
        cls.brand_dropdown = get_dropdown("Marca", list=brand)

        # Descrição do Produto
        cls.description_text = get_text()

        cls.button_enter = ft.ElevatedButton(
            **button(),
            icon=icons.SAVE,
            text="Insira o produto",
            on_click=lambda _: print("Insiriu o produto na Base de Dados"),
        )

        cls.btn_close_img = IconButton(
            bgcolor=colors.BLACK26,
            top=10,
            right=10,
            icon=icons.CLOSE,
            icon_color=colors.WHITE54,
            selected=True,
            selected_icon=icons.CLOSE,
            on_click=cls.close_img,
            visible=False,
        )
        cls.image_insert_product = ft.Image(visible=False, fit=ft.ImageFit.CONTAIN)
        cls.img_Container = ft.Stack(
            [
                cls.image_insert_product,
                cls.btn_close_img,
            ],
            width=300,
            height=300,
            visible=False,
        )

        cls.button_image = ft.ElevatedButton(
            **button(),
            icon=icons.UPLOAD_FILE,
            text="Insira a Imagem",
            on_click=lambda _: file_picker.pick_files(
                allow_multiple=False, allowed_extensions=["jpg", "jpeg", "png"]
            ),
        )

        # Quantity Type
        quantity_ = QuantityType.return_types()
        cls.quantity_dropdown = get_dropdown("Unidade de Medida", list=quantity_)

        container = ft.Container(
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
                                width=200,
                                height=400,
                                controls=[
                                    cls.image_insert_product,
                                    cls.img_Container,
                                    file_picker,
                                    cls.button_image,
                                    cls.button_enter,
                                ],
                                spacing=20,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    ft.Column(
                        controls=[
                            title_product,
                            cls.txt_name_product,
                            ft.Row(controls=[cls.quantity_dropdown, cls.txt_price]),
                            ft.Row(controls=[cls.brand_dropdown, cls.category_dropdown]),
                            cls.description_text,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )
        return container

    @classmethod
    def insert_img_product(cls, e: ft.FilePickerResultEvent):
        if e.files and len(e.files):
            file_path = e.files[0].path
            with open(file_path, 'rb') as f:
                image_content = f.read()

                # Obter a extensão do arquivo usando o método os.path.splitext
                file_name, file_extension = os.path.splitext(file_path)

                # Diretório de destino para salvar a imagem
                directory = os.path.abspath('assets/products')
                if not os.path.exists(directory):
                    os.makedirs(directory)

                # Nome do produto em letras minúsculas, separado por _
                name_text = cls.txt_name_product.value.strip().lower().split()
                name_separate = "_".join(name_text)
                file_name = name_separate + file_extension

                # Converte a imagem em base64 para exibição
                img_base64 = base64.b64encode(image_content).decode('utf-8')
                cls.image_insert_product.src = f'{directory}/{file_name}'

                cls.image_insert_product.data = file_name
                # Inclui com o Fábio
                # data para identificar o que é aquele campo

                # Salvar o arquivo no diretório
                with open(os.path.join(directory, file_name), 'wb') as w:
                    w.write(image_content)

                # Atualiza a interface gráfica
                cls.img_Container.visible = True
                cls.btn_close_img.visible = True
                cls.image_insert_product.visible = True
                cls.image_insert_product.visible = False
                cls.button_image.visible = False

    @classmethod
    def close_img(cls, e):
        cls.img_Container.visible = not cls.img_Container.visible
        cls.btn_close_img.visible = not cls.btn_close_img.visible


if __name__ == "__main__":
    ft.app(target=ProductNew, assets_dir="./assets")
