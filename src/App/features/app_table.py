import flet as ft
from flet import Container, UserControl


class AppTable(UserControl):
    """

    """
    def __init__(self, app, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._table = self.build()
        self.app_layout = app
        self.page = page
        # self._table = self.get_table()

    @classmethod
    def get_table(cls, data=None):
        """

        :param data:
        :return:
        """
        col = [ft.DataColumn(label=ft.Text(column.replace("_", " ").capitalize()),
                             on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                             visible=True) for column in data[0].keys()]
        line = []
        cells = []
        color = ["#ffffff", "#f2f2f2"]
        for j, row in enumerate(data):
            for keys, values in enumerate(row, j):
                cells.append(ft.DataCell(ft.Text(value=row[values]), visible=True))
            line.append(ft.DataRow(cells=cells.copy(), color=color[j % 2], selected=True, visible=True,
                                   on_select_changed=lambda e: print(f"row select changed: {e.data}")))
            cells.clear()
        return ft.DataTable(
            data_row_color={ft.MaterialState.HOVERED: ft.colors.BLUE_GREY_300},
            data_text_style=ft.TextStyle(color=ft.colors.BLACK),
            border_radius=20,
            sort_column_index=0,
            sort_ascending=False,
            heading_row_height=30,
            heading_row_color=ft.colors.BLACK54,
            show_checkbox_column=False,
            divider_thickness=0,
            column_spacing=40,
            columns=col,
            rows=line,
            show_bottom_border=True,
        )

    def build(self):
        return Container(
            expand=True,
            content=self.get_table()
        )

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, new_table):
        self._table = new_table
        self.update()
