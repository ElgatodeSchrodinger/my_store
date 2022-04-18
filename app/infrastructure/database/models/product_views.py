from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from domain.events.events import Event
from domain.events.actions import IInformationSaver

from core.db import Base, engine, get_db

class ProductViewsModel(Base):
    __tablename__ = 'product_views'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    date = Column(DateTime(timezone=True), nullable=False)

class InformationSaver(IInformationSaver):

    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.session = next(get_db())
    
    def save_details(self, event: Event):
        product_view_data = event.__dict__
        product_view_obj = ProductViewsModel(**product_view_data)
        with self.session as session:
            session.add(product_view_obj)
            session.commit()
            session.flush()
            session.refresh(product_view_obj)
        return product_view_obj