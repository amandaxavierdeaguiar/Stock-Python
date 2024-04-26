from typing import List
from sqlalchemy import select

from models.category.orm.CategoryOrm import CategoryOrm
from models.category.dto.CategoryDto import CategoryDto
from shared.Base.BaseRepository import BaseRepository
from shared.Base.BaseResponse import BaseResponse
from shared.Enums.TypeResult import TypeResult
from shared.db.db_conection import get_session


class CategoryRepository(BaseRepository[CategoryDto]):
    session = get_session()

    @classmethod
    def add(cls, entity_dto: CategoryDto, user_) -> BaseResponse[CategoryDto]:
        entity = None
        result = None
        message = None
        try:
            orm = CategoryOrm(**entity_dto.dict())
            cls.session.add(orm)
            cls.session.commit()
            cls.session.refresh(orm)

            entity = CategoryDto.validate(orm)
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def get_all(cls, user_) -> BaseResponse[List[CategoryDto]]:
        statement = select(CategoryOrm)
        entity = None
        result = None
        message = None
        try:
            result_exec = cls.session.execute(statement).all()

            entity = [CategoryDto.validate(e[0]) for e in result_exec]
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def get_by_id(cls, entity: CategoryDto, user_) -> BaseResponse[CategoryDto]:
        pass

    @classmethod
    def update(cls, entity: CategoryDto, user_) -> BaseResponse[CategoryDto]:
        pass

    @classmethod
    def delete(cls, entity: CategoryDto, user_) -> BaseResponse[CategoryDto]:
        pass
