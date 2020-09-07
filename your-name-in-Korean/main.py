# Escribe un programa que permita al usuario introducir su fecha de nacimiento y que el programa
# le muestre su nombre en coreano.
# Crea un módulo que gestione la entrada de la fecha de nacimiento y devuelva los valores necesarios
# como variables
# Utiliza la relación de claves de la imagen adjunta ("tu nombre en coreano")

from app_pkg.your_name_in_Korean import data_input


if __name__ == '__main__':
    birthdate = input('Introduce tu fecha de nacimiento (dd/mm/AAAA): ')
    data_input(birthdate)
