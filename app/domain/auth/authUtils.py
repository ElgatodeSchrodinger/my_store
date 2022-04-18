from functools import wraps
from domain.userManagment.userService import UserService
from domain.userManagment.userSchema import UserDBSchema
from fastapi import HTTPException, status, Security, Depends
from fastapi.security import SecurityScopes
from api.utils import get_user_services
from domain.auth.authSchema import AuthSchema
# from fastapi import Request

# def validate_user_permission(rol):
#     pass

# def auth_required(func, rol):
#     @wraps(func)
#     async def wrapper(request: Request, *args, **kwargs):
#         validate_user_permission(request, rol)
#         return await func(*args, **kwargs)
#     return wrapper

def get_current_user_from_service(
    security_scopes: SecurityScopes,
    token: str = Depends(AuthSchema), 
    user_service=Depends(get_user_services),
    ):
    current_user = user_service.get_current_user(security_scopes=security_scopes, token=token)
    if not current_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized", headers={"WWW-Authenticate": "Bearer"})
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# async def get_current_active_user(
#     current_user: UserDBSchema = Security(get_current_user, scopes=["me"]),
#     user_service: UserService = Depends(),
#     token: str

# ):
#     if not current_user.is_active:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


# class auth_check(object):

#     def __init__(self, roles: dict):
#         """
#         If there are decorator arguments, the function
#         to be decorated is not passed to the constructor!
#         """
#         # print(roles)
#         self.roles = roles

#     def __call__(self, func):
#         """
#         If there are decorator arguments, __call__() is only called
#         once, as part of the decoration process! You can only give
#         it a single argument, which is the function object.
#         """
#         def wrapped_f(*args, **kwargs):
#             print("??????")
#             print(self.roles)
#             token = kwargs["token"]
#             user_service = kwargs["user_service"]
#             current_user = user_service.get_current_user(token)
#             user_role = current_user.rol
#             if user_role in self.roles:
#                 return func(*args, **kwargs)
#             return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized", headers={"WWW-Authenticate": "Bearer"})
#         return wrapped_f



# def auth_check(roles):
#     def decorator_auth(func):
#         @wraps(func)
#         def wrapper_auth(*args, **kwargs):
#             print("======")
#             print(args)
#             print(kwargs)
#             print("======")
#             token = kwargs["token"]
#             user_service = kwargs["user_service"]
#             current_user = user_service.get_current_user(token)
#             user_role = current_user.rol
#             if user_role in roles:
#                 return func(*args, **kwargs)
#             return HTTPException(status_code=401, detail="Unauthorized")
#         return wrapper_auth
#     return decorator_auth