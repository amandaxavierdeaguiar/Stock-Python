import flet as ft
from flet import Text, Column, Card, Row, Container

from app.page.features.search import Search
from app.page.features.table import Table
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
                Table.get_table(
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
    def create_search(cls, var, table, new_data=None):
        """

        :param :
        :param :
        :return:
        """
        return Container(content=Search.get_panel(var, table),
                         expand=True,
                         expand_loose=True,
                         border=ft.border.only(left=None),
                         border_radius=ft.border_radius.only(top_left=20, bottom_left=20),
                         padding=ft.padding.all(5),
                         margin=ft.margin.all(10),
                         width=370,
                         bgcolor=ft.colors.GREY_50, )

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
