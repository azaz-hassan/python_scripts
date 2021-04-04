# Azaz Hassan Jafri - BITF17M010


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


shipping_rates = {'Azerbaijan': 3,
                  'Belgium': 5, 'Croatia': 5, 'Deutschland': 5,
                  'Ethiopia': 10, 'Finland': 7, 'Pakistan': 2}


def calculateShippingRates(country, itemBaseValue):
    """
    >>> calculateShippingRates("Pakistan", 1000)
    100.0
    >>> calculateShippingRates("Azerbaijan", 1000)
    150.0
    >>> calculateShippingRates("Croatia", 500)
    125.0
    """
    return (itemBaseValue * 0.05) * shipping_rates[country]
