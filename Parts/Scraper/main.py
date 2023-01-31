from string import ascii_letters, whitespace
import requests
from bs4 import BeautifulSoup as bs4
from fake_useragent import UserAgent
from requests.adapters import HTTPAdapter
from random import choice, random
import time

# ------- AMAZON --- NEWEGG --- BESTBUY ------- WEBSCRAPER ------- #

# Create session object
session = requests.Session()
# Create an HTTP adapter that uses a pool of proxy IPs
adapter = HTTPAdapter(pool_connections=50, pool_maxsize=50)
session.mount('https://', adapter)

# User-Agent strings pool
user_agents = [
    'Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1',
    'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1',
    'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/94.0.4606.65',
    'Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.117 Mobile Safari/537.36 OPR/63.3.3216.58675'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70'

]

# ------------------------ #
# --------- AMZN --------- #


def amazonPrice(url) -> float:
    # Gets all page content #
    try:
        headers = {'User-Agent': choice(user_agents),
        'Origin': 'https://www.google.com', 'Referer': 'https://www.google.com'}
        page = session.get(url, headers=headers).content
    except Exception:
        headers = {'User-Agent': choice(user_agents),
        'Origin': 'https://www.google.com', 'Referer': 'https://www.google.com'}
        page = session.get(url, headers=headers).content
    r = bs4(page, 'lxml')
    # Gets price and decimal value separate #
    try:
        price = r.find('span', class_='a-price-whole').text
        decimal = r.find('span', class_='a-price-fraction').text
    except AttributeError:
        print('Fetching failed...')
        print('Amazon may have blocked scraper')
        return 'AMZ-F'
    return (price.rstrip(price[-1]) + '.' + decimal)


def amazonSale(url) -> float:
    # Gets all page content #
    try:
        headers = {'User-Agent': choice(user_agents),
        'Origin': 'https://www.google.com', 'Referer': 'https://www.google.com'}
        page = session.get(url, headers=headers).content
    except Exception:
        headers = {'User-Agent': choice(user_agents),
        'Origin': 'https://www.google.com', 'Referer': 'https://www.google.com'}
        page = session.get(url, headers=headers).content
    r = bs4(page, 'lxml')
    # Gets sale percentage #
    salePercent = r.find('span', class_='a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage').text
    if salePercent is not None:
        return (round(float(salePercent[1:-1]), 1))
    else:
        return float(0)


def amazonRating(url) -> float:
    # Gets all page content #
    try:
        headers = {'User-Agent': choice(user_agents),
        'Origin': 'https://www.google.com', 'Referer': 'https://www.google.com'}
        page = session.get(url, headers=headers).content
    except Exception:
        headers = {'User-Agent': choice(user_agents),
        'Origin': 'https://www.google.com', 'Referer': 'https://www.google.com'}
        page = session.get(url, headers=headers).content
    r = bs4(page, 'lxml')
    # Gets rating of product from amazon #
    description = r.find('span', class_='a-icon-alt').text
    rating = description[0:3]
    return (round(float(rating), 0))


# ------------------------ #
# --------- NEWG --------- #


def neweggPrice(url) -> float:
    """ Fetching Newegg product price given its url """
    # Gets all page content #
    try:
        headers = {'User-Agent': choice(user_agents),
        'Origin': 'https://www.google.com', 'Referer': 'https://www.google.com'}
        page = session.get(url, headers=headers).content
    except Exception:
        headers = {'User-Agent': choice(user_agents),
        'Origin': 'https://www.google.com', 'Referer': 'https://www.google.com'}
        page = session.get(url, headers=headers).content
    r = bs4(page, 'lxml')
    # Gets price and decimal value separate #
    price = r.find('li', class_='price-current').text
    return float(price[1:].replace(',', ''))


def neweggSale(url) -> float:
    """ Calculating newegg price | manually doesn't automatically fetch it """
    # Gets all page content #
    try:
        headers = {'User-Agent': choice(user_agents),
        'Origin': 'https://www.google.com', 'Referer': 'https://www.google.com'}
        page = session.get(url, headers=headers).content
    except Exception:
        headers = {'User-Agent': choice(user_agents),
        'Origin': 'https://www.google.com', 'Referer': 'https://www.google.com'}
        page = session.get(url, headers=headers).content
    r = bs4(page, 'lxml')
    # Gets new price and old price, then calculates sale #
    oldprice = r.find('span', class_='price-was-data').text
    oldprice = float(oldprice[1:].replace(',', ''))
    newprice = r.find('li', class_='price-current').text
    newprice = float(newprice[1:].replace(',', ''))
    sale = 100 - ((float(newprice)/float(oldprice))*100)
    return (float(round(sale, 1)))


def neweggRating(url) -> float:
    # Gets all page content #
    headers = {'User-Agent': choice(user_agents)}
    page = session.get(url, headers=headers, timeout=5)
    page.raise_for_status()

    r = bs4(page.content, 'lxml')
    # Gets price and decimal value separate #
    container = r.find('div', class_='product-rating')
    inner = container.find(attrs={"class": "rating"})
    rating = inner.get('title')[0:3]
    return (float(round(rating, 0)))

# ------------------------ #
# --------- BSTBY -------- #


def bestbuyPrice(url) -> float:
    # Gets all page content #
    headers = {'User-Agent': choice(user_agents)}
    page = session.get(url, headers=headers, timeout=5)
    page.raise_for_status()

    r = bs4(page.content, 'lxml')
    # Gets price and decimal value separate #
    container = r.find('div', class_='priceView-hero-price priceView-customer-price')
    inner = container.find_all('span')
    rating = inner[0].text
    return (float(rating[1:]))


def bestbuySale(url) -> float:
    # Gets all page content #
    headers = {'User-Agent': choice(user_agents)}
    page = session.get(url, headers=headers, timeout=5)
    page.raise_for_status()

    r = bs4(page.content, 'lxml')
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
    headers = {'User-Agent': choice(user_agents)}
    page = session.get(url, headers=headers, timeout=5)
    page.raise_for_status()

    r = bs4(page.content, 'lxml')
    # Gets price and decimal value separate #
    number = r.find('span', class_='ugc-c-review-average font-weight-medium order-1')
    stars = round(float(number.text), 0)
    return (float(stars))


# ------------------------ #
# ------------------------ #
