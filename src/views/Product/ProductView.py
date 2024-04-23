from controllers.StockHistoryController import StockHistoryController
from controllers.ProductHistoryController import ProductHistoryController
from controllers.CategoryController import CategoryController
from controllers.BrandController import BrandController
from controllers.ProductController import ProductController
from controllers.StockController import StockController
from shared.Base.SharedControls import SharedControls
from views.Product.ListProduct import table_data
import pandas as pd


class ProductView(SharedControls):
    ctrl_category = CategoryController()
    ctrl_brand = BrandController()
    ctrl_product = ProductController()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def get_all_categories(cls):
        base = cls.ctrl_product.get_all(cls.user)
        entities = [e.dict() for e in base.entity['entity_']]
        data_category = pd.DataFrame.from_dict(data=entities)
        count_by_category = data_category.groupby('category_id')['category_id'].count().head(5)
        dict_count_by_category = [count_by_category.to_dict()]
        return dict_count_by_category

    @classmethod
    def get_all_brands(cls):
        base = cls.ctrl_brand.get_all(cls.user)
        entities = [e.dict() for e in base.entity['entity_']]
        data_brand = pd.DataFrame.from_dict(data=entities)
        count_by_brand = data_brand.groupby('name')['name'].count().head(5)
        dict_count_by_brand = [count_by_brand.to_dict()]
        return dict_count_by_brand

    @classmethod
    def get_all_prices(cls):
        base = cls.ctrl_product.get_all(cls.user)
        entities = [e.dict() for e in base.entity['entity_']]
        data_price = pd.DataFrame.from_dict(data=entities)
        # Min , max do que vem da base de dados
        min_price = data_price['price'].min()
        max_price = data_price['price'].max()
        avg_price = data_price['price'].mean()

        # calcula como tem que dividir por 5 com base do min, max
        num_groups = round((max_price - min_price) // 5 + avg_price)
        n_groups = int(num_groups)

        # Create bins and labels
        bins = [0, ]
        for i in range(n_groups):
            bins.append(min_price + avg_price * i)
        labels = ['{:.2f}'.format(bins[i]) + '-' + '{:.2f}'.format(bins[i + 1]) for i in range(n_groups - 1)] + [
            f'{bins[-1]}-{max_price}']
        # Add a new column 'price_group' to DataFrame with bin labels
        data_price['price_group'] = pd.cut(data_price['price'], bins=bins, labels=labels, right=False)

        # Group by 'price_group' and count occurrences
        grouped_counts = data_price.groupby('price_group', observed=True).size().reset_index(name='count')
        dict_count_by_price = grouped_counts.to_dict()
        groups, counts = dict_count_by_price['price_group'].values(), dict_count_by_price['count'].values()
        return groups, counts
