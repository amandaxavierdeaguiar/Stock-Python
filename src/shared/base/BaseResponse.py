from abc import ABC
from typing import Generic, Optional, TypeVar

from sqlalchemy.orm import Session
from pydantic import BaseModel

from shared.Enums.TypeResult import TypeResult

T = TypeVar("T")


class BaseResponse(Generic[T], ABC):
    entity: [T]
    session: Session
    user = None
    result: TypeResult
    message: Optional[str]

    def __init__(self, user_, result_, session_, message_=None, **entity_):
        super().__init__()
        self.entity: [T] = entity_
        self.session: Session = session_
        self.user = user_
        self.result: TypeResult = result_
        self.message: Optional[str] = message_

    def __repr__(self):
        return {
            'user': self.user,
            'session': self.session,
            'entity': [self.entity],
            'result': self.result.value,
            'message': self.message,
        }
