from time import sleep, thread_time
from bs4 import BeautifulSoup as bs4
import requests
from selenium import webdriver
from string import ascii_letters, whitespace

# ------- AMAZON --- NEWEGG --- BESTBUY ------- WEBSCRAPER ------- #

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        'accepted-language': 'en-US',
            'referer': 'https://www.google.com/'}


def proxy_request(url):
    payload = {
        "source": "universal",
        "url": url,
        "geo_location": "USA"
    }

# ------------------------ #
# --------- AMZN --------- #


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
        savingPriceOverride aok-align-center\
            reinventPriceSavingsPercentageMargin\
                savingsPercentage').text
    if salePercent is not None:
        return (float(round((salePercent[1:-1]), 1)))
    else:
        return float(0)


def amazonRating(url) -> float:
    # Gets all page content #
    page = requests.get(url, headers=headers).text
    r = bs4(page, 'lxml')
    # Gets price and decimal value separate #
    description = r.find('span', class_='a-icon-alt').text
    rating = description[0:3]
    rating = None
    return (float(round(rating, 0)))


# ------------------------ #
# --------- NEWG --------- #


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


def neweggRating(url) -> float:
    # Gets all page content #
    page = requests.get(url, headers=headers).text
    r = bs4(page, 'lxml')
    # Gets price and decimal value separate #
    container = r.find('div', class_='product-rating')
    inner = container.find(attrs={"class": "rating"})
    rating = inner.get('title')[0:3]
    return (float(round(rating, 0)))

# ------------------------ #
# --------- BSTBY -------- #


def bestbuyPrice(url) -> float:
    # Gets all page content #
    page = requests.get(url, headers=headers).text
    r = bs4(page, 'lxml')
    # Gets price and decimal value separate #
    container = r.find('div', class_='priceView-hero-price priceView-customer-price')
    inner = container.find_all('span')
    rating = inner[0].text
    return (float(rating[1:]))


def bestbuySale(url) -> float:
    # Gets all page content #
    page = requests.get(url, headers=headers).text
    r = bs4(page, 'lxml')
    ignore = ascii_letters + whitespace
    # Gets price and decimal value separate #
    oldPrice = float((r.find('div', class_='pricing-price__regular-price')\
        .text).translate(str.maketrans('', '', ignore))[1:])
    saleAmount = float((r.find('div', class_='pricing-price__savings')\
        .text).translate(str.maketrans('', '', ignore))[1:])
    salePercent = round((saleAmount/oldPrice)*100, 1)
    return (salePercent)


def bestbuyRating(url) -> float:
    # Gets all page content #
    page = requests.get(url, headers=headers).text
    r = bs4(page, 'lxml')
    # Gets price and decimal value separate #
    number = r.find('span', class_='ugc-c-review-average font-weight-medium order-1')
    stars = round(float(number.text), 0)
    return (float(stars))


# ------------------------ #
# ------------------------ #
