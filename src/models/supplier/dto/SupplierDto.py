from pydantic import BaseModel, EmailStr, ConfigDict


class SupplierDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    address: str
    phone: str
    email: EmailStr
