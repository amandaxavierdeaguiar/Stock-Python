import shortuuid

from pydantic import BaseModel, computed_field, ConfigDict


class ProductDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    photo: str
    description: str
    price: float
    brand_id: int
    category_id: int
    _bar_cod: str

    @computed_field
    @property
    def bar_cod(self) -> str:
        shortuuid.set_alphabet(alphabet="013456789")
        self._bar_cod = '{:0=3}-{:0=3}-{}'.format(
            self.brand_id,
            self.category_id,
            shortuuid.uuid(self.name)[:8])
        return self._bar_cod