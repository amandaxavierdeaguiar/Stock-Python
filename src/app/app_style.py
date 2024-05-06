import flet as ft

WIDTH = 400


def read_only_textfield():
    return {
        "read_only": True,
        "color": ft.colors.BLACK,
        "border_color": ft.colors.BLACK,
        "bgcolor": ft.colors.WHITE,
        "focused_border_color": ft.colors.BLUE_400,
        "width": WIDTH
    }


def dropbox():
    return {
        "color": ft.colors.BLACK,
        "border_color": ft.colors.BLACK,
        "bgcolor": ft.colors.WHITE,
        "focused_bgcolor": ft.colors.GREY_200,
        "width": WIDTH / 2 - 5
    }


def text():
    return {
        "color": ft.colors.BLACK,
        "bgcolor": ft.colors.WHITE,
    }


def title():
    return {
        "size": 30,
        "color": ft.colors.BLUE_900,
    }


def data_theme():
    return {
        "border_radius": 20,
        "sort_column_index": 0,
        "sort_ascending": False,
        "heading_row_height": 30,
        "heading_row_color": ft.colors.BLACK54,
        "show_checkbox_column": False,
        "divider_thickness": 0,
        "column_spacing": 40,
        "columns": "col",
        "rows": "line",
        "show_bottom_border": True,
    }


def page_theme():
    return {
        "page.fonts": {
            "font_title": "assets/fonts/coolvetica rg.otf",
        },
        "page.theme": ft.Theme(font_family="font_title"),
    }


def title_pg():
    return {
        "size": 30,
        "color": ft.colors.AMBER_ACCENT_700,
    }


def button():
    return {
        "style": ft.ButtonStyle(
            shape=ft.ContinuousRectangleBorder(radius=30),
            color={
                ft.MaterialState.DEFAULT: ft.colors.BLACK,
                ft.MaterialState.HOVERED: ft.colors.WHITE,
            },
            bgcolor={
                ft.MaterialState.DEFAULT: ft.colors.YELLOW,
                ft.MaterialState.HOVERED: ft.colors.AMBER_600,
            },
            elevation={"pressed": 0, "": 1},
            animation_duration=150,
        ),
    }
