from models.supplier.dto import SupplierDto
from repositories.SupplierRepository import SupplierRepository
from shared.Base.BaseController import BaseController
from shared.Base.BaseResponse import BaseResponse


class SupplierController(BaseController[SupplierDto]):
    repo = SupplierRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity, user) -> BaseResponse[SupplierDto]:
        return cls.repo.add(entity, user)

    @classmethod
    def get_all(cls, user):
        return cls.repo.get_all(user)

    @classmethod
    def get_by_id(cls, entity, user):
        pass

    @classmethod
    def update(cls, entity, user) -> None:
        pass

    @classmethod
    def delete(cls, entity, user) -> None:
        pass
