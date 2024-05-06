from typing import List

from models.category.dto import CategoryDto
from repositories.CategoryRepository import CategoryRepository
from shared.base.BaseController import BaseController, T
from shared.base.BaseResponse import BaseResponse


class CategoryController(BaseController[CategoryDto]):
    repo = CategoryRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity: T, user_) -> BaseResponse[CategoryDto]:
        return cls.repo.add(entity, user_)

    @classmethod
    def get_all(cls, user_) -> BaseResponse[List[CategoryDto]]:
        return cls.repo.get_all(user_)

    @classmethod
    def get_by_id(cls, entity: T, user_) -> BaseResponse[CategoryDto]:
        pass

    @classmethod
    def update(cls, entity: T, user_) -> BaseResponse[CategoryDto]:
        pass

    @classmethod
    def delete(cls, entity: T, user_) -> BaseResponse[CategoryDto]:
        pass
