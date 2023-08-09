import pytest


class TestCard:
    # It should have all its params
    def test_card_params(self):
        name = 'Oro'
        cvv = '321'

        assert name == 'Oro'
        assert cvv == '321'

    # It should raise an error if city don't have value
    def test_card_city(self):
        city = ''

        assert len(city) > 0

    # It should pass if cvv is equal to 3 chars
    def test_card_cvv(self):
        cvv = '613'

        assert len(cvv) == 3
