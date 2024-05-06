from typing import List

from models.history.dto.StockHistoryDto import StockHistoryDto
from repositories.StockHistoryRepository import StockHistoryRepository
from shared.base.BaseController import BaseController
from shared.base.BaseResponse import BaseResponse


class StockHistoryController(BaseController[StockHistoryDto]):
    repo = StockHistoryRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity: StockHistoryDto, user_) -> BaseResponse[StockHistoryDto]:
        return cls.repo.add(entity, user_)

    @classmethod
    def get_all(cls, user_) -> BaseResponse[List[StockHistoryDto]]:
        pass

    @classmethod
    def get_by_id(cls, entity: StockHistoryDto, user_) -> BaseResponse[StockHistoryDto]:
        pass

    @classmethod
    def get_by_name(cls, name: str, user_) -> BaseResponse[List[StockHistoryDto]]:
        return cls.repo.get_by_name(name, user_)

    @classmethod
    def update(cls, entity: StockHistoryDto, user_) -> BaseResponse[StockHistoryDto]:
        pass

    @classmethod
    def delete(cls, entity: StockHistoryDto, user_) -> BaseResponse[StockHistoryDto]:
        pass
