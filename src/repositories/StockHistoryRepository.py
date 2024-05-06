from typing import List

from sqlalchemy import select

from models.history.dto.StockHistoryDto import StockHistoryDto
from models.history.orm.StockHistoryOrm import StockHistoryOrm
from shared.Enums.TypeResult import TypeResult
from shared.base.BaseRepository import BaseRepository
from shared.base.BaseResponse import BaseResponse
from shared.db.db_conection import get_session


class StockHistoryRepository(BaseRepository[StockHistoryOrm]):
    session = get_session()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity_dto: StockHistoryDto, user_) -> BaseResponse[StockHistoryDto]:
        entity = None
        result = None
        message = None
        try:
            orm = StockHistoryOrm(**entity_dto.dict())
            cls.session.add(orm)
            cls.session.commit()
            cls.session.refresh(orm)

            entity = StockHistoryDto.model_validate(orm)
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def get_all(cls, user_) -> BaseResponse[List[StockHistoryDto]]:
        pass

    @classmethod
    def get_by_id(cls, entity: StockHistoryDto, user_) -> BaseResponse[StockHistoryDto]:
        pass

    @classmethod
    def get_by_name(cls, name: str, user_) -> BaseResponse[List[StockHistoryDto]]:
        statement = select(StockHistoryOrm).where(StockHistoryOrm.product_name == name)
        entity = None
        result = None
        message = None
        try:
            # result_exec = session_.exec(statement).one()
            result_exec = cls.session.execute(statement).all()
            entity = [StockHistoryDto.model_validate(e[0]) for e in result_exec]
            result = TypeResult.Success
        except Exception as e:
            message = e
            result = TypeResult.Failure
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def update(cls, entity: StockHistoryDto, user_) -> BaseResponse[StockHistoryDto]:
        pass

    @classmethod
    def delete(cls, entity: StockHistoryDto, user_) -> BaseResponse[StockHistoryDto]:
        pass
