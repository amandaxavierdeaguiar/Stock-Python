from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.supplier.dto.SupplierDto import SupplierDto
from models.supplier.orm.SupplierOrm import SupplierOrm
from shared.Enums.TypeResult import TypeResult
from shared.base.BaseRepository import BaseRepository
from shared.base.BaseResponse import BaseResponse
from shared.db.db_conection import get_session


class SupplierRepository(BaseRepository[SupplierDto]):
    session: Session = get_session()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity_dto: SupplierDto, user_) -> BaseResponse[SupplierDto]:
        entity = None
        result = None
        message = None
        try:
            orm = SupplierOrm(**entity_dto.dict())
            cls.session.add(orm)
            cls.session.commit()
            cls.session.refresh(orm)

            entity = SupplierDto.validate(orm)
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def get_all(cls, user_) -> BaseResponse[List[SupplierDto]]:
        statement = select(SupplierOrm)
        entity = None
        result = None
        message = None
        try:
            result_exec = cls.session.execute(statement).all()

            entity = [SupplierDto.validate(e[0]) for e in result_exec]
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def get_by_id(cls, entity: SupplierDto, user_) -> BaseResponse[SupplierDto]:
        pass

    @classmethod
    def update(cls, entity: SupplierDto, user_) -> BaseResponse[SupplierDto]:
        pass

    @classmethod
    def delete(cls, entity: SupplierDto, user_) -> BaseResponse[SupplierDto]:
        pass
