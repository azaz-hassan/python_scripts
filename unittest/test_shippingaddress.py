import unittest


from Shipping import Shipping


class ShippingAddressTest(unittest.TestCase):

    def setUp(self) -> None:
        self.shipping = Shipping()

    @unittest.skip("Still under development")
    def test_shippingAddress_search(self):
        self.shipping.add("Ali", "Katchehry Road, Lahore")
        self.assertEqual("Katchehry Road, Lahore",
                         self.shipping.search("Ali"))

    def test_address_not_found(self):
        with self.assertRaises(KeyError):
            self.shipping.search("Anything")

    def test_find_Country_exists(self):
        self.assertTrue(self.shipping.findCountry('Pakistan'))

    def test_find_Country_not_exists(self):
        self.assertFalse(self.shipping.findCountry('NewYork'))

    def test_calculate_Shipping_Rates(self):
        self.assertEqual(
            self.shipping.calculateShippingRates('Pakistan', 1000), 100)

    def test_shipping_Discounts_Full(self):
        self.assertEqual(self.shipping.shippingDiscounts(6, 100), 100)

    def test_shipping_Discounts_None(self):
        self.assertEqual(self.shipping.shippingDiscounts(1, 100), 0)

    def test_shipping_Discounts_30Percent(self):
        self.assertEqual(self.shipping.shippingDiscounts(3, 100), 70)


unittest.main()
