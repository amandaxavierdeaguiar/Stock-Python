import random

import numpy as np
import pandas as pd

from controllers.BrandController import BrandController
from controllers.CategoryController import CategoryController
from controllers.ProductController import ProductController
from controllers.ProductHistoryController import ProductHistoryController
from controllers.StockController import StockController
from controllers.StockHistoryController import StockHistoryController
from models.product.dto.Product import ProductDto
from models.stock.dto.StockDto import StockDto
from shared.Base.SharedControls import SharedControls


class ProductView(SharedControls):
    ctrl_category = CategoryController()
    ctrl_brand = BrandController()
    ctrl_product = ProductController()
    ctrl_stock = StockController()
    ctrl_history_stock = StockHistoryController()
    ctrl_history_product = ProductHistoryController()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.new_product()
        self.new_stock()

    @classmethod
    def get_all_categories(cls):
        base = cls.ctrl_product.get_all(cls.user)
        entities = [e.dict() for e in base.entity["entity_"]]
        data_category = pd.DataFrame.from_dict(data=entities)
        count_by_category = (
            data_category.groupby("category_id")["category_id"].count().head(5)
        )
        dict_count_by_category = [count_by_category.to_dict()]
        return dict_count_by_category

    @classmethod
    def get_all_brands(cls):
        base = cls.ctrl_brand.get_all(cls.user)
        entities = [e.dict() for e in base.entity["entity_"]]
        data_brand = pd.DataFrame.from_dict(data=entities)
        count_by_brand = data_brand.groupby("name")["name"].count().head(5)
        dict_count_by_brand = [count_by_brand.to_dict()]
        return dict_count_by_brand

    @classmethod
    def get_all_prices(cls):
        base = cls.ctrl_product.get_all(cls.user)
        entities = [e.dict() for e in base.entity["entity_"]]
        data_price = pd.DataFrame.from_dict(data=entities)
        # Min , max do que vem da base de dados
        min_price = data_price["price"].min()
        max_price = data_price["price"].max()
        avg_price = data_price["price"].mean()

        # calcula como tem que dividir por 5 com base do min, max
        num_groups = round((max_price - min_price) // 5 + avg_price)
        n_groups = int(num_groups)

        # Create bins and labels
        bins = [
            0,
        ]
        for i in range(n_groups):
            bins.append(min_price + avg_price * i)
        labels = [
                     "{:.2f}".format(bins[i]) + "-" + "{:.2f}".format(bins[i + 1])
                     for i in range(n_groups - 1)
                 ] + [f"{bins[-1]}-{max_price}"]
        # Add a new column 'price_group' to DataFrame with bin labels
        data_price["price_group"] = pd.cut(
            data_price["price"], bins=bins, labels=labels, right=False
        )

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
        }
        return data

    @classmethod
    def get_product(cls, selected):
        base = cls.ctrl_product.get_by_name(selected)
        return base.entity["entity_"]

    def new_product(self):
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
        base = self.ctrl_stock.get_all(self.user)
        stock = random.choice(base.entity["entity_"])
        stock_dto = StockDto.model_validate(stock)
        op = random.randint(0, 1)
        if op == 0:
            stock_dto.quantity = "{:.4f}".format(stock_dto.quantity - (stock_dto.quantity * random.uniform(0, 0.25)))
        elif op == 1:
            stock_dto.quantity = "{:.4f}".format(stock_dto.quantity + (stock_dto.quantity * random.uniform(0, 0.25)))
        self.ctrl_stock.update(stock_dto, self.user)
