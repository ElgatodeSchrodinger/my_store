from typing import Any, List, Optional
from domain.events.events import UpdateProduct
from domain.productManagment.productSchema import ProductCreateSchema, ProductDBSchema, ProductUpdateSchema
from datetime import datetime

class ProductService:
    def __init__(self, product_queries: Any):
        self.__product_queries = product_queries

    def create_product(self, product: ProductCreateSchema) -> ProductDBSchema:
        new_product = self.__product_queries.create_product(product)
        print(new_product)
        return ProductDBSchema.from_orm(new_product)

    def get_product_by_id(self, product_id: int) -> Optional[ProductDBSchema]:
        product = self.__product_queries.get_product_byid(product_id)
        if product:
            return ProductDBSchema.from_orm(product)
        else:
            return None

    def update_product(self, product_id: int, new_product: ProductUpdateSchema) -> ProductDBSchema:
        old_product = self.__product_queries.get_product_byid(product_id)
        product_updated = self.__product_queries.update_product(old_product, new_product)
        return ProductDBSchema.from_orm(product_updated)

    def remove_product(self, product_id: int) -> ProductDBSchema:
        product_removed = self.__product_queries.delete_product(product_id)
        return ProductDBSchema.from_orm(product_removed)