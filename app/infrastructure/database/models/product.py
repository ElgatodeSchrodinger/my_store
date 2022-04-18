
from domain.productManagment.queriesInterface import IProductQueries
from domain.productManagment.productSchema import ProductCreateSchema, ProductUpdateSchema
from fastapi.encoders import jsonable_encoder
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from core.db import Base, engine, get_db

class ProductModel(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    sku = Column(String, nullable=False, unique=True)
    price = Column(Float(8, 2), nullable=False)
    brand = Column(String)
    created_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class ProductQueries(IProductQueries):

    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.session = next(get_db())

    def create_product(self, product: ProductCreateSchema) -> ProductModel:
        product_data = jsonable_encoder(product)
        product_obj = ProductModel(**product_data)
        with self.session as session:
            session.add(product_obj)
            session.commit()
            session.flush()
            session.refresh(product_obj)
        return product_obj

    def update_product(self, old_product: ProductModel, new_product: ProductUpdateSchema) -> ProductModel:
        with self.session as session:
            data = new_product.dict(exclude_unset=True)
            session.query(ProductModel).filter_by(product_id=old_product.product_id).update(data)
            session.commit()
            product_updated = session.query(ProductModel).filter_by(product_id=old_product.product_id).first()
        return product_updated

    def delete_product(self, product_id: int) -> ProductModel:
        with self.session as session:
            product_obj = session.query(ProductModel).get(product_id)
            session.delete(product_obj)
            session.commit()
        return product_obj

    def get_product_byid(self, product_id: int) -> ProductModel:

        with self.session as session:
            product_obj = session.query(ProductModel).filter_by(product_id=product_id).first()
        return product_obj
