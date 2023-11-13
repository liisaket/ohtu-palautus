import re
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

        user = self._user_repository.find_by_username(username)

        #Register With Already Taken Username And Valid Password
        if user and self.valid_password(password):
            raise UserInputError("Username is taken")

        # Register With Too Short Username And Valid Password
        if len(username) < 3 and self.valid_password(password):
            raise UserInputError("Username is too short")

        # Register With Enough Long But Invalid Username And Valid Password
        if not bool(re.search(r'^[a-z]+$', username)) \
            and len(username) >= 3 and self.valid_password(password):
                raise UserInputError("Username invalid")

        # Register With Valid Username And Too Short Password
        if self.valid_username(username) and len(password) < 8:
            raise UserInputError("Password is too short")
    
        # Register With Valid Username And Long Enough Password Containing Only Letters
        if self.valid_username and len(password) >= 8 and not bool(re.search(r'\d', password)):
            raise UserInputError("Password has to contain letters and numbers")
    
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
