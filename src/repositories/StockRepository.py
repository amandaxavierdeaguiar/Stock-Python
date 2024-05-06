from typing import List

from sqlalchemy import select, update

from models.product.orm.Product import ProductOrm
from models.stock.dto.StockDto import StockDto
from models.stock.dto.StockTableDto import StockTableDto
from models.stock.orm.StockOrm import StockOrm
from shared.Enums.TypeResult import TypeResult
from shared.base.BaseRepository import BaseRepository
from shared.base.BaseResponse import BaseResponse
from shared.db.db_conection import get_session


class StockRepository(BaseRepository[StockDto]):
    session = get_session()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity_dto: StockDto, user_) -> BaseResponse[StockDto]:
        entity = None
        result = None
        message = None
        try:
            orm = StockOrm(**entity_dto.model_dump())
            cls.session.add(orm)
            cls.session.commit()
            cls.session.refresh(orm)

            entity = StockDto.model_validate(orm)
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def get_all(cls, user_) -> BaseResponse[List[StockDto]]:
        statement = select(StockOrm)
        entity = None
        result = None
        message = None
        try:
            result_exec = cls.session.execute(statement).all()

            entity = [StockDto.validate(e[0]) for e in result_exec]
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def get_all_table(cls, user_) -> BaseResponse[List[StockTableDto]]:
        statement = (select(
            StockOrm.product_bar_cod,
            StockOrm.product_name,
            ProductOrm.brand_name,
            ProductOrm.category_name,
            ProductOrm.price,
            StockOrm.quantity,
            ProductOrm.description,
            ProductOrm.photo,
            StockOrm.supplier_name)
                     .join(StockOrm, ProductOrm.name == StockOrm.product_name, full=True))
        entity = None
        result = None
        message = None
        try:
            result_exec = cls.session.execute(statement).mappings().all()

            entity = [StockTableDto.model_validate(e) for e in result_exec]
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def get_search(cls, search, user_) -> BaseResponse[List[StockTableDto]]:
        w = {}
        for field in search['fields']:
            if field[0] == 'price':
                label1, label2 = field[1].split('-')
                w = {ProductOrm.price.between(label1, label2)}
            elif field[0] == 'category' or field[0] == 'category_name':
                w = {ProductOrm.category_name == field[1]}
            elif field[0] == 'brand' or field[0] == 'brand_name':
                w = {ProductOrm.brand_name == field[1]}
            elif field[0] == 'product_name':
                w = {ProductOrm.name.like(f"%{field[1]}%")}

        statement = (select(
            StockOrm.product_bar_cod,
            StockOrm.product_name,
            ProductOrm.brand_name,
            ProductOrm.category_name,
            ProductOrm.price,
            StockOrm.quantity,
            ProductOrm.description,
            ProductOrm.photo,
            StockOrm.supplier_name)
                     .filter(*w)
                     .join(StockOrm, ProductOrm.name == StockOrm.product_name, full=True))
        entity = None
        result = None
        message = None
        try:
            result_exec = cls.session.execute(statement).mappings().all()

            entity = [StockTableDto.model_validate(e) for e in result_exec]
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def get_by_id(cls, entity: StockDto, user_) -> BaseResponse[StockDto]:
        pass

    @classmethod
    def update(cls, entity_dto: StockDto, user_) -> BaseResponse[StockDto]:
        stmt = ((update(StockOrm)
                 .where(StockOrm.product_name == entity_dto.product_name))
                .values(quantity=entity_dto.quantity)
                .returning(StockOrm))
        entity = None
        result = None
        message = None
        try:
            result_exec = cls.session.execute(stmt).one()
            cls.session.commit()
            entity = StockDto.model_validate(result_exec[0])
            result = TypeResult.Success
        except Exception as e:
            result = TypeResult.Failure
            message = e
        finally:
            cls.session.close()
            return BaseResponse(entity_=entity, result_=result, session_=cls.session, message_=message, user_=user_)

    @classmethod
    def delete(cls, entity: StockDto, user_) -> BaseResponse[StockDto]:
        pass
