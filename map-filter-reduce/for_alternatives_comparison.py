import functools
from colorama import Fore

numbers = [1, 2, 3, 4, 5, 6]

# BEST: Using filter, map and reduce
new_odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
print(Fore.BLUE, "> New odd numbers:", new_odd_numbers)

new_squared_odd_numbers = list(map(lambda x: x * x, new_odd_numbers))
print(Fore.BLUE, "> New squared odd numbers:", new_squared_odd_numbers)

new_total = functools.reduce(lambda x, y: x + y, new_squared_odd_numbers)
print(Fore.BLUE, "> New total:", new_total)

# ORIGINAL
odd_numbers = []
squared_odd_numbers = []
total = 0

# filter for odd numbers
for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)
print(Fore.RED, "> Original odd numbers:", odd_numbers)

# square all odd numbers
for number in odd_numbers:
    squared_odd_numbers.append(number * number)
print(Fore.RED, "> Original squared odd numbers:", squared_odd_numbers)

# calculate total
for number in squared_odd_numbers:
    total += number
print(Fore.RED, "> Original Total:", total)
