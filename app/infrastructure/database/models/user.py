from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum
from sqlalchemy.sql import func
from typing import List
from fastapi.encoders import jsonable_encoder
from  core.db import Base, engine, get_db
from  domain.userManagment.queriesInterface import IUserQueries
from  domain.userManagment.userSchema import UserCreateSchema, UserUpdateSchema
from  domain.userManagment.userConstants import UserRoles

class UserModel(Base):
    __tablename__ = "users"

    user_id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    full_name = Column(String ) 
    password = Column(String )
    is_active = Column(Boolean, nullable=False)
    rol = Column(Enum(UserRoles), nullable=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class UserQueries(IUserQueries):

    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.session = next(get_db())

    def create_user(self, user: UserCreateSchema) -> UserModel:
        user_data = jsonable_encoder(user)
        user_obj = UserModel(**user_data)
        with self.session as session:
            session.add(user_obj)
            session.commit()
            session.flush()
            session.refresh(user_obj)
        return user_obj

    def update_user(self, old_user: UserModel, new_user: UserUpdateSchema) -> UserModel:
        with self.session as session:
            data = new_user.dict(exclude_unset=True)
            session.query(UserModel).filter_by(user_id=old_user.user_id).update(data)
            session.commit()
            user_updated = session.query(UserModel).filter_by(user_id=old_user.user_id).first()
        return user_updated

    def delete_user(self, user_id: int) -> UserModel:
        with self.session as session:
            user_obj = session.query(UserModel).get(user_id)
            session.delete(user_obj)
            session.commit()
        return user_obj

    def get_user_byid(self, user_id: int) -> UserModel:

        with self.session as session:
            user_obj = session.query(UserModel).filter_by(user_id=user_id, is_active=True).first()
        return user_obj

    def get_user_byemail(self, user_email: str) -> UserModel:

        with self.session as session:
            user_obj = session.query(UserModel).filter_by(email=user_email, is_active=True).first()
        return user_obj
    
    def get_admin_emails(self):
        with self.session as session:
            admin_users = session.query(UserModel).filter_by(rol=UserRoles.admin).all()
        return [
            admin.email for admin in admin_users
        ]