import flet as ft
from flet import Text, Column, Card, Row, Container, UserControl

from App.features.app_table import AppTable
from Views.Product.ListProduct import table_data as db_product
from Views.Supplier.ListSupplier import table_data as db_supplier
from Views.User.ListUser import table_data as db_user
import pandas as pd

list_tables = {
    0: db_product,
    1: db_supplier,
    2: db_user,
}


class AppPages(UserControl):
    """

    """

    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__()
        self.page = page

    @classmethod
    def create_content(cls, view=0):
        """

        :param view:
        :return:
        """
        list_view = ft.ListView(
            controls=[
                AppTable.get_table(list_tables[view]),
            ],
            spacing=10,
            padding=10,
            auto_scroll=False
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
        )
        return content

    @classmethod
    def create_search(cls):
        """

        :param :
        :param :
        :return:
        """
        return Container(
            content=Column([
                ft.Container(
                    content=Text("Search", color=ft.colors.GREY_50, weight=ft.FontWeight.BOLD),
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
                            ft.TextField(label="Produto", width=300, height=30),
                            cls.create_panel_search()
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                )
            ], tight=True),
            border=ft.border.only(left=None),
            border_radius=ft.border_radius.only(top_left=20, bottom_left=20),
            padding=ft.padding.all(5),
            margin=ft.margin.all(10),
            width=370,
            bgcolor=ft.colors.GREY_50,
        )

    @classmethod
    def create_panel_search(cls):
        category = cls.create_category_box()
        brand = cls.create_brand_box()
        price = cls.create_price_box()
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
    def create_price_box(cls):
        data_price = pd.DataFrame.from_dict(data=db_product)
        # Min , max do que vem da base de dados
        min_price = data_price['price'].min()
        max_price = data_price['price'].max()
        avg_price = data_price['price'].mean()

        # calcula como tem que dividir por 5 com base do min, max
        num_groups = round((max_price - min_price) // 5 + avg_price)
        n_groups = int(num_groups)

        # Create bins and labels
        bins = [0, ]
        for i in range(n_groups):
            bins.append(min_price + avg_price * i)
        labels = ['{:.2f}'.format(bins[i]) + '-' + '{:.2f}'.format(bins[i + 1]) for i in range(n_groups - 1)] + [
            f'{bins[-1]}-{max_price}']
        # Add a new column 'price_group' to DataFrame with bin labels
        data_price['price_group'] = pd.cut(data_price['price'], bins=bins, labels=labels, right=False)

        # Group by 'price_group' and count occurrences
        grouped_counts = data_price.groupby('price_group', observed=True).size().reset_index(name='count')
        dict_count_by_price = grouped_counts.to_dict()
        groups, counts = dict_count_by_price['price_group'].values(), dict_count_by_price['count'].values()

        top_3_lines = [ft.Checkbox(label=f"{group} ({count})", label_style=ft.TextStyle(color=ft.colors.BLACK),
                                   on_change=cls.checkbox_changed) for group, count in zip(groups, counts)]
        top_3 = ft.ListView(auto_scroll=False, controls=top_3_lines)
        exp = ft.ExpansionPanel(
            bgcolor=ft.colors.GREY_50,
            header=ft.ListTile(title=Row(
                controls=[ft.Text(value="Preço", width=210, height=30,
                                  color=ft.colors.BLACK, weight=ft.FontWeight.W_500, text_align=ft.TextAlign.CENTER),
                          ft.IconButton(ft.icons.SEARCH_SHARP)],
                width=100,
                spacing=0,
            )),
            content=ft.ListTile(
                    title=ft.Text("Entre:", color=ft.colors.BLACK),
                    subtitle=top_3,
            ))
        return exp

    @classmethod
    def create_category_box(cls):
        data_category = pd.DataFrame.from_dict(data=db_product)
        count_by_category = data_category.groupby('name_2')['name_2'].count().head(5)
        dict_count_by_category = [count_by_category.to_dict()]
        top_3_lines = []
        for e in dict_count_by_category:
            top_3_lines = [ft.Checkbox(label=f"{category} ({e[category]})",
                                       label_style=ft.TextStyle(color=ft.colors.BLACK),
                                       on_change=cls.checkbox_changed) for count, category in enumerate(e)]
        top_3 = ft.ListView(auto_scroll=False, controls=top_3_lines)
        exp = ft.ExpansionPanel(
            bgcolor=ft.colors.GREY_50,
            header=ft.ListTile(title=Row(
                controls=[ft.TextField(label="Procure por Categoria", width=200, height=30),
                          ft.IconButton(ft.icons.SEARCH_SHARP)],
                alignment=ft.MainAxisAlignment.CENTER,
                width=100,
            )),
            content=ft.ListTile(
                title=ft.Text("Top 5 Categorias", color=ft.colors.BLACK),
                subtitle=top_3,
            ))
        return exp

    @classmethod
    def create_brand_box(cls):
        data_brand = pd.DataFrame.from_dict(data=db_product)
        count_by_brand = data_brand.groupby('name_1')['name_1'].count().head(5)
        dict_count_by_brand = [count_by_brand.to_dict()]
        top_3_lines = []
        for e in dict_count_by_brand:
            top_3_lines = [ft.Checkbox(label=f"{brand} ({e[brand]})",
                                       label_style=ft.TextStyle(color=ft.colors.BLACK),
                                       on_change=cls.checkbox_changed) for count, brand in enumerate(e)]
        top_3 = ft.ListView(auto_scroll=False, controls=top_3_lines)
        exp = ft.ExpansionPanel(
            bgcolor=ft.colors.GREY_50,
            header=ft.ListTile(title=Row(
                controls=[ft.TextField(label="Procure por Marca", width=200, height=30),
                          ft.IconButton(ft.icons.SEARCH_SHARP)],
                width=100,
            )),
            content=ft.ListTile(
                title=ft.Text("Top 5 marcas", color=ft.colors.BLACK),
                subtitle=top_3,
            ))
        return exp

    @classmethod
    async def checkbox_changed(cls, e):
        pass
        # await t.update_async()

    def handle_change(e: ft.ControlEvent):
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
                        Card(content=Container(Text(title, weight=ft.FontWeight.BOLD), padding=8)),
                        Text(body),
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )
