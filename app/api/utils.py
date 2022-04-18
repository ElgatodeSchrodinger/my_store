from  domain.userManagment.userService import UserService
from  infrastructure.database.models.user import UserQueries
from infrastructure.auth.jwt import JWT

def get_user_services() -> UserService:
    return UserService(UserQueries(), JWT())