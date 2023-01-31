from .models import *

JSON = {
    'Budget': 4000,
    'FPS': 144,
    'Res': '4k',
    'Game Type': 'AAA',
    'Form Factor': 'ATX',
    'Purpose': 'Table Top',
    'Theme': ['Dark', 'RGB'],
    'Question': {'Q1': None, 'Q2': None}
}

partPercentages = {500: 
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    750:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    1000:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    1250:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    1500:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    1750:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    2000:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    2250:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    2500:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    2750:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    3000:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    3250:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    3500:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    3750:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    4000:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    4250:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    4500:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    4750:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    5000:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},}

cache = dict()

def params(JSON):
    global partPercentages
    price = JSON['Budget']
    percents = partPercentages[price]


def get_cpu():
    pass


def get_mobo():
    pass


def get_mobo():
    pass


def get_gpu():
    pass
