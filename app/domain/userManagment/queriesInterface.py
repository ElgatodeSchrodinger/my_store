# used only for python >=3.6
from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, List

from domain.userManagment.userSchema import UserCreateSchema, UserUpdateSchema

if TYPE_CHECKING:
    from infrastructure.database.models.user import UserModel


class IUserQueries:
    @abstractmethod
    async def create_user(self, user: UserCreateSchema) -> UserModel:
        raise NotImplementedError

    @abstractmethod
    async def update_user(
        self, old_user: UserModel, new_user: UserUpdateSchema
    ) -> UserModel:
        raise NotImplementedError

    @abstractmethod
    async def delete_user(self, user_id: int) -> UserModel:
        raise NotImplementedError

    @abstractmethod
    async def get_user_byid(self, user_id: int) -> UserModel:
        raise NotImplementedError

    @abstractmethod
    async def get_user_byemail(self, user_email: str) -> UserModel:
        raise NotImplementedError

    @abstractmethod
    async def get_admin_emails(self) -> List[str]:
        raise NotImplementedError
