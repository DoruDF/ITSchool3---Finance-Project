import json

from domain.user.factory import UserFactory
from domain.user.persistence_interface import UserPersistenceInterface
from domain.user.user import User

# TODO (not homework) singleton
class UserRepo:
    def __init__(self, persistence: UserPersistenceInterface):
        self.__persistence = persistence
        self.__users = None

    def add(self, new_user: User):
        self.check_users_not_none()
        self.__users.append(new_user)
        self.__persistence.add(new_user)

    def get_all(self) -> list[User]:
        self.check_users_not_none()
        return self.__users

    def get_by_username(self, username) -> User:
        self.check_users_not_none()
        for u in self.__users:
            if u.username == username:
                return u

    def get_by_id(self, user_id) -> User:
        self.check_users_not_none()
        for u in self.__users:
            if u.id == user_id:
                return u

    def check_users_not_none(self):
        if self.__users is None:
            self.__users = self.__persistence.get_all()
