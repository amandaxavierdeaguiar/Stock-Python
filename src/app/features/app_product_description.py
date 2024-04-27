import flet as ft
from app.features.chart_date_quantity import DateQuantity

from app.app_style import disabled_textfield, title
from shared.Base.SharedControls import SharedControls
from views.Product.ProductView import ProductView


class ProductDescription(SharedControls):
    product_view = ProductView()
    date_quantity = DateQuantity()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_content(self, seleted):
        product = self.product_view.get_product(seleted["product_name"])
        quantities = self.product_view.get_history_quantity(seleted["product_name"])
        prices = self.product_view.get_history_prices(seleted["product_name"])
        # Colocar título
        title_product = ft.Text("Descrição do produto", **title())

        # TextField nome do Produto
        txt_name_product = ft.TextField(
            **disabled_textfield(),
            value=product.name,
            label="Nome do Produto",
            width=450,
        )

        # TextField Valor do Produto
        txt_price = ft.TextField(
            **disabled_textfield(),
            label="Valor do Produto",
            width=450,
            value=product.price,
        )

        # TextField Categoria
        c = ft.TextField(
            **disabled_textfield(),
            label="Categoria",
            width=220,
            value=product.category_id,
        )

        # TextField Categoria
        b = ft.TextField(
            **disabled_textfield(),
            label="Marca",
            width=220,
            value=product.brand_id,
        )

        # Descrição do Produto
        description_db = product.description

        button_enter = ft.ElevatedButton(
            "Edite o produto",
            on_click=lambda _: print("Insiriu o produto na Base de Dados"),
        )

        image_insert_product = ft.Image(
            src=f"products/{product.photo}",
            width=200,
            height=200,
            fit=ft.ImageFit.CONTAIN,
        )

        container = ft.Container(
            width=1230,  # 720
            height=730,
            padding=10,
            border_radius=20,
            bgcolor="white",
            content=ft.Column(
                scroll=ft.ScrollMode.ALWAYS,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Column(
                                        width=230,
                                        height=400,
                                        controls=[
                                            image_insert_product,
                                            button_enter,
                                        ],
                                        spacing=20,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                ],
                                spacing=20,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Column(
                                        controls=[
                                            title_product,
                                            txt_name_product,
                                            txt_price,
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                        controls=[
                                            b,
                                            c,
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Container(
                                                height=150,
                                                width=450,
                                                border_radius=5,
                                                border=ft.border.all(
                                                    0.9, ft.colors.GREY
                                                ),
                                                padding=ft.padding.all(5),
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Column(
                                                            controls=[
                                                                ft.Text(description_db)
                                                            ],
                                                            height=140,
                                                            width=440,
                                                            scroll=ft.ScrollMode.ALWAYS,
                                                            on_scroll_interval=0,
                                                        ),
                                                    ]
                                                ),
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ],
                    ),
                    ft.Row(
                        controls=[
                            self.date_quantity.create_chart(prices),
                        ],
                    ),
                    ft.Row(
                        controls=[
                            self.date_quantity.create_chart(quantities),
                        ],
                    ),
                ],
            ),
        )
        return container
