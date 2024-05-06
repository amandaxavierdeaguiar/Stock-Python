import flet as ft

from app.app_style import read_only_textfield, dropbox


def get_TextField(txt_value=None, txt_label=None):
    """

    :param txt_value:
    :param txt_label:
    :return:
    """
    return ft.TextField(
        **read_only_textfield(),
        value=txt_value,
        label=txt_label,
    )


def get_dropdown(label, list=None):
    """

    :param label:
    :param list:
    :return:
    """
    drop = ft.Dropdown(
        **dropbox(),
        label=label,
    )
    for elem in list:
        drop.options.append(ft.dropdown.Option(elem))
    return drop


def get_text(value=None):
    """

    :param value:
    :return:
    """
    return ft.TextField(
        **read_only_textfield(),
        value=value,
        multiline=True,
        max_lines=3)


def get_image(value=None):
    return ft.Image(
        src=f"products/{value}",
        width=150,
        height=150,
        fit=ft.ImageFit.CONTAIN,
    )
