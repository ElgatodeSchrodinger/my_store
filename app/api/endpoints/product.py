from datetime import datetime
from typing import List, Optional
from domain.events.events import UpdateProduct, ViewProductByAnon
from domain.userManagment.userConstants import UserRoles
from fastapi import Security

# from app.domain.auth.authUtils import auth_check
from domain.auth.authUtils import get_current_user_from_service

from fastapi import APIRouter, HTTPException, Depends, status

from api.utils import get_product_services
from domain.productManagment.productSchema import (
    ProductCreateSchema,
    ProductDBSchema,
    ProductUpdateSchema,
)
from domain.productManagment.productService import ProductService
from domain.auth.authSchema import AuthSchema
from domain.events import message_bus

router = APIRouter()


@router.post("/", response_model=ProductDBSchema)
def create_product(
    product: ProductCreateSchema,
    product_service: ProductService = Depends(get_product_services),
    token: str = Depends(AuthSchema),
    current_user: ProductDBSchema = Security(
        get_current_user_from_service, scopes=[UserRoles.admin.value]
    ),
) -> ProductDBSchema:
    return product_service.create_product(product)


@router.get("/{product_id}", response_model=ProductDBSchema)
def get_product_by_id(
    product_id: int,
    product_service: ProductService = Depends(get_product_services),
    token: str = Depends(AuthSchema),
    current_user: ProductDBSchema = Security(
        get_current_user_from_service,
        scopes=[UserRoles.admin.value, UserRoles.anonymous.value],
    ),
) -> Optional[ProductDBSchema]:
    product = product_service.get_product_by_id(product_id)
    if product:
        try:
            if current_user.rol == UserRoles.anonymous:
                view_event = ViewProductByAnon(
                    user_id=current_user.user_id,
                    product_id=product.product_id,
                    date=datetime.now(),
                )
            return product
        finally:
            message_bus.handle(view_event)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with id:{product_id} not found",
    )


@router.put("/{product_id}", response_model=ProductDBSchema)
def update_product(
    product_id: int,
    new_product: ProductUpdateSchema,
    product_service: ProductService = Depends(get_product_services),
    token: str = Depends(AuthSchema),
    current_user: ProductDBSchema = Security(
        get_current_user_from_service, scopes=[UserRoles.admin.value]
    ),
) -> ProductDBSchema:
    try:
        product_updated: ProductDBSchema = product_service.update_product(
            product_id, new_product
        )
        update_event = UpdateProduct(
            user_id=current_user.user_id,
            product_id=product_id,
            change=new_product.dict(exclude_unset=True),
            date=datetime.now(),
        )
        return product_updated
    finally:
        message_bus.handle(update_event)


@router.delete("/{product_id}", response_model=ProductDBSchema)
def remove_product(
    product_id: int,
    product_service: ProductService = Depends(get_product_services),
    token: str = Depends(AuthSchema),
    current_user: ProductDBSchema = Security(
        get_current_user_from_service, scopes=[UserRoles.admin.value]
    ),
) -> ProductDBSchema:
    product_removed: ProductDBSchema = product_service.remove_product(
        product_id
    )
    return product_removed
