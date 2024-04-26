from models.user.dto.UserDto import UserDto
from repositories.UserRepository import UserRepository
from shared.Base.BaseController import BaseController
from shared.Base.BaseResponse import BaseResponse


class UserController(BaseController[UserDto]):
    repo = UserRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity, user) -> BaseResponse[UserDto]:
        return cls.repo.add(entity, user)

    @classmethod
    def get_all(cls, user):
        return cls.repo.get_all(user)

    @classmethod
    def get_by_email(cls, email: str):
        return cls.repo.get_by_email(email)

    @classmethod
    def get_by_id(cls, entity, user):
        return cls.repo.get_by_id(entity, user)

    @classmethod
    def update(cls, entity, user) -> None:
        cls.repo.update(entity, user)

    @classmethod
    def delete(cls, entity, user) -> None:
        cls.repo.delete(entity, user)
