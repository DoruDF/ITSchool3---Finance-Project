import re

from domain.user.user import User


class InvalidUsername(Exception):
    pass


class UserFactory:
    def make(self, username: str) -> User:
        if len(username) < 6:
            raise InvalidUsername("Username should have at least 6 characters")
        elif len(username) > 20:
            raise InvalidUsername("Username should have at most 20 characters")
        return User(username)
