from dataclasses import dataclass
from datetime import datetime
from typing import Dict

from domain.productManagment.productSchema import ProductUpdateSchema


class Event:
    pass


@dataclass
class ViewProductByAnon(Event):
    user_id: int
    product_id: int
    date: datetime


@dataclass
class UpdateProduct(Event):
    user_id: int
    product_id: int
    change: Dict
    date: datetime
