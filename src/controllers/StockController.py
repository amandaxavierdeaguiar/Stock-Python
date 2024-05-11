from typing import List

from controllers.StockHistoryController import StockHistoryController
from models.history.dto.StockHistoryDto import StockHistoryDto
from models.stock.dto import StockDto
from models.stock.dto.StockTableDto import StockTableDto
from repositories.StockRepository import StockRepository
from shared.Enums.TypeResult import TypeResult
from shared.base.BaseController import BaseController
from shared.base.BaseResponse import BaseResponse


class StockController(BaseController[StockDto]):
    repo = StockRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity_dto: StockDto, user_) -> BaseResponse[StockDto]:
        base = cls.repo.add(entity_dto, user_)
        if base.result == TypeResult.Success:
            to_pass = {
                'product_name': base.entity['entity_'].product_name,
                'product_bar_cod': base.entity['entity_'].product_bar_cod,
                'supplier_name': base.entity['entity_'].supplier_name,
                'user_login': 'admin@email.com',
                'quantity': base.entity['entity_'].quantity
            }
            new_history = StockHistoryDto(**to_pass)
            ctrl = StockHistoryController()
            ctrl.add(new_history, base.user)
        return base

    @classmethod
    def get_all(cls, user) -> BaseResponse[List[StockDto]]:
        return cls.repo.get_all(user)

    @classmethod
    def get_all_table(cls, user) -> BaseResponse[List[StockTableDto]]:
        return cls.repo.get_all_table(user)

    @classmethod
    def get_search(cls, search, user) -> BaseResponse[List[StockTableDto]]:
        return cls.repo.get_search(search, user)

    @classmethod
    def get_by_id(cls, entity: StockDto, user_) -> BaseResponse[StockDto]:
        pass

    @classmethod
    def update(cls, entity_dto: StockDto, user_) -> BaseResponse[StockDto]:
        return cls.repo.update(entity_dto, user_)

    @classmethod
    def update_quantity(cls, entity_dto: StockDto, user_) -> BaseResponse[StockDto]:
        base = cls.repo.update(entity_dto, user_)
        if base.result == TypeResult.Success:
            to_pass = {
                'product_name': base.entity['entity_'].product_name,
                'product_bar_cod': base.entity['entity_'].product_bar_cod,
                'supplier_name': base.entity['entity_'].supplier_name,
                'user_login': 'admin@email.com',
                'quantity': base.entity['entity_'].quantity
            }
            new_history = StockHistoryDto(**to_pass)
            ctrl = StockHistoryController()
            test = ctrl.add(new_history, base.user)
        return base

    @classmethod
    def delete(cls, entity: StockDto, user_) -> BaseResponse[StockDto]:
        pass
