from models.brand.dto import BrandDto
from repositories.BrandRepository import BrandRepository
from shared.base.BaseController import BaseController
from shared.base.BaseResponse import BaseResponse


class BrandController(BaseController[BrandDto]):
    repo = BrandRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity, user) -> BaseResponse[BrandDto]:
        return cls.repo.add(entity, user)

    @classmethod
    def get_all(cls, user):
        return cls.repo.get_all(user)

    @classmethod
    def get_by_id(cls, entity, user):
        pass

    @classmethod
    def get_by_name(cls, name: str, user):
        return cls.repo.get_by_name(name, user)

    @classmethod
    def update(cls, entity, user) -> None:
        pass

    @classmethod
    def delete(cls, entity, user) -> None:
        pass
