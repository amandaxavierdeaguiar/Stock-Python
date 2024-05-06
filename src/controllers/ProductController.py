from typing import List

from controllers.ProductHistoryController import ProductHistoryController
from models.history.dto.ProductHistoryDto import ProductHistoryDto
from models.product.dto.Product import ProductDto
from repositories.ProductRepository import ProductRepository
from shared.Enums.TypeResult import TypeResult
from shared.base.BaseController import BaseController
from shared.base.BaseResponse import BaseResponse


class ProductController(BaseController[ProductDto]):
    repo = ProductRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity_dto: ProductDto, user_) -> BaseResponse[ProductDto]:
        base = cls.repo.add(entity_dto, user_)
        if base.result == TypeResult.Success:
            to_pass = {
                'product_name': base.entity['entity_'].name,
                'product_bar_cod': base.entity['entity_'].bar_cod,
                'user_login': 'admin@email.com',
                'price': base.entity['entity_'].price
            }
            new_history = ProductHistoryDto(**to_pass)
            ctrl = ProductHistoryController()
            ctrl.add(new_history, base.user)
        return base

    @classmethod
    def get_all(cls, user_) -> BaseResponse[List[ProductDto]]:
        return cls.repo.get_all(user_)

    @classmethod
    def get_by_name(cls, name) -> BaseResponse[ProductDto]:
        return cls.repo.get_by_name(name)

    @classmethod
    def get_by_id(cls, entity: ProductDto, user_) -> BaseResponse[ProductDto]:
        pass

    @classmethod
    def update(cls, entity_dto: ProductDto, user_) -> BaseResponse[ProductDto]:
        return cls.repo.update(entity_dto, user_)

    @classmethod
    def update_price(cls, entity_dto: ProductDto, user_) -> BaseResponse[ProductDto]:
        base = cls.repo.update(entity_dto, user_)
        if base.result == TypeResult.Success:
            to_pass = {
                'product_name': base.entity['entity_'].name,
                'product_bar_cod': base.entity['entity_'].bar_cod,
                'user_login': 'admin@email.com',
                'price': base.entity['entity_'].price
            }
            new_history = ProductHistoryDto(**to_pass)
            ctrl = ProductHistoryController()
            test = ctrl.add(new_history, base.user)
        return base

    @classmethod
    def delete(cls, entity: ProductDto, user_) -> BaseResponse[ProductDto]:
        pass
