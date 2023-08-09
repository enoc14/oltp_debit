from schemas.account import Account
from schemas.user import User
from schemas.card import Card
import datetime
from typing import Union

# CRUD (Create, Read, Update, Delete)


class AccountController:
    # Create account
    @staticmethod
    def create_account(
            user: User,
            balance: float,
            open_date: datetime = datetime.datetime.now()) -> Account:

        # Validations
        assert isinstance(user, User), 'user must be instance of User class'
        assert isinstance(balance, (float, int)), 'balance must be float'
        assert balance >= 0, 'balance must be greater than 0'

        account = Account(user_id=user.id, balance=balance, open_date=open_date)
        account.save()
        return account

    # Read methods
    @staticmethod
    def get_account_by_id(account_id: int) -> Union[Account, None]:
        # Validations
        assert isinstance(account_id, int), 'account_id must be integer'

        try:
            return Account.get(id=account_id)
        except Account.DoesNotExist:
            print('Account not found.')
            return None

    @staticmethod
    def get_account_by_user(user: User) -> Union[Account, None]:
        # Validations
        assert isinstance(user, User), 'user must be instance of User class'

        try:
            return Account.get(user_id=user.id)
        except Account.DoesNotExist:
            print('Account not found.')
            return None

    @staticmethod
    def get_account_by_card(card: Card) -> Union[Account, None]:
        # Validations
        assert isinstance(card, Card), 'card must be instance of Card class'

        try:
            return Account.get(id=card.account_id)
        except Account.DoesNotExist:
            print('Account not found.')
            return None

    # Update methods
    @staticmethod
    def update_balance(account: Account, amount: float) -> bool:
        # Validations
        assert isinstance(account, Account), 'account must be instance of Account class'
        assert isinstance(amount, (float, int)), 'amount must be float'

        balance = account.balance + amount
        if balance >= 0:
            account.balance = balance
            account.save()
            return True
        else:
            print('Not enough balance')
            return False

    # Delete methods
    @staticmethod
    def delete_account(account: Account):
        # Validations
        assert isinstance(account, Account), 'account must be instance of Account class'

        try:
            card = Account.get(id=account.id)
        except Account.DoesNotExist:
            card = None

        if card is None:
            account.delete_instance()
        else:
            card.delete_instance()
            account.delete_instance()
