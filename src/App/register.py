import flet as ft
from flet import Page

class Register():
    def __init__(self, page: Page):
        self.page = page
        self.create_user =  ft.TextField(label="Digite o Nome:", width=300, prefix_icon=ft.icons.PERSON)
        self.create_login = ft.TextField(label="Digite o Login:", width=300, prefix_icon=ft.icons.EMAIL)
        self.create_password = ft.TextField(label="Digite a Password:",width=300, password=True,can_reveal_password=True, prefix_icon=ft.icons.LOCK)
        self.check_password = ft.TextField(label="Repita a Password:",width=300, password=True,can_reveal_password=True, prefix_icon=ft.icons.LOCK)

        self.create_type_acess = ft.Dropdown(
            options=[
                ft.dropdown.Option("Admin"),
                ft.dropdown.Option("Sub_Admin"),
                ft.dropdown.Option("User"),
            ],
            width=300,
        )
        
        self.button_register_user: ft.ElevatedButton = ft.ElevatedButton(
            text='Cadastro',
            width=140,
        )
        
        
    def create_user_(self) -> None: #, e: ft.ControlEvent
        login_page = ft.Container( 
                width=400, 
                height=450, 
                padding=50, 
                border_radius=20, 
                bgcolor="white", 
                content=ft.Column( 
                    controls=[ ft.Column( 
                        controls=[
                            self.create_user,
                            self.create_login,
                            self.create_password, 
                            self.check_password, 
                            self.create_type_acess,
                            self.button_register_user,
                            ], 
                        alignment=ft.MainAxisAlignment.CENTER, 
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                        ), 
                        ], 
                    ) 
                ) 

        return login_page
    
