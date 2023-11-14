import re
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

        # Register With Too Short Username And Valid Password
        if len(username) < 3 and self.valid_password(password):
            raise UserInputError("Username is too short")

        # Register With Valid Username And Invalid Password
        if self.valid_username and not self.valid_password(password):
            raise UserInputError("Password is invalid")

        if password != password_confirmation:
            raise UserInputError("Passwords do not match")

    def valid_password(self, password):
        if len(password) >= 8 and bool(re.search(r'\d', password)):
            return True
        return False

    def valid_username(self, username):
        user = self._user_repository.find_by_username(username)
        if bool(re.search(r'^[a-z]+$', username)) \
            and len(username) >= 3 and not user:
                return True
        return False


user_service = UserService()
