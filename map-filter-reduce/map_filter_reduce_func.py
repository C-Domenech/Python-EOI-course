import functools


# for alternatives using map, filter and reduce
def my_new_total(numbers):
    new_odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
    print("New odd numbers:", new_odd_numbers)
    new_squared_odd_numbers = list(map(lambda x: x * x, new_odd_numbers))
    print("New squared odd numbers:", new_squared_odd_numbers)
    new_total = functools.reduce(lambda x, y: x + y, new_squared_odd_numbers)
    print("> New total:", new_total)


numbers = []
for i in range(5):
    numbers.append(int(input('Introduce un número: ')))

my_new_total(numbers)
