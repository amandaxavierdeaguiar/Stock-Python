import flet as ft
from flet import Text, Column, UserControl, icons, Control, IconButton, colors

from App.app_pages import AppPages
from App.features.app_menu import AppMenu
from App.app_auth import AppAuth
from Views.Product.ListProduct import table_data as db_product
from Views.Supplier.ListSupplier import table_data as db_supplier
from Views.User.ListUser import table_data as db_user

list_tables = {
    0: db_product,
    1: db_supplier,
    2: db_user,
}


class AppLayout(UserControl):
    """

    """
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.app_menu = AppMenu(self.page)
        self.app_pages = AppPages(self.page)

        pages = [
            (
                self.app_menu.create_menu_btn(label_='Stock', icon_=icons.WAREHOUSE_OUTLINED),
                self.app_pages.create_content(0),
            ),
            (
                self.app_menu.create_menu_btn(label_='Supplier', icon_=icons.PERSON_2),
                self.app_pages.create_content(1),
            ),
            (
                self.app_menu.create_menu_btn(label_='User', icon_=icons.PERSON),
                self.app_pages.create_content(2),
            ),
        ]

        self.navigation_items = [navigation_item for navigation_item, _ in pages]
        self.navigation_rail = self.app_menu.build_navigation_rail(self._navigation_change)
        self.update_destinations()
        self._menu_extended = True
        self.navigation_rail.extended = True

        self.menu_panel = self.app_menu.get_menu(self.navigation_rail)
        self.search_panel = self.app_pages.create_search()

        page_contents = [page_content for _, page_content in pages]
        self.content_area = Column(controls=page_contents, expand=True)

        self.toggle_menu_panel = IconButton(
            icon=icons.ARROW_CIRCLE_LEFT, icon_color=colors.BLUE_GREY_400, selected=False,
            selected_icon=icons.ARROW_CIRCLE_RIGHT, on_click=self.toggle_menu_panel)

        self.toggle_search_panel = IconButton(
            icon=icons.ARROW_CIRCLE_RIGHT, icon_color=colors.BLUE_GREY_400, selected=True,
            selected_icon=icons.ARROW_CIRCLE_LEFT, on_click=self.toggle_search_panel)

        self._active_view: Control = Column(controls=[
            Text("")
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        self.set_content()
        self._change_displayed_page()

    def select_page(self, page_number):
        self.navigation_rail.selected_index = page_number
        self._change_displayed_page()

    def _navigation_change(self, e):
        self._change_displayed_page()
        self.page.update()

    def _change_displayed_page(self):
        page_number = self.navigation_rail.selected_index
        for i, content_page in enumerate(self.content_area.controls):
            # update selected page
            content_page.visible = page_number == i

    def update_destinations(self):
        self.navigation_rail.destinations = self.navigation_items
        self.navigation_rail.label_type = ft.NavigationRailLabelType.ALL,

    def set_content(self, panel_=None):
        self.controls = [self.menu_panel, self.toggle_menu_panel, self.active_view,
                         self.content_area, self.toggle_search_panel, self.search_panel]
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
