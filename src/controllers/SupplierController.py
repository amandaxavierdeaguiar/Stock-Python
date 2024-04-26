from models.supplier.dto import SupplierDto
from repositories.SupplierRepository import SupplierRepository
from shared.Base.BaseController import BaseController
from shared.Base.BaseResponse import BaseResponse


class SupplierController(BaseController[SupplierDto]):
    repo = SupplierRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity, session_, user) -> BaseResponse[SupplierDto]:
        return cls.repo.add(entity, session_, user)

    @classmethod
    def get_all(cls, session_):
        return cls.repo.get_all(session_)

    @classmethod
    def get_by_id(cls, entity, session_):
        pass

    @classmethod
    def update(cls, entity, session_) -> None:
        pass

    @classmethod
    def delete(cls, entity, session_) -> None:
        pass
