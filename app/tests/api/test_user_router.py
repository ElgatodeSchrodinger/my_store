from typing import Any, List
from domain.auth.authUtils import get_current_user_from_service
from domain.userManagment.userConstants import UserRoles

import pytest
from fastapi import FastAPI
from starlette import status
from starlette.testclient import TestClient

from api.api import api_router
from api.utils import get_user_services
from domain.userManagment.userSchema import UserDBSchema
from infrastructure.database.models.user import UserModel

FAKE_TOKEN = "eyJhbG.arGiJVjDp9lRezwxx2qLU33TG5O892nozvgKv1t_iHg"


def create_test_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)

    return app


app = create_test_app()
client = TestClient(app)

USER_MODEL = UserModel(
    user_id=1,
    email="test@test.com",
    full_name="test",
    password="test",
    is_active=True,
    rol=UserRoles.admin,
    created_date="1/1/2020",
)

USER_DB_SCHEMA = UserDBSchema(
    user_id=1,
    email="test@test.com",
    full_name="test",
    is_active=True,
    rol=UserRoles.admin,
    created_date="1/1/2020",
)


class UserServiceDummy:
    def create_user(self, user: Any) -> UserModel:
        return USER_DB_SCHEMA

    def get_user_by_id(self, id: int) -> UserModel:
        return USER_DB_SCHEMA

    def update_user(self, id: int, new_user: Any) -> UserModel:
        return USER_DB_SCHEMA

    def remove_user(self, id: int) -> UserModel:
        return USER_DB_SCHEMA


def get_user_services_dummy() -> UserServiceDummy:
    return UserServiceDummy()


def get_current_user_from_service_dummy() -> UserModel:
    return USER_MODEL


app.dependency_overrides[get_user_services] = get_user_services_dummy
app.dependency_overrides[
    get_current_user_from_service
] = get_current_user_from_service_dummy


@pytest.fixture
def user_model() -> UserModel:
    return USER_MODEL


@pytest.fixture
def user_schema() -> UserDBSchema:
    return UserDBSchema(
        user_id=1,
        email="test@test.com",
        full_name="test",
        is_active=True,
        rol=UserRoles.admin,
        created_date="1/1/2020",
    )


class TestUserRouter:
    def test_user_create_valide(
        self, user_model: UserModel, user_schema: UserDBSchema
    ) -> None:

        response = client.post(
            "/users/",
            json={
                "email": "test@test.com",
                "full_name": "test",
                "password": "test",
                "is_active": True,
                "rol": "admin",
                "created_date": "1/1/2020",
            },
        )
        assert response.status_code == status.HTTP_200_OK
        assert UserDBSchema(**response.json()) == user_schema

    def test_user_update(
        self, user_model: UserModel, user_schema: UserDBSchema
    ) -> None:

        response = client.put(
            "/users/1",
            json={
                "email": "test@test.com",
                "full_name": "test",
                "password": "test",
                "is_active": True,
                "rol": "admin",
                "created_date": "1/1/2020",
            },
            headers={"Authorization": f"Bearer {FAKE_TOKEN}"},
        )
        assert response.status_code == status.HTTP_200_OK
        assert UserDBSchema(**response.json()) == user_schema

    def test_user_delete(
        self, user_model: UserModel, user_schema: UserDBSchema
    ) -> None:

        response = client.delete(
            "/users/1", headers={"Authorization": f"Bearer {FAKE_TOKEN}"}
        )
        assert response.status_code == status.HTTP_200_OK
        assert UserDBSchema(**response.json()) == user_schema

    def test_user_get_byid(
        self, user_model: UserModel, user_schema: UserDBSchema
    ) -> None:

        response = client.get(
            "/users/1", headers={"Authorization": f"Bearer {FAKE_TOKEN}"}
        )
        assert response.status_code == status.HTTP_200_OK
        assert UserDBSchema(**response.json()) == user_schema
