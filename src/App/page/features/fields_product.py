import flet as ft

from app.app_style import read_only_textfield, dropbox


def get_text_field(txt_value=None, txt_label=None, size=False, write=False):
    """

    :param write:
    :param size:
    :param txt_value:
    :param txt_label:
    :return:
    """
    return ft.TextField(
        **read_only_textfield(write, size),
        value=txt_value,
        label=txt_label,
    )


def get_dropdown(label, disabled_=False, list=None):
    """

    :param disabled_:
    :param label:
    :param list:
    :return:
    """
    drop = ft.Dropdown(
        **dropbox(),
        label=label,
        disabled=disabled_,
    )
    for elem in list:
        txt = None
        if elem == 'weight':
            txt = 'Peso'
        elif elem == 'unit':
            txt = 'Unidade'
        else:
            txt = elem
        drop.options.append(ft.dropdown.Option(key=elem, text=txt))
    return drop


def get_text(value=None, write=False):
    """

    :param value:
    :return:
    """
    return ft.TextField(
        **read_only_textfield(write),
        value=value,
        multiline=True,
        max_lines=3)


def get_image(value=None):
    return ft.Image(
        src=f"products/{value}",
        width=150,
        height=150,
        fit=ft.ImageFit.CONTAIN,
        data=value
    )
