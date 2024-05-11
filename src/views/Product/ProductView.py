import random

import numpy as np
import pandas as pd

from controllers.BrandController import BrandController
from controllers.CategoryController import CategoryController
from controllers.ProductController import ProductController
from controllers.ProductHistoryController import ProductHistoryController
from controllers.StockController import StockController
from controllers.StockHistoryController import StockHistoryController
from controllers.SupplierController import SupplierController
from controllers.UserController import UserController
from models.product.dto.Product import ProductDto
from models.stock.dto.StockDto import StockDto
from shared.base.SharedControls import SharedControls
from temp import ListProduct


class ProductView(SharedControls):
    ctrl_category = CategoryController()
    ctrl_supplier = SupplierController()
    ctrl_user = UserController()
    ctrl_brand = BrandController()
    ctrl_product = ProductController()
    ctrl_stock = StockController()
    ctrl_history_stock = StockHistoryController()
    ctrl_history_product = ProductHistoryController()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.new_product()
        self.new_stock()
        # self.new_from_list_product()

    @classmethod
    def search(cls, search):
        details = {
            "Stock": cls.ctrl_stock.get_search(search, cls.user),
            "Supplier": cls.ctrl_supplier,
            "User": cls.ctrl_user,
        }
        return details[search['table']]

    @classmethod
    def get_top_categories(cls, new_data=None):
        if new_data is None:
            new_data = cls.ctrl_product.get_all(cls.user)
        entities = [e.dict() for e in new_data.entity["entity_"]]
        data_category = pd.DataFrame.from_dict(data=entities)
        count_by_category = (data_category.groupby("category_name")["category_name"]
                             .count().sort_values(na_position='last', ascending=False).head(5))
        sorted_count_by_category = sorted(count_by_category.to_dict().items(), key=lambda x: x[1], reverse=True)
        dict_count_by_category = dict(sorted_count_by_category)
        return dict_count_by_category

    @classmethod
    def get_all_categories(cls):
        base = cls.ctrl_product.get_all(cls.user)
        entities = [e.dict() for e in base.entity["entity_"]]
        data_category = pd.DataFrame.from_dict(data=entities)
        return data_category['category_name'].unique()

    @classmethod
    def get_all_brands(cls):
        base = cls.ctrl_product.get_all(cls.user)
        entities = [e.dict() for e in base.entity["entity_"]]
        data_brand = pd.DataFrame.from_dict(data=entities)
        return data_brand["brand_name"].unique()

    @classmethod
    def get_top_brands(cls, new_data=None):
        if new_data is None:
            new_data = cls.ctrl_product.get_all(cls.user)
        entities = [e.dict() for e in new_data.entity["entity_"]]
        data_brand = pd.DataFrame.from_dict(data=entities)
        count_by_brand = (data_brand.groupby("brand_name")["brand_name"]
                          .count().sort_values(na_position='last', ascending=False).head(5))
        sorted_count_by_brand = sorted(count_by_brand.to_dict().items(), key=lambda x: x[1], reverse=True)
        dict_count_by_brand = dict(sorted_count_by_brand)
        return dict_count_by_brand

    @classmethod
    def get_all_prices(cls, new_data=None):
        if new_data is None:
            new_data = cls.ctrl_product.get_all(cls.user)
        entities = [e.dict() for e in new_data.entity["entity_"]]
        data_price = pd.DataFrame.from_dict(data=entities)
        # Min , max do que vem da base de dados
        min_price = data_price["price"].min()
        max_price = data_price["price"].max()

        # calcula como tem que dividir por 5 com base do min, max
        num_groups = round((max_price - min_price) // 5)
        n_groups = int(num_groups)

        if len(entities) <= 1:
            data_price["price_group"] = pd.qcut(data_price["price"], q=1)
        else:
            data_price["price_group"] = pd.qcut(data_price["price"], q=5)

        # Group by 'price_group' and count occurrences
        grouped_counts = (
            data_price.groupby("price_group", observed=True)
            .size()
            .reset_index(name="count")
        )
        dict_count_by_price = grouped_counts.to_dict()
        groups, counts = (
            dict_count_by_price["price_group"].values(),
            dict_count_by_price["count"].values(),
        )
        return groups, counts

    @classmethod
    def get_history_prices(cls, name=None):
        base = cls.ctrl_history_product.get_by_name(name, cls.user)
        entities = [e.dict() for e in base.entity["entity_"]]
        data_price = pd.DataFrame.from_dict(data=entities).sort_values(by=["date"])
        data_price["date"] = pd.to_datetime(data_price["date"], format="%Y-%m-%d %H:%M")
        prices = data_price["price"].tolist()
        data = {
            "min": np.min(data_price["price"]) - 75,
            "max": np.max(data_price["price"]),
            "y": data_price["price"],
            "x": data_price["date"],
            "length": len(data_price),
            "values": prices,
            "name": "Preços"
        }
        return data

    @classmethod
    def get_history_quantity(cls, name=None):
        base = cls.ctrl_history_stock.get_by_name(name, cls.user)
        entities = [e.dict() for e in base.entity["entity_"]]
        data_quantity = pd.DataFrame.from_dict(data=entities).sort_values(by=["date"])
        quantities = data_quantity["quantity"].tolist()
        data = {
            "min": np.min(data_quantity["quantity"]) - 75,
            "max": np.max(data_quantity["quantity"]),
            "y": data_quantity["quantity"],
            "x": data_quantity["date"],
            "length": len(data_quantity),
            "values": quantities,
            "name": "Quantidades"
        }
        return data

    @classmethod
    def get_product(cls, selected):
        base = cls.ctrl_product.get_by_name(selected)
        return base.entity["entity_"]

    def new_product(self):
        """
        metodo que cria uma alteração do preço de um certo produto escolhido de forma random
        :return:
        """
        base = self.ctrl_product.get_all(self.user)
        product = random.choice(base.entity["entity_"])
        product_dto = ProductDto.model_validate(product)
        op = random.randint(0, 1)
        if op == 0:
            product_dto.price = "{:.4f}".format(product_dto.price - (product_dto.price * random.uniform(0, 0.50)))
        elif op == 1:
            product_dto.price = "{:.4f}".format(product_dto.price + (product_dto.price * random.uniform(0, 0.50)))
        self.ctrl_product.update(product_dto, self.user)

    def new_stock(self):
        """
        metodo que cria uma alteração a quantidade em stock de um certo produto que escolhe random
        :return:
        """
        base = self.ctrl_stock.get_all(self.user)
        stock = random.choice(base.entity["entity_"])
        stock_dto = StockDto.model_validate(stock)
        op = random.randint(0, 1)
        if op == 0:
            stock_dto.quantity = "{:.4f}".format(stock_dto.quantity - (stock_dto.quantity * random.uniform(0, 0.25)))
        elif op == 1:
            stock_dto.quantity = "{:.4f}".format(stock_dto.quantity + (stock_dto.quantity * random.uniform(0, 0.25)))
        self.ctrl_stock.update(stock_dto, self.user)

    def new_from_list_product(self):
        """
        Metodo para adicionar novos produtos e o seu registo no stock que estejam no ficheiro ListProduct da pasta temp
        :return:
        """
        list_product = ListProduct.table_data
        for product in list_product:
            product_dto = ProductDto.model_validate(product)
            base = self.ctrl_product.add(product_dto, self.user)
            new_stock = {
                'product_name': product_dto.name,
                'product_bar_cod': product_dto.bar_cod,
                'supplier_name': 'Proprio',
                'quantity': random.randint(1, 1000),
            }
            stock_dto = StockDto.model_validate(new_stock)
            self.ctrl_stock.add(stock_dto, self.user)
