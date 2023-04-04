import logging
import json

from domain.user.factory import UserFactory
from domain.user.persistance_interface import UserPersistenceInterface
from domain.user.user import User


class UserRepo:
    def __init__(self, persistence: UserPersistenceInterface):
        self.__persistence = persistence
        self.logger = logging.getLogger(__name__)
        self.__users = None
        logging.basicConfig(filename='user_repo.log', level=logging.DEBUG)

    def add(self, new_user: User):
        # TODO homework, refactor to not have duplicate code + add for get_by_id
        if self.__users is None:
            self.__users = self.__persistence.get_all()
        self.__users.append(new_user)
        self.__persistence.add(new_user)

    def get_all(self) -> list[User]:
        if self.__users is None:
            self.__users = self.__persistence.get_all()
        return self.__users

    def get_by_username(self, username: str) -> User:
        for u in self.__users:
            if u.username == username:
                return u

    def get_by_id(self, user_id: str) -> User:
        for u in self.__users:
            if u.id == user_id:
                return u

    def delete(self, user_id: str):
        user_to_delete = self.get_by_id(user_id)
        if user_to_delete:
            self.__users.remove(user_to_delete)
            users_info = [(str(x.id), x.username, x.stocks) for x in self.__users]
            users_json = json.dumps(users_info)
            file = open(self.file_path, "w")
            file.write(users_json)
            file.close()
            return True
        else:
            return False
