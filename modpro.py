"""
import math

print(math.pi)
print(math.sqrt(49))
print(math.pow(2,3))

from math import sqrt

print(sqrt(67))

import random
import string

print(random.randint(1,17))
random_letter=random.choice(string.ascii_letters)
print(random_letter)

small_letter=random.choice(string.ascii_lowercase)
print(small_letter)

capital_letter=random.choice(string.ascii_uppercase)
print(capital_letter)

nos=[1,3,4,7,8]
print(random.choice(nos))
print(random.sample(nos,k=3))

#secret module

#date and time module
import datetime

print(datetime.datetime.now())  # noqa: DTZ005
print(datetime.date.today())  # noqa: DTZ011
print(datetime.date.today()-datetime.timedelta(days=1))  # noqa: DTZ011

from datetime import datetime

now=datetime.now()  # noqa: DTZ005
currenttime=now.time()
print(currenttime)

import sys

print(sys.version)
print(sys.platform)

import os

print(os.getcwd())
print(os.listdir())"""

import datetime as dt

print(dt.datetime.now())  # noqa: DTZ005

import requests

response = requests.get("https://httpbin.org/get")
print(response.json())