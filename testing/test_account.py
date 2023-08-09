import datetime
import pytest


class TestAccount:
    # It should have all its params
    def test_account_params(self):
        now = datetime.datetime.now()
        balance = 100
        open_date = now

        assert balance == 100
        assert open_date == now

    # It should pass if balance is greater than 0
    def test_account_balance(self):
        balance = 500

        assert balance > 0

    # It should pass if balance is float or int
    def test_account_balance_type(self):
        balance = 400

        assert isinstance(balance, (int, float))

    # It should raise an error if open_date is not a datetime class
    def test_account_open_date(self):
        open_date = '2023-08-10'

        assert isinstance(open_date, datetime.datetime)
