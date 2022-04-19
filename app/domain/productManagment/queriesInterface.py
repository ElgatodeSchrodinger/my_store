# used only for python >=3.6
from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, List
from domain.productManagment.productSchema import (
    ProductCreateSchema,
    ProductUpdateSchema,
)

if TYPE_CHECKING:
    from infrastructure.database.models.product import ProductModel


class IProductQueries:
    @abstractmethod
    async def create_product(self, user: ProductCreateSchema) -> ProductModel:
        raise NotImplementedError

    @abstractmethod
    async def update_product(
        self, old_user: ProductModel, new_user: ProductUpdateSchema
    ) -> ProductModel:
        raise NotImplementedError

    @abstractmethod
    async def delete_product(self, user_id: int) -> ProductModel:
        raise NotImplementedError

    @abstractmethod
    async def get_product_byid(self, user_id: int) -> ProductModel:
        raise NotImplementedError
