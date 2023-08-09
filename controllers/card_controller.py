from schemas.account import Account
from schemas.card import Card
from typing import Union


class CardController:
    # Create method
    @staticmethod
    def create_card(account: Account, name: str, cvv: str) -> Card:
        # Validations
        assert isinstance(account, Account), 'account must be instance of Account class'
        assert len(name) > 0, 'Name must have a value'
        assert len(cvv) > 0 and len(cvv) == 3, 'cvv must have 3 characters'

        card = Card(account_id=account.id, name=name, cvv=cvv)
        card.save()
        return card

    # Read methods
    @staticmethod
    def get_card_by_id(card_id: int) -> Union[Card, None]:
        # Validations
        assert isinstance(card_id, int), 'card_id must be integer'

        try:
            return Card.get(id=card_id)
        except Card.DoesNotExist:
            print('Card not found.')
            return None

    @staticmethod
    def get_card_by_account(account: Account) -> Union[Card, None]:
        # Validations
        assert isinstance(account, Account), 'account must be instance of Account class'

        try:
            return Card.filter(account_id=account.id)
        except Card.DoesNotExist:
            print('Card not found.')
            return None

    # Update methods
    @staticmethod
    def update_cvv(card: Card, cvv: str) -> bool:
        # Validations
        assert isinstance(card, Card), 'card must be instance of Card class'
        assert len(cvv) > 0 and len(cvv) == 3, 'cvv must have 3 characters'

        card.cvv = cvv
        card.save()
        return True

    # Delete methods
    @staticmethod
    def delete_card(card: Card):
        # Validations
        assert isinstance(card, Card), 'card must be instance of Card class'

        try:
            account = Account.get(id=card.account_id)
            balance = account.balance
            if balance == 0:
                card.delete_instance()
            else:
                print('Balance must be zero to delete card')
        except Account.DoesNotExist:
            print('Not found.')
