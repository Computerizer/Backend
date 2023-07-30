from .models import cpu, gpu, ram, motherboard, case, aircooler, watercooler, ssd, hdd, fan, case, psu
from datetime import datetime, timedelta
from .scraper import *


def cpuUpdate(part) -> float:
    oldPrice = part.current_price
    try:
        amazon = amazonPrice(part.url)
    except Exception:
        print(f'Error in Amazon Web Scrpaer Price ({datetime.now()})')
        print('-')
        print(Exception)
    try:
        newegg = neweggPrice(part.url)
    except Exception:
        print(f'Error in Newegg Web Scrpaer Price ({datetime.now()})')
        print('-')
        print(Exception)
    if amazon < newegg:
        link = part.amazon_url
        newPrice = amazon
        part.update(current_price=newPrice, previous_price=oldPrice,\
        amazon_price=amazon, newegg_price=newegg, lowest_Price_Link=link)
        part.save()
        return
    elif amazon > newegg:
        link = part.newegg_url
        newPrice = newegg
        part.update(current_price=newPrice, previous_price=oldPrice,\
        amazon_price=amazon, newegg_price=newegg, lowest_Price_Link=link)
        part.save()
        return


def gpuUpdate(url) -> float:
    pass


def ramUpdate(ur) -> float:
    pass


def moboUpdate(url) -> float:
    pass


def aircoolerUpdate(url) -> float:
    pass


def watercoolerUpdate(url) -> float:
    pass


def storageUpdate(url) -> float:
    pass


def psuUpdate(url) -> float:
    pass


def caseUpdate(url) -> float:
    pass


def main() -> float:
    pass
