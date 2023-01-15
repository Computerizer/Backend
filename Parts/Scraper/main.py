from time import sleep, thread_time
from bs4 import BeautifulSoup as bs4
import requests
from selenium import webdriver

# ------- AMAZON --- NEWEGG --- BESTBUY ------- WEBSCRAPER ------- #

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
'accepted-language': 'en-US',
'referer': 'https://www.google.com/'}


def amazonPrice(url) -> float:
    # Gets all page content #
    page = requests.get(url, headers=headers).text
    r = bs4(page, 'lxml')

    # Gets price and decimal value separate #
    price = r.find('span', class_='a-price-whole').text
    decimal = r.find('span', class_='a-price-fraction').text

    return (price.rstrip(price[-1]) + '.' + decimal)


def amazonSale(url) -> float:
    # Gets all page content #
    page = requests.get(url, headers=headers).text
    r = bs4(page, 'lxml')
    salePercent = r.find('span', class_='a-size-large a-color-price\
    savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin\
    savingsPercentage').text
    if salePercent is not None:
        return (salePercent[1:-1])
    else:
        return float(0)


def neweggPrice(url) -> float:
    # Gets all page content #
    page = requests.get(url, headers=headers).text
    r = bs4(page, 'lxml')
    cls = r.find('li', class_='price-current')
    fullPrice = cls.text

    return float(fullPrice[1:].replace(',', ''))


def neweggSale(url) -> float:
    # Gets all page content #
    page = requests.get(url, headers=headers).text
    r = bs4(page, 'lxml')

    # Gets price and decimal value separate #
    oldprice = r.find('span', class_='price-was-data').text
    oldprice = float(oldprice[1:].replace(',', ''))
    newprice = neweggPrice(url)

    sale = 100 - ((newprice/oldprice)*100)
    return (float(round(sale, 1)))
