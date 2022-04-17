from typing import Any, List, Optional

from  domain.userManagment.userSchema import UserCreateSchema, UserDBSchema, UserUpdateSchema


class UserService:
    def __init__(self, user_queries: Any):
        self.__user_queries = user_queries

    def create_user(self, user: UserCreateSchema) -> UserDBSchema:
        new_user = self.__user_queries.create_user(user)
        return UserDBSchema.from_orm(new_user)

    def get_user_by_id(self, user_id: int) -> Optional[UserDBSchema]:
        user = self.__user_queries.get_user_byid(user_id)
        if user:
            return UserDBSchema.from_orm(user)
        else:
            return None

    def update_user(self, user_id: int, new_user: UserUpdateSchema) -> UserDBSchema:
        old_user = self.__user_queries.get_user_byid(user_id)
        user_updated = self.__user_queries.update_user(old_user, new_user)
        return UserDBSchema.from_orm(user_updated)

    def remove_user(self, user_id: int) -> UserDBSchema:
        user_removed = self.__user_queries.delete_user(user_id)
        return UserDBSchema.from_orm(user_removed)