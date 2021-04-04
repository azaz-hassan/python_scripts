import pytest
from datetime import datetime

from Shipping import Shipping


@pytest.mark.instant
def test_shippingAddress_search(_shipping):
    _shipping.add("Ali", "Katchehry Road, Lahore")
    assert "Katchehry Road, Lahore" == _shipping.search("Ali")


@pytest.mark.instant
def test_find_Country_exists(_shipping):
    assert True == _shipping.findCountry("Pakistan")


@pytest.mark.instant
def test_find_Country_not_exists(_shipping):
    assert False == _shipping.findCountry("Mongolia")


@pytest.mark.skip
def test_check_Rate(_shipping):
    pass


@pytest.mark.slow
def test_read_Last_Transaction_From_File(_shipping):
    time = str(datetime.now())
    name = "Abdullah"
    ship_rate = 166.60
    expected = f'{time} {name} was charged for Shipping: {ship_rate}'
    _shipping.writeTransactiontoFile(time, name, ship_rate)
    assert expected == _shipping.readLastTransactionFromFile()


@pytest.mark.parametrize("totalItems, ship_rate, expected_discount",
                         [(6, 100, 100),
                          (1, 100, 0),
                             (3, 100, 70)])
def test_shipping_Discounts(totalItems, ship_rate, expected_discount):
    assert expected_discount == shippingDiscounts(totalItems, ship_rate)


@pytest.fixture
def _shipping():
    """
      This is initialization of shipping object
    """
    ship = Shipping()
    yield ship
    ship.closeFile()


def shippingDiscounts(totalItems, shippingRate):
    """
      Shipping Discount 30% if 2 to 5 items bought
     """
    if 6 > totalItems >= 2:
        return (shippingRate - (shippingRate * 0.30))
    elif totalItems == 1:
        return 0
    else:
        return shippingRate
