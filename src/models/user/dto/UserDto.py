from typing import Optional, Union

from pydantic import BaseModel, EmailStr, SecretStr, field_serializer, ConfigDict


from shared.Enums.TypeAccess import TypeAccess


class UserDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    login: EmailStr
    password: str
    typeAccess: TypeAccess

    @field_serializer('password', when_used='always')
    def dump_secret(self, v):
        return v.get_secret_value()
