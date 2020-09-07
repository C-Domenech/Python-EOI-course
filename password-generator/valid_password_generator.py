import random
from re import search
from constants import *


def password_generator():
    psw = ''
    for _ in range(random.randint(L_MIN, L_MAX)):
        psw = psw + chr(random.randint(ASC_START, ASC_END))
    return psw


def password_validate(psw):
    length = len(psw) >= 8
    upper = search(r'[A-Z]', psw)
    lower = search(r'[a-z]', psw)
    number = search(r'[0-9]', psw)
    # return length and upper and lower and number
    return all([length, upper, lower, number])
