from fastapi import APIRouter

from api.endpoints import product, user, auth

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(product.router, prefix="/products", tags=["products"])
