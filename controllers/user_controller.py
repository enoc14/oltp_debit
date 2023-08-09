from schemas.user import User
from schemas.account import Account
from controllers.account_controller import AccountController
from typing import Union


class UserController:
    # Create method
    @staticmethod
    def create_user(
            name: str,
            city: str,
            age: int) -> User:

        # Validations
        assert len(name) > 0, 'Name must have a value'
        assert len(city) > 0, 'City must have a value'
        assert 18 < age <= 60, 'Age must be between 18 and 60'

        user = User(name=name, age=age, city=city)
        user.save()
        return user

    # Read methods
    @staticmethod
    def get_user_by_id(user_id: int) -> Union[User, None]:
        # Validations
        assert isinstance(user_id, int), 'user_id must be integer'

        try:
            return User.get(id=user_id)
        except User.DoesNotExist:
            print('User not found.')
            return None

    @staticmethod
    def get_user_by_name(name: str) -> Union[User, None]:
        # Validations
        assert len(name) > 0, 'Name must have a value'

        try:
            return User.get(name=name)
        except User.DoesNotExist:
            print('User not found.')
            return None

    # Update methods
    @staticmethod
    def update_name(user: User, name: str) -> User:
        # Validations
        assert isinstance(user, User), 'user must be instance of User class'
        assert len(name) > 0, 'Name must have a value'

        user.name = name
        user.save()
        return user

    # Delete methods
    @staticmethod
    def delete_user(user: User):
        # Validations
        assert isinstance(user, User), 'user must be instance of User class'

        try:
            account = Account.get(user_id=user.id)
        except Account.DoesNotExist:
            account = None

        if account is None:
            user.delete_instance()
        else:
            AccountController.delete_account(account)
            user.delete_instance()
