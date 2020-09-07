# v 3.0
import random
from colorama import Fore

__version__: '3.0'

def triangle_validation(s_one, s_two, s_three):
    if s_one + s_two > s_three and s_one + s_three > s_two and s_two + s_three > s_one:
        return True
    else:
        return False


def valid_triangle_generator(s_one, s_two, s_three):
    if s_three < s_one or s_three < s_two:
        while s_three + s_one <= s_two or s_three + s_two <= s_one:
            s_three += 1
        print(Fore.YELLOW + f">>> Un triángulo válido debería tener estas medidas: {s_one}, {s_two} y {s_three}")
    elif s_three > s_one or s_three > s_two:
        while s_three >= s_one + s_two:
            s_three -= 1
        print(Fore.YELLOW + f">>> Un triángulo válido debería tener estas medidas: {s_one}, {s_two} y {s_three}")


s_one = int(input("Introduce la medida del primer lado: "))
s_two = int(input("Introduce la medida del segundo lado: "))
s_three = int(input("Introduce la medida del tercer lado: "))

while s_one < 1 or s_two < 1 or s_three < 1:
    print("Los valores no pueden ser menores que uno.\nVuelve a introducir unos valores.")
    s_one = int(input("Introduce la medida del primer lado: "))
    s_two = int(input("Introduce la medida del segundo lado: "))
    s_three = int(input("Introduce la medida del tercer lado: "))

# test random sides
# s_one = random.randint(1, 500)
# s_two = random.randint(1, 500)
# s_three = random.randint(1, 500)

is_triangle = triangle_validation(s_one, s_two, s_three)
if is_triangle:
    print(Fore.BLUE + f"Las medidas {s_one}, {s_two} y {s_three} forman un triángulo.")
if not is_triangle:
    print(Fore.RED + f"Las medidas {s_one}, {s_two} y {s_three} NO forman un triángulo.")
    valid_triangle_generator(s_one, s_two, s_three)
