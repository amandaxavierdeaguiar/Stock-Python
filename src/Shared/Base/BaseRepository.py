from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

from shared.Base.BaseResponse import BaseResponse
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)


class BaseRepository(Generic[T], ABC):

    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def add(cls, entity: T, user_) -> BaseResponse[T]:
        return BaseResponse[T]

    @classmethod
    @abstractmethod
    def get_all(cls, user_) -> BaseResponse[List[T]]:
        return BaseResponse[List[T]]

    @classmethod
    @abstractmethod
    def get_by_id(cls, entity: T, user_) -> BaseResponse[T]:
        return BaseResponse[T]

    @classmethod
    @abstractmethod
    def update(cls, entity: T, user_) -> BaseResponse[T]:
        return BaseResponse[T]

    @classmethod
    @abstractmethod
    def delete(cls, entity: T, user_) -> BaseResponse[T]:
        return BaseResponse[T]
