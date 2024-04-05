import flet as ft
import base64
from flet import Text, Column, colors, icons, IconButton, Control, Row, Container, Image, ImageFit

class ProductDescription():    
    def __init__(self, page: ft.Page):
        self.page = page
        page.title = 'Produtos'
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.bgcolor=ft.colors.BLUE_500

        #Colocar título
        self.title_product = ft.Text("Descrição do produto", size = 30, color=colors.BLUE_900)
    
        # TextField nome do Produto
        # Pegar da database
        product_bd = 'Alho Poró'
        self.txt_name_product = ft.TextField(
            label='Nome do Produto',
            width=450,
            disabled=True,
            value=product_bd,
            )
        
        # TextField Valor do Produto
        price_bd = '2.90'
        self.txt_price = ft.TextField(
            label='Valor do Produto',
            width=450,
            disabled=True,
            value=price_bd,
            )
        
        # TextField Categoria
        category_bd = 'Legumes'
        self.c = ft.TextField(
            label='Categoria',
            width=220,
            disabled=True,
            value=category_bd,
            )
            
        # TextField Categoria
        brand_db = 'Marca Própria'
        self.b = ft.TextField(
            label='Marca',
            width=220,
            disabled=True,
            value=brand_db,
            )
        
        # Descrição do Produto
        #self.description_product = ft.TextField(label="Descrição do produto", multiline=True, max_lines=3)
        self.description_db = 'O Alho Francês (Allium ampeloprasum) é um dos membros da família das cebolas. Tem uma forma cilíndrica, alargando-se em folhas que crescem sobrepostas umas nas outras. É constituído por uma parte branca - o fuste (zona subterrânea) - que é a mais usada na culinária (guisados, tartes e gratinados), e uma parte verde (folhas aéreas) que deve ser aproveitada, por exemplo, na preparação de sopas.'
        self.description_product = ft.TextField(
            label="Descrição do produto", 
            multiline=True,
            width=450, 
            height=500,
            max_lines=10,
            disabled=True,
            value=self.description_db,
            )  
        
        self.button_enter = ft.ElevatedButton("Edite o produto", on_click=lambda _: print("Insiriu o produto na Base de Dados"))
        
        self.image_insert_product = ft.Image(src=f"products/alho_frances.png",width=200, height=200, fit=ft.ImageFit.CONTAIN)

        page.add(
                ft.Container(
                    width=720,
                    height=500,
                    padding=10,
                    border_radius=20,
                    bgcolor="white",
                    content=ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Column(
                                        controls=[
                                            #image_holder,
                                        ],
                                        #alignment=ft.MainAxisAlignment.CENTER,
                                        #horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                                        spacing=5,
                                    ),
                                    ft.Column(width=200, height=400,
                                        controls=[
                                            self.image_insert_product,
                                            self.button_enter
                                        ],
                                        spacing=20,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                                    ),
                                ],
                                alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=20,
                            ),
                            ft.Column(width=30,
                                controls=[
                                ],
                                #alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Column(
                                        controls=[
                                            self.title_product,
                                            self.txt_name_product,
                                            self.txt_price,
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                       controls=[
                                            self.b,
                                            self.c,
                                        ], 
                                       alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Column(
                                        controls=[
                                            self.description_product,
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        #horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        ],
                    ),
                ),
            ),  
        
if __name__ == '__main__':
    
    ft.app(target=ProductDescription, assets_dir="./assets")
