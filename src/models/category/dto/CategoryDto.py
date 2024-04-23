from pydantic import BaseModel, ConfigDict


class CategoryDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str

