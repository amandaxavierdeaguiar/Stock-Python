import flet as ft

from app.app_style import title_pg
from app.page.features.chart import Charts
from app.page.features.fields_product import get_TextField, get_dropdown, get_text, get_image
from shared.base.SharedControls import SharedControls
from views.Product.ProductView import ProductView


# from app.features.app_product_edit import ProductEdit


class ProductEdit(SharedControls):
    product_view = ProductView()
    date_quantity = Charts()
    # product_edit = ProductEdit()

    txt_name_product: ft.TextField
    txt_price: ft.TextField
    c: ft.TextField
    b: ft.TextField
    description_db: ft.Container
    image_insert_product: ft.Image
    btn_edit: ft.ElevatedButton
    selected = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.selected = None

    def get_content(self, seleted, show=None):
        self.selected = seleted
        product = self.product_view.get_product(seleted["product_name"])
        quantities = self.product_view.get_history_quantity(seleted["product_name"])
        prices = self.product_view.get_history_prices(seleted["product_name"])
        # Colocar título
        title_product = ft.Text("Descrição do produto", **title_pg())

        # TextField nome do Produto
        self.txt_name_product = get_TextField(product.name, 'Nome do Produto')
        # self.txt_name_product.disabled = True

        # TextField Valor do Produto
        self.txt_price = get_TextField(product.price, "Valor do Produto")
        # self.txt_price.disabled = True

        # TextField Categoria
        category = self.product_view.get_all_categories()
        dropdown_category = get_dropdown("Categoria", category)

        # TextField Brand
        brand = self.product_view.get_all_brands()
        dropdown_brand = get_dropdown("Marca", brand)

        # Descrição do Produto
        description_text = get_text(product.description)

        image_insert_product = get_image(product.photo)
        self.btn_edit = ft.ElevatedButton(text='Edit Product', on_click=show, data='Stock_edit')

        container = ft.Container(
            width=1500,  # 1230
            height=800,  # 730
            padding=10,
            border_radius=20,
            bgcolor=ft.colors.WHITE,
            content=ft.Column(
                scroll=ft.ScrollMode.ALWAYS,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Column(
                                        width=180,  # 230
                                        height=400,
                                        controls=[
                                            image_insert_product,
                                            # button_enter,
                                            self.btn_edit,
                                            self.btn_edit,
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                ],
                                # spacing=20,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Column(
                                        controls=[
                                            title_product,
                                            self.txt_name_product,
                                            self.txt_price,
                                            ft.Row(
                                                controls=[
                                                    dropdown_brand,
                                                    dropdown_category,
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                            ),
                                            description_text,
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),

                                ],

                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ],
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
        )
        return container
