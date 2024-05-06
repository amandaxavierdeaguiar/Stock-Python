from typing import List

from sqlalchemy import select

from models.brand.dto.BrandDto import BrandDto
from models.brand.orm.BrandOrm import BrandOrm as brand
from shared.Enums.TypeResult import TypeResult
from shared.base.BaseRepository import BaseRepository
from shared.base.BaseResponse import BaseResponse
from shared.db.db_conection import get_session


class BrandRepository(BaseRepository[BrandDto]):
    session = get_session()

    def __init__(self):
        super().__init__()

    def add(self, entity_dto: BrandDto, user_) -> BaseResponse[BrandDto]:
        entity = None
        result = None
        message = None
        try:
            orm = brand(**entity_dto.dict())
            self.session.add(orm)
            self.session.commit()
            self.session.refresh(orm)

            entity = BrandDto.validate(orm)
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=self.session, message_=message, user_=user_)

    @classmethod
    def get_all(cls, user_) -> BaseResponse[List[BrandDto]]:
        statement = select(brand)
        entity = None
        result = None
        message = None
        try:
            result_exec = cls.session.execute(statement).all()

            entity = [BrandDto.validate(e[0]) for e in result_exec]
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def get_by_id(cls, entity: BrandDto, user_) -> BaseResponse[BrandDto]:
        pass

    @classmethod
    def get_by_name(cls, name_: str, user_) -> BaseResponse[BrandDto]:
        statement = select(brand).where(brand.name == name_)
        result = cls.session.exec(statement).one()
        return result

    @classmethod
    def update(cls, entity: BrandDto, user_) -> BaseResponse[BrandDto]:
        pass

    @classmethod
    def delete(cls, entity: BrandDto, user_) -> BaseResponse[BrandDto]:
        pass
