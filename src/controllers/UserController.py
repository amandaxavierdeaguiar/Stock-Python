from models.user.dto.UserDto import UserDto
from repositories.UserRepository import UserRepository
from shared.Base.BaseController import BaseController
from shared.Base.BaseResponse import BaseResponse


class UserController(BaseController[UserDto]):
    repo = UserRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity, session_, user) -> BaseResponse[UserDto]:
        return cls.repo.add(entity, session_, user)

    @classmethod
    def get_all(cls, session_, user):
        return cls.repo.get_all(session_, user)

    @classmethod
    def get_by_email(cls, email: str, session_, user):
        return cls.repo.get_all(session_, user)

    @classmethod
    def get_by_id(cls, entity, session_, user):
        return cls.repo.get_by_id(entity, session_)

    @classmethod
    def update(cls, entity, session_, user) -> None:
        cls.repo.update(entity, session_, user)

    @classmethod
    def delete(cls, entity, session_, user) -> None:
        cls.repo.delete(entity, session_, user)

    @classmethod
    def authenticate_user(cls, email, password, session_, user):
        result = cls.get_by_email(email, session_, user)
        if result:
            if result.password == password:
                return True
            else:
                return False
        else:
            return False
