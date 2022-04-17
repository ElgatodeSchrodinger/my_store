from  domain.userManagment.userService import UserService
from  infrastructure.database.models.user import UserQueries
from infrastructure.auth.hash import Hash

def get_user_services() -> UserService:
    return UserService(UserQueries(), Hash())