from data_dicts_pkg.korean_dicts import *


def data_input(full_birthdate):
    split_birthdate = full_birthdate.split('/')
    your_name_in_korean(day=split_birthdate[0], month=split_birthdate[1], year=split_birthdate[2])


def your_name_in_korean(day, month, year):
    last_name = year_dict[int(year[-1])]
    middle_name = month_dict[int(month)]
    first_name = day_dict[int(day)]
    print(last_name, middle_name, first_name)
