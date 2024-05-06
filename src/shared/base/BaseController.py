from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

from shared.base.BaseResponse import BaseResponse

T = TypeVar("T")


class BaseController(Generic[T], ABC):

    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def add(cls, entity: T, user) -> BaseResponse[T]:
        return BaseResponse[T]

    @classmethod
    @abstractmethod
    def get_all(cls, user) -> BaseResponse[List[T]]:
        return BaseResponse[List[T]]

    @classmethod
    @abstractmethod
    def get_by_id(cls, entity: T, user) -> BaseResponse[T]:
        return BaseResponse[T]

    @classmethod
    @abstractmethod
    def update(cls, entity: T, user) -> BaseResponse[T]:
        return BaseResponse[T]

    @classmethod
    @abstractmethod
    def delete(cls, entity: T, user) -> BaseResponse[T]:
        return BaseResponse[T]
