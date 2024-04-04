import flet as ft
from flet import Text, Column, colors, icons, IconButton, Control, Row, Container
from App.sidebar import Sidebar
from App.login import Login
from App.register import Register
#from App.product_new import ProductNew
from App.product_new1 import ProductNew
class AppLayout(Row):
    def __init__(self, app, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        self.toggle_nav_rail_button = IconButton(
            icon=icons.ARROW_CIRCLE_LEFT, icon_color=colors.BLUE_GREY_400, selected=False,
            selected_icon=icons.ARROW_CIRCLE_RIGHT, on_click=self.toggle_nav_rail)
        self.sidebar = Sidebar(self, page)
        self._active_view: Control = Column(controls=[
            Text("")
        ], alignment=ft.alignment.center, horizontal_alignment=ft.alignment.center, expand=True)
        
        #self.content = ProductNew().products_new(page) #add
        #self.content = ProductNew2()
        #self.content = Register().create_user_()
        #self.content = Register(page)
        self.content = Login().create_container()
        
        """self.content = Container(
         
            width=500,
            height=500,
            alignment=ft.alignment.center,
            margin=ft.margin.all(30),
            bgcolor=ft.colors.BLUE,
            content=Text("Login")
        )"""
        
        self.controls = [self.sidebar,
                         self.toggle_nav_rail_button, self.active_view, self.content]


    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.update()

    def toggle_nav_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        self.page.update()

