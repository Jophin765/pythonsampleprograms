import math


def generate_bill(fee, medicine):
    return math.ceil(fee + medicine)
