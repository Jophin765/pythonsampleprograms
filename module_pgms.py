'''import math

print(math.pi)
print(math.sqrt(49))
print(math.pow(2,3))

from math import sqrt
print(sqrt(49))

import random  # this module used to print random numbers,letters
print(random.randint(150,300))

import string
random_letter=random.choice(string.ascii_letters)
print(random_letter)
small_letter=random.choice(string.ascii_lowercase)
capital_letter=random.choice(string.ascii_uppercase)

print(small_letter)
print(capital_letter)

num=[1,2,3,4,5,6,7,8,9,10]
print(random.choice(num))
print(random.sample(num,k=3))

#try out secret module and more of random and math


import datetime  

print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.date.today()-datetime.timedelta(1))  # timedelta:-used to sub or add time
print(datetime.date.today()+datetime.timedelta(1))  # tomorrow

# try out random dates b/w specific days
#2025 and 2026 edayil olla random date
from datetime import datetime
now=datetime.now()
current_time=now.time()
print(current_time)

import sys
print(sys.platform)
print(sys.version)
import os
print(os.getcwd())
print(os.listdir())


import datetime  as dt 
print(dt.datetime.now())

import requests 
#check out module reloading:-“Module reloading means loading the module again after we make changes to it, so that Python uses the updated code.”


api




import datetime
print(datetime.date.today()+datetime.timedelta(1))

'''

import requests
url=requests.get('https://jsonplaceholder.typicode.com/users/1')
print(url.json())
