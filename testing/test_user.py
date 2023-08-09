import pytest


class TestUser:
    # It should have all its params
    def test_user_params(self):
        name = 'John Doe'
        city = 'New York'
        age = 25

        assert name == 'John Doe'
        assert city == 'New York'
        assert age == 25

    # It should raise an error if name don't have value
    def test_user_name(self):
        name = ''

        assert len(name) > 0

    # It should raise an error if city don't have value
    def test_user_city(self):
        city = ''

        assert len(city) > 0

    # It should raise an error if age is not between 18 and 60
    def test_user_age(self):
        age = 17

        assert 18 <= age < 60
