import flet as ft
from flet import Text, Column, Card, Row, Container

from app.page.features.app_table import AppTable
from controllers.StockController import StockController
from controllers.SupplierController import SupplierController
from controllers.UserController import UserController
from shared.base.SharedControls import SharedControls
from views.Product.ProductView import ProductView


class AppPages(SharedControls):
    """ """

    ctrl_stock: StockController = StockController()
    ctrl_user: UserController = UserController()
    ctrl_supplier: SupplierController = SupplierController()
    product_view: ProductView = ProductView()

    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(page, *args, **kwargs)

    @classmethod
    def create_content(cls, row, table, view=0, show=None, new_data=None):
        """

        :param show:
        :param new_data:
        :param table:
        :param row:
        :param view:
        :return:
        """
        list_repo = {
            0: cls.ctrl_stock.get_all_table(user=cls.user),
            1: cls.ctrl_supplier.get_all(user=cls.user),
            2: cls.ctrl_user.get_all(user=cls.user),
        }
        base = list_repo[view]
        list_view = ft.ListView(
            controls=[
                AppTable.get_table(
                    data=base.entity["entity_"] if new_data is None else new_data,
                    select=row,
                    table_name=table
                ),
            ],
            spacing=10,
            padding=10,
            auto_scroll=False,
        )
        content = Container(
            border_radius=20,
            padding=ft.padding.all(5),
            margin=ft.margin.all(10),
            expand=True,
            expand_loose=True,
            bgcolor=ft.colors.GREY_50,
            content=list_view,
            adaptive=True,
            data=table,
        )
        return content

    @classmethod
    def create_search(cls, var, new_data=None):
        """

        :param :
        :param :
        :return:
        """
        return Container(
            content=Column(
                [
                    ft.Container(
                        content=Text(
                            "Search", color=ft.colors.GREY_50, weight=ft.FontWeight.BOLD
                        ),
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.BLACK54,
                        margin=10,
                        padding=5,
                        height=30,
                        border=ft.border.only(top=None),
                        border_radius=ft.border_radius.only(top_left=10, top_right=10),
                    ),
                    ft.Container(
                        expand=True,
                        width=400,
                        padding=20,
                        content=ft.Column(
                            controls=[
                                # CAIXAS DA PESQUISA AQUI
                                ft.TextField(label="Produto", width=300, height=30, on_submit=var, data='product_name'),
                                cls.create_panel_search(var) if new_data is None else cls.create_panel_search(var,
                                                                                                              new_data),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ),
                ],
                tight=True,
            ),
            border=ft.border.only(left=None),
            border_radius=ft.border_radius.only(top_left=20, bottom_left=20),
            padding=ft.padding.all(5),
            margin=ft.margin.all(10),
            width=370,
            bgcolor=ft.colors.GREY_50,
        )

    @classmethod
    def create_panel_search(cls, var, new_data=None):
        if new_data is None:
            category = cls.create_category_box(var)
            brand = cls.create_brand_box(var)
            price = cls.create_price_box(var)
        else:
            category = cls.create_category_box(var, new_data)
            brand = cls.create_brand_box(var, new_data)
            price = cls.create_price_box(var, new_data)
        return ft.ExpansionPanelList(
            expand_icon_color=ft.colors.BLACK,
            elevation=7,
            divider_color=ft.colors.AMBER,
            on_change=cls.handle_change,
            expanded_header_padding=15,
            controls=[
                price,
                category,
                brand,
            ],
        )

    @classmethod
    def create_price_box(cls, var, new_data=None):
        groups, counts = None, None
        if new_data is None:
            groups, counts = cls.product_view.get_all_prices()
        else:
            groups, counts = cls.product_view.get_all_prices(new_data)

        top_3_lines = [
            ft.Checkbox(
                label=f"{group.left} - {group.right}  ({count})",
                label_style=ft.TextStyle(color=ft.colors.BLACK),
                on_change=var,
                data='price',
            )
            for group, count in zip(groups, counts)
        ]
        top_3 = ft.ListView(auto_scroll=False, controls=top_3_lines)
        exp = ft.ExpansionPanel(
            bgcolor=ft.colors.GREY_50,
            header=ft.ListTile(
                title=Row(
                    controls=[
                        ft.Text(
                            value="Preço",
                            width=210,
                            height=30,
                            color=ft.colors.BLACK,
                            weight=ft.FontWeight.W_500,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.IconButton(ft.icons.SEARCH_SHARP),
                    ],
                    data='stock',
                    width=100,
                    spacing=0,
                )
            ),
            content=ft.ListTile(
                title=ft.Text("Entre:", color=ft.colors.BLACK),
                subtitle=top_3,
            ),
        )
        return exp

    @classmethod
    def create_category_box(cls, var, new_data=None):
        dict_count_by_category = None
        if new_data is None:
            dict_count_by_category = cls.product_view.get_top_categories()
        else:
            dict_count_by_category = cls.product_view.get_top_categories(new_data)
        top_5_lines = []
        top_5_lines = [
            ft.Checkbox(
                label=f"{category[0]} ({category[1]})",
                label_style=ft.TextStyle(color=ft.colors.BLACK),
                on_change=var,
                data='category',
            )
            for i, category in enumerate(dict_count_by_category.items())
        ]
        top_3 = ft.ListView(auto_scroll=False, controls=top_5_lines)
        exp = ft.ExpansionPanel(
            bgcolor=ft.colors.GREY_50,
            header=ft.ListTile(
                title=Row(
                    controls=[
                        ft.TextField(
                            label="Procure por Categoria", width=200, height=30, on_submit=var, data='category_name'
                        ),
                        ft.IconButton(ft.icons.SEARCH_SHARP),
                    ],
                    data='stock',
                    alignment=ft.MainAxisAlignment.CENTER,
                    width=100,
                )
            ),
            content=ft.ListTile(
                title=ft.Text("Top 5 Categorias", color=ft.colors.BLACK),
                subtitle=top_3,
            ),
        )
        return exp

    @classmethod
    def create_brand_box(cls, var, new_data=None):
        dict_count_by_brand = None
        if new_data is None:
            dict_count_by_brand = cls.product_view.get_top_brands()
        else:
            dict_count_by_brand = cls.product_view.get_top_brands(new_data)
        top_3_lines = []
        top_3_lines = [
            ft.Checkbox(
                label=f"{brand[0]} ({brand[1]})",
                label_style=ft.TextStyle(color=ft.colors.BLACK),
                on_change=var,
                data='brand',
            )
            for count, brand in enumerate(dict_count_by_brand.items())
        ]
        top_3 = ft.ListView(auto_scroll=False, controls=top_3_lines)
        exp = ft.ExpansionPanel(
            bgcolor=ft.colors.GREY_50,
            header=ft.ListTile(
                title=Row(
                    controls=[
                        ft.TextField(label="Procure por Marca", width=200, height=30, on_submit=var, data='brand_name'),
                        ft.IconButton(ft.icons.SEARCH_SHARP),
                    ],
                    data='stock',
                    width=100,
                )
            ),
            content=ft.ListTile(
                title=ft.Text("Top 5 marcas", color=ft.colors.BLACK),
                subtitle=top_3,
            ),
        )
        return exp

    @classmethod
    def handle_change(cls, e: ft.ControlEvent):
        pass

    @classmethod
    def create_page(cls, title: str, body: str):
        """

        :param title:
        :param body:
        :return:
        """
        return Row(
            controls=[
                Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        Card(
                            content=Container(
                                Text(title, weight=ft.FontWeight.BOLD), padding=8
                            )
                        ),
                        Text(body),
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )
