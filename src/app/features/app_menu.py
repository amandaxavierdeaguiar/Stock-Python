import flet as ft
from flet import (Column, Container, Row, Text, NavigationRail, NavigationRailDestination,
                  border_radius, colors, padding, margin)

from shared.Base.SharedControls import SharedControls


class AppMenu(SharedControls):
    def __init__(self, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page

    @classmethod
    def get_menu(cls, controls_):
        return Container(
            content=Column([
                Row(
                    controls=[
                        Text("Menu",
                             color=ft.colors.BLACK,
                             weight=ft.FontWeight.BOLD)
                    ], alignment=ft.MainAxisAlignment.CENTER
                ),
                cls.divider(),
                controls_,
                cls.divider(),
            ], tight=True),
            padding=padding.all(10),
            margin=margin.all(0),
            width=170,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
        )

    @classmethod
    def create_menu_btn(cls, label_, icon_, type_=None):
        return NavigationRailDestination(
            label_content=Text(label_, color=ft.colors.BLACK),
            label=label_,
            icon=icon_,
            selected_icon=icon_,
        )

    @classmethod
    def build_navigation_rail(cls, var_on_change, type_=None):
        if type_ == 'login':
            return NavigationRail(
                selected_index=0,
                label_type=ft.NavigationRailLabelType.ALL,
                on_change=var_on_change,
                bgcolor=colors.LIGHT_BLUE_ACCENT_700,
                expand=True,
                visible=False,
            )
        else:
            return NavigationRail(
                selected_index=0,
                label_type=ft.NavigationRailLabelType.ALL,
                on_change=var_on_change,
                bgcolor=colors.LIGHT_BLUE_ACCENT_700,
                expand=True,
            )

    def update_destinations(self):
        pass

    @classmethod
    def divider(cls):
        return Container(
            bgcolor=colors.BLACK26,
            border_radius=border_radius.all(30),
            height=1,
            width=150,
        )
