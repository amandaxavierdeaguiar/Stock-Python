import flet as ft
from flet import Text, Column, icons, Control, IconButton, colors

from app.app_pages import AppPages
from app.features.app_menu import AppMenu
from app.features.app_product_description import ProductDescription
from shared.Base.SharedControls import SharedControls
from views.Product.ProductView import ProductView


class AppLayout(SharedControls):
    """ """

    product_details: ft.BottomSheet
    app_product_description = ProductDescription()
    product_view = ProductView()

    def __init__(self, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.details()
        self.app_menu = AppMenu(self.page)
        self.app_pages = AppPages(self.page, self.user)

        pages = [
            (
                self.app_menu.create_menu_btn(
                    label_="Stock", icon_=icons.WAREHOUSE_OUTLINED
                ),
                self.app_pages.create_content(
                    view=0, row=self.row_selected, table="Stock"
                ),
            ),
            (
                self.app_menu.create_menu_btn(label_="Supplier", icon_=icons.PERSON_2),
                self.app_pages.create_content(
                    view=1, row=self.row_selected, table="Supplier"
                ),
            ),
            (
                self.app_menu.create_menu_btn(label_="User", icon_=icons.PERSON),
                self.app_pages.create_content(
                    view=2, row=self.row_selected, table="User"
                ),
            ),
        ]

        self.navigation_items = [navigation_item for navigation_item, _ in pages]
        self.navigation_rail = self.app_menu.build_navigation_rail(
            self._navigation_change
        )
        self.update_destinations()
        self._menu_extended = True
        self.navigation_rail.extended = True

        self.menu_panel = self.app_menu.get_menu(self.navigation_rail)
        self.search_panel = self.app_pages.create_search(self.checkbox_changed)

        page_contents = [page_content for _, page_content in pages]
        self.content_area = Column(controls=page_contents, expand=True)

        self.toggle_menu_panel = IconButton(
            icon=icons.ARROW_CIRCLE_LEFT,
            icon_color=colors.BLUE_GREY_400,
            selected=False,
            selected_icon=icons.ARROW_CIRCLE_RIGHT,
            on_click=self.toggle_menu_panel,
        )

        self.toggle_search_panel = IconButton(
            icon=icons.ARROW_CIRCLE_RIGHT,
            icon_color=colors.BLUE_GREY_400,
            selected=True,
            selected_icon=icons.ARROW_CIRCLE_LEFT,
            on_click=self.toggle_search_panel,
        )

        self._active_view: Control = Column(
            controls=[Text("")],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        self.set_content()
        self._change_displayed_page()

    @classmethod
    async def checkbox_changed(cls, e):
        list_tables = {
            "price": 'Stock',
            "category": 'Stock',
            "brand": 'Stock',
        }
        table = list_tables[e.control.data]
        field = e.control.data
        label, qnt = e.control.label.split('(')
        label = label.replace(' ', '')
        cls.product_view.search(table, label, field)
        print()

    @classmethod
    async def row_selected(cls, event):
        col_names = {
            "Stock": ["product_name", "product_bar_cod", "supplier_name", "quantity"],
            "Supplier": ["name", "address", "phone", "email"],
            "User": ["name", "login", "password", "typeAccess"],
        }
        selected = {}
        for cells, col_name in zip(event.control.cells, col_names[event.control.data]):
            selected[col_name] = cells.content.value
        await cls.show_bs(selected, event.control.data)

    @classmethod
    def details(cls):
        cls.product_details = ft.BottomSheet(
            open=False,
            on_dismiss=cls.bs_dismissed,
            elevation=0.7,
            maintain_bottom_view_insets_padding=True,
            use_safe_area=True,
        )

    @classmethod
    def bs_dismissed(cls, e):
        print("Dismissed!")

    @classmethod
    async def close_bs(cls, e):
        cls.product_details.open = False
        await cls.product_details.update_async()

    @classmethod
    async def show_bs(cls, selected, table):
        # Alterar o description do Supplier e do User
        details = {
            "Stock": cls.app_product_description.get_content(selected),
            "Supplier": cls.app_product_description.get_content(selected),
            "User": cls.app_product_description.get_content(selected),
        }
        content = details[table]
        cls.product_details.content = content
        cls.product_details.open = True
        await cls.product_details.update_async()

    # happens when example is added to the page (when user chooses the BottomSheet control from the grid)
    def did_mount(self):
        self.page.overlay.append(self.product_details)
        self.page.update()

    # happens when example is removed from the page (when user chooses different control group on the navigation rail)
    def will_unmount(self):
        self.page.overlay.remove(self.product_details)
        self.page.update()

    # def select_page(self, page_number):
    #     self.navigation_rail.selected_index = page_number
    #     self._change_displayed_page()

    def _navigation_change(self, e):
        self._change_displayed_page()
        # self.content_area.update()
        # self.page.update()

    def _change_displayed_page(self):
        page_number = self.navigation_rail.selected_index
        for i, content_page in enumerate(self.content_area.controls):
            # update selected page
            content_page.visible = page_number == i
            # self.content_area.update()
            self.page.update()

    def update_destinations(self):
        self.navigation_rail.destinations = self.navigation_items
        self.navigation_rail.label_type = (ft.NavigationRailLabelType.ALL,)

    def set_content(self, panel_=None):
        self.controls = [
            self.menu_panel,
            self.toggle_menu_panel,
            self.active_view,
            self.content_area,
            self.toggle_search_panel,
            self.search_panel,
            self.product_details,
        ]
        self.update_destinations()
        self.navigation_rail.extended = self._menu_extended
        if panel_:
            self.menu_panel.visible = panel_
            self.search_panel.visible = False
        return self.controls

    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.update()

    def toggle_menu_panel(self, e):
        self.menu_panel.visible = not self.menu_panel.visible
        self.toggle_menu_panel.selected = not self.toggle_menu_panel.selected
        self.page.update()

    def toggle_search_panel(self, e):
        self.search_panel.visible = not self.search_panel.visible
        self.toggle_search_panel.selected = not self.toggle_search_panel.selected
        self.page.update()
