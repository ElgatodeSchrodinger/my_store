from typing import Any, List
from domain.productManagment.productService import ProductService
from domain.productManagment.productSchema import ProductCreateSchema, ProductDBSchema, ProductUpdateSchema
from infrastructure.database.models.product import ProductModel

import pytest

from domain.productManagment.productSchema import ProductCreateSchema, ProductDBSchema, ProductUpdateSchema
from domain.productManagment.productService import ProductService
from infrastructure.database.models.product import ProductModel

PRODUCT_MODEL = ProductModel(
    product_id=1,
    name="Product1",
    sku="abc-1",
    price=10.0,
    brand="JQ",
    created_date="1/1/2020",
)


class ProductQueriesDummy:
    def create_product(self, product: Any) -> ProductModel:
        return PRODUCT_MODEL

    def update_product(self, old_product: Any, new_product: Any) -> ProductModel:
        return PRODUCT_MODEL

    def delete_product(self, product_id: int) -> ProductModel:
        return PRODUCT_MODEL

    def get_product_byid(self, product_id: int) -> ProductModel:
        return PRODUCT_MODEL


@pytest.fixture
def product_model() -> ProductModel:
    return PRODUCT_MODEL


@pytest.fixture
def product_schema() -> ProductCreateSchema:
    return ProductCreateSchema(
        product_id=1,
        name="Product1",
        sku="abc-1",
        price=10.0,
        brand="JQ",
        created_date="1/1/2020",
    )


@pytest.fixture
def product_update_schema() -> ProductUpdateSchema:
    return ProductUpdateSchema(
        product_id=1,
        name="Product1",
        sku="abc-1",
        price=10.0,
        brand="JQ",
        created_date="1/1/2020",
    )


class TestProductService:
    
    def test_product_create_valide(
        self, product_model: ProductModel, product_schema: ProductCreateSchema
    ) -> None:
        product_service = ProductService(ProductQueriesDummy())

        result = product_service.create_product(product_schema)
        assert result == ProductDBSchema(
            product_id=1,
            name="Product1",
            sku="abc-1",
            price=10.0,
            brand="JQ",
            created_date="1/1/2020",
        )

    def test_product_update_product(
        self, product_model: ProductModel, product_update_schema: ProductUpdateSchema
    ) -> None:
        product_service = ProductService(ProductQueriesDummy())

        result = product_service.update_product(1, product_update_schema)
        assert result == ProductDBSchema(
            product_id=1,
            name="Product1",
            sku="abc-1",
            price=10.0,
            brand="JQ",
            created_date="1/1/2020",
        )

    def test_product_remove_product(
        self, product_model: ProductModel, product_schema: ProductCreateSchema
    ) -> None:
        product_service = ProductService(ProductQueriesDummy())

        result = product_service.remove_product(1)
        assert result == ProductDBSchema(
            product_id=1,
            name="Product1",
            sku="abc-1",
            price=10.0,
            brand="JQ",
            created_date="1/1/2020",
        )

    def test_product_get_product_by_id(
        self, product_model: ProductModel, product_schema: ProductCreateSchema
    ) -> None:
        product_service = ProductService(ProductQueriesDummy())

        result = product_service.get_product_by_id(1)
        assert result == ProductDBSchema(
            product_id=1,
            name="Product1",
            sku="abc-1",
            price=10.0,
            brand="JQ",
            created_date="1/1/2020",
        )
