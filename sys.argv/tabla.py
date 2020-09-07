import sys

# Ejecutar en terminal, por ejemplo:
# python tabla.py 5 4

# 0-> nombre del archivo 1,2-> argumentos
if len(sys.argv) == 3:
    #primer argumento
    filas = int(sys.argv[1])
    #segundo argumento
    columnas = int(sys.argv[2])

# si recibe los argumentos correctos realiza el programa
    if filas >= 1 and filas <= 9 and columnas >= 1 and columnas <= 9:

        for i in range(filas):
            for j in range(columnas):
                print("| * ", end="")
            print("|")
# si no son correctos, imprime mensaje de error
    else:
        print("Error: El número de filas o columnas es incorrecto.")
        print("Filas: Entre 1 y 9. Columnas: Entre 1 y 9.")
# si no es correcto, imprime mensaje de error
else:
    print("Debe introducir el número de filas y el número de columnas de la tabla.")
