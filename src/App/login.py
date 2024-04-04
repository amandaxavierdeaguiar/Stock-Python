import flet as ft
from flet import Text, Column, colors, icons, IconButton, Control, Row, Container
from App.register import Register

class Login(Row):
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.txt_username = ft.TextField(label="Digite seu Login", width=300, prefix_icon=ft.icons.EMAIL)
        self.txt_password = ft.TextField(label="Digite sua Password", width=300, password=True,can_reveal_password=True, prefix_icon=ft.icons.LOCK)
        self.button_register = ft.ElevatedButton("Cadastra-se!", on_click=self.registerbtn)
        self.button_enter = ft.ElevatedButton("Entre", on_click=lambda _: print("Button clicked!"))
        self.register = Register()
    
    def create_container(self) -> ft.Container:
        image = ft.Image(src="icons/login.png", width=150, height=150)

        c = ft.Container(
            width=400,
            height=450,
            padding=20,
            border_radius=20,
            bgcolor="white",
            content=ft.Column(
                controls=[
                    image, 
                    self.txt_username,
                    self.txt_password,
                    self.button_enter, 
                    self.button_register,          
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            ),
        )

        return c
    

    def registerbtn(self):
        pass
        #self.register = Register(self.page)

