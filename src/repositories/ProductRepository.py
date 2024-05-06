from typing import List

from sqlalchemy import select, update

from models.product.dto.Product import ProductDto
from models.product.orm.Product import ProductOrm
from shared.Enums.TypeResult import TypeResult
from shared.base.BaseRepository import BaseRepository
from shared.base.BaseResponse import BaseResponse
from shared.db.db_conection import get_session


class ProductRepository(BaseRepository[ProductDto]):
    session = get_session()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity_dto: ProductDto, user_) -> BaseResponse[ProductDto]:
        entity = None
        result = None
        message = None
        try:
            orm = ProductOrm(**entity_dto.dict())
            cls.session.add(orm)
            cls.session.commit()
            cls.session.refresh(orm)

            entity = ProductDto.model_validate(orm)
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def get_all(cls, user_) -> BaseResponse[List[ProductDto]]:
        statement = select(ProductOrm)
        entity = None
        result = None
        message = None
        try:
            result_exec = cls.session.execute(statement).all()

            entity = [ProductDto.model_validate(e[0]) for e in result_exec]
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def get_by_name(cls, name: str) -> BaseResponse[ProductDto]:
        statement = select(ProductOrm).where(ProductOrm.name == name)
        entity = None
        result = None
        message = None
        try:
            # result_exec = session_.exec(statement).one()
            result_exec = cls.session.execute(statement).one()
            entity = ProductDto.model_validate(result_exec[0])
            result = TypeResult.Success
        except Exception as e:
            message = e
            result = TypeResult.Failure
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=None)

    @classmethod
    def get_by_id(cls, entity: ProductDto, user_) -> BaseResponse[ProductDto]:
        pass

    @classmethod
    def update(cls, entity_dto: ProductDto, user_) -> BaseResponse[ProductDto]:
        stmt = ((update(ProductOrm)
                 .where(ProductOrm.name == entity_dto.name))
                .values(price=entity_dto.price)
                .returning(ProductOrm))
        entity = None
        result = None
        message = None
        try:
            result_exec = cls.session.execute(stmt).one()
            cls.session.commit()
            entity = ProductDto.model_validate(result_exec[0])
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            cls.session.close()
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def delete(cls, entity: ProductDto, user_) -> BaseResponse[ProductDto]:
        pass
