import unittest
from main import Scraper

class Scraper_Tests(unittest.TestCase):
    
    def test_Amazon_Price_Check(self):
        """Checks that AMAZON Scraper returns correct price"""
        price = Scraper('Ryzen', 'https://www.amazon.com/AMD-Ryzen-3600-12-Thread-Processor/dp/B07STGGQ18').get_price_amazon
        print(price)
        self.assertTrue(price == 144.95)

    def test_Newegg_Price_Check(self):
        """Checks that NEWEGG Scraper returns correct price"""
        price = Scraper('Ryzen', 'https://www.newegg.com/amd-ryzen-5-3600/p/N82E16819113569').get_price_newegg
        print(price)
        self.assertEqual(price, 2)

    def test_Bestbuy_Price_Check(self):
        """Checks that BESTBUY Scraper returns correct price"""
        price = Scraper('Ryzen', 'https://www.bestbuy.com/site/amd-ryzen-5-3600xt-3rd-gen-6-core-12-threads-unlocked-desktop-processor-with-wraith-spire-cooler/6422513.p').get_price_bestbuy
        print(price)
        self.assertEqual(price, 199.99)


if __name__ == "__main__":
    unittest.main()