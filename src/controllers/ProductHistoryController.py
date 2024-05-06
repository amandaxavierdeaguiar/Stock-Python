from typing import List

from models.history.dto.ProductHistoryDto import ProductHistoryDto
from repositories.ProductHistoryRepository import ProductHistoryRepository
from shared.base.BaseController import BaseController
from shared.base.BaseResponse import BaseResponse


class ProductHistoryController(BaseController[ProductHistoryDto]):
    repo = ProductHistoryRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity: ProductHistoryDto, user_) -> BaseResponse[ProductHistoryDto]:
        return cls.repo.add(entity, user_)

    @classmethod
    def get_all(cls, user_) -> BaseResponse[List[ProductHistoryDto]]:
        pass

    @classmethod
    def get_by_id(
            cls, entity: ProductHistoryDto, user_
    ) -> BaseResponse[ProductHistoryDto]:
        pass

    @classmethod
    def get_by_name(cls, name: str, user_) -> BaseResponse[List[ProductHistoryDto]]:
        return cls.repo.get_by_name(name, user_)

    @classmethod
    def update(
            cls, entity: ProductHistoryDto, user_
    ) -> BaseResponse[ProductHistoryDto]:
        pass

    @classmethod
    def delete(
            cls, entity: ProductHistoryDto, user_
    ) -> BaseResponse[ProductHistoryDto]:
        pass
