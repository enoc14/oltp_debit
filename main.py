from db.migrations import create_db

from controllers.user_controller import UserController
from controllers.account_controller import AccountController
from controllers.card_controller import CardController

from schemas.user import User
from schemas.account import Account
from schemas.card import Card


def print_users():
    print('Users:')
    users = User.select()
    if users:
        for user in users:
            print(f'id: {user.id}, name: {user.name}, age: {user.age}, city: {user.city}')
    else:
        print('No users to print')


def print_accounts():
    print('Accounts:')
    accounts = Account.select()
    if accounts:
        for account in Account.select():
            print(f'id: {account.id}, user_id: {account.user_id},'
                  f'balance: {account.balance}, open_date: {account.open_date}')
    else:
        print('No accounts to print')


def print_cards():
    print('Cards:')
    cards = Card.select()
    if cards:
        for card in Card.select():
            print(f'id: {card.id}, account_id: {card.account_id}, name: {card.name}, cvv: {card.cvv}')
    else:
        print('No cards to print')


def print_results():
    print_users()
    print_accounts()
    print_cards()
    print('\n')


if __name__ == '__main__':
    create_db('db/db_oltp_debit.db')

    # Create John and Michael users
    john = UserController.create_user(name='John Doe', age=40, city='New York')
    michael = UserController.create_user(name='Michael Scott', age=55, city='New Jersey')

    # Create account for the users
    john_banamex = AccountController.create_account(user=john, balance=75_000)
    michael_bbva = AccountController.create_account(user=michael, balance=25_000)

    # Create cards for the users
    john_gold = CardController.create_card(account=john_banamex, name='Gold Card', cvv='653')
    michael_plus = CardController.create_card(account=michael_bbva, name='Plus Card', cvv='921')

    # Print results
    print('Results of creations:')
    print_results()

    # Update user name
    UserController.update_name(user=michael, name='Michael Jackson')

    # Update account balance
    AccountController.update_balance(account=john_banamex, amount=-75_000)
    AccountController.update_balance(account=michael_bbva, amount=-25_000)

    # Update card cvv
    CardController.update_cvv(card=michael_plus, cvv='163')
    CardController.update_cvv(card=john_gold, cvv='872')

    # Print updated results
    print('Results after updates:')
    print_results()

    # Delete cards
    CardController.delete_card(card=john_gold)
    CardController.delete_card(card=michael_plus)

    # Delete accounts
    AccountController.delete_account(account=michael_bbva)
    AccountController.delete_account(account=john_banamex)

    # Delete users
    UserController.delete_user(user=john)
    UserController.delete_user(user=michael)

    # Print deleted results
    print('Results after deletions:')
    print_results()
