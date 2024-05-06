from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.user.dto.UserDto import UserDto
from models.user.orm.UserOrm import UserOrm
from shared.Enums.TypeResult import TypeResult
from shared.base.BaseRepository import BaseRepository
from shared.base.BaseResponse import BaseResponse
from shared.db.db_conection import get_session


class UserRepository(BaseRepository[UserDto]):
    session: Session = get_session()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity_dto: UserDto, user_) -> BaseResponse[UserDto]:
        entity = None
        result = None
        message = None
        try:
            orm = UserOrm(**entity_dto.dict())
            cls.session.add(orm)
            cls.session.commit()
            cls.session.refresh(orm)

            entity = UserDto.model_validate(orm)
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def get_all(cls, user_) -> BaseResponse[List[UserDto]]:
        statement = select(UserOrm)
        entity = None
        result = None
        message = None
        try:
            result_exec = cls.session.execute(statement).all()

            entity = [UserDto.validate(e[0]) for e in result_exec]
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def get_by_id(cls, entity: UserDto, user_) -> BaseResponse[UserDto]:
        pass

    @classmethod
    async def get_by_email(cls, login: str) -> BaseResponse[UserDto]:
        statement = select(UserOrm).where(UserOrm.login == login)
        entity = None
        result = None
        message = None
        try:
            # result_exec = session_.exec(statement).one()
            result_exec = cls.session.execute(statement).one()
            entity = UserDto.model_validate(result_exec[0])
            result = TypeResult.Success
        except Exception as e:
            message = e
            result = TypeResult.Failure
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=None)

    @classmethod
    def update(cls, entity: UserDto, user_) -> BaseResponse[UserDto]:
        pass

    @classmethod
    def delete(cls, entity: UserDto, user_) -> BaseResponse[UserDto]:
        pass
