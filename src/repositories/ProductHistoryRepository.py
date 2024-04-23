from typing import List
from sqlalchemy import select

from models.history.dto.ProductHistoryDto import ProductHistoryDto
from models.history.orm.ProductHistoryOrm import ProductHistoryOrm
from shared.Base.BaseRepository import BaseRepository, T
from shared.Base.BaseResponse import BaseResponse
from shared.Enums.TypeResult import TypeResult
from shared.db.db_conection import get_session


class ProductHistoryRepository(BaseRepository[ProductHistoryOrm]):
    session = get_session()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity_dto: ProductHistoryDto, user_) -> BaseResponse[ProductHistoryDto]:
        entity = None
        result = None
        message = None
        try:
            orm = ProductHistoryOrm(**entity_dto.dict())
            cls.session.add(orm)
            cls.session.commit()
            cls.session.refresh(orm)

            entity = ProductHistoryDto.validate(orm)
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def get_all(cls, user_) -> BaseResponse[List[ProductHistoryDto]]:
        pass

    @classmethod
    def get_by_name(cls, entity_dto: ProductHistoryDto, user_) -> BaseResponse[ProductHistoryDto]:
        statement = select(ProductHistoryOrm).where(ProductHistoryOrm.product_name == entity_dto.product_name)
        entity = None
        result = None
        message = None
        try:
            # result_exec = session_.exec(statement).one()
            result_exec = cls.session.execute(statement).one()
            entity = ProductHistoryDto.model_validate(result_exec[0])
            result = TypeResult.Success
        except Exception as e:
            message = e
            result = TypeResult.Failure
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=None)

    @classmethod
    def get_by_id(cls, entity: T, user_) -> BaseResponse[T]:
        pass

    @classmethod
    def update(cls, entity: ProductHistoryDto, user_) -> BaseResponse[ProductHistoryDto]:
        pass

    @classmethod
    def delete(cls, entity: ProductHistoryDto, user_) -> BaseResponse[ProductHistoryDto]:
        pass
