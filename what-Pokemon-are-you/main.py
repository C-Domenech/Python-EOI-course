# EJERCICIO 2 TEMA 15 - MÓDULOS Y PAQUETES
#
# Escribe un programa que permita al usuario introducir su nombre y apellido y que devuelva
# el número de pokemon que le corresponde.
# Las reglas para calcular éste las tienes en la imagen adjunta ("Pokemon")
# Crea el módulo que contenga las funciones que permiten gestionar el nombre y el apellido
# y extraer los números necesarios para el programa.

from app_pkg.what_pokemon_are_you import data_input

if __name__ == '__main__':
    birthdate = input('Introduce tu fecha de nacimiento (dd/mm/AAAA): ')
    name = input('Introduce tu nombre: ')
    data_input(birthdate, name)


