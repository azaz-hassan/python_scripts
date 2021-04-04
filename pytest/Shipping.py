from datetime import datetime


class Shipping:
    def __init__(self):
        self.addresses = dict()
        self.countries = ['Azerbaijan', 'Belgium', 'Croatia',
                          'Deutschland', 'Ethiopia', 'Finland', 'Pakistan']
        self.shipping_rates = {'Azerbaijan': 3,
                               'Belgium': 5, 'Croatia': 5, 'Deutschland': 5,
                               'Ethiopia': 10, 'Finland': 7, 'Pakistan': 2}

        self.file = "clients.txt"
        self.fin = open(self.file, 'a+')

    def add(self, name, address):
        self.addresses[name] = address

    def search(self, name):
        return self.addresses[name]

    def findCountry(self, country):
        return country in self.countries

    def calculateShippingRates(self, country, itemBaseValue):
        """
          Shipping Rate is equal to 5% of base item value multiplied by country rates.
        """
        return (itemBaseValue * 0.05) * self.shipping_rates[country]

    def shippingDiscounts(self, totalItems, shippingRate):
        """
          Shipping Discount 30% if 2 to 5 items bought
         """
        if 6 > totalItems >= 2:
            return (shippingRate - (shippingRate * 0.30))
        elif totalItems == 1:
            return 0
        else:
            return shippingRate

    def writeTransactiontoFile(self, dateTime, name, shippingRate):
        self.fin.write(
            f'{dateTime} {name} was charged for Shipping: {shippingRate}\n')

    def readLastTransactionFromFile(self):
        self.fin.seek(0)
        lines = self.fin.readlines()
        print(lines[-1].strip())
        return (lines[-1].strip())

    def closeFile(self):
        self.fin.close()
