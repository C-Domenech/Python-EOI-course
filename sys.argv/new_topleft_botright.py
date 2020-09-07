from graphics import *
from random import randint
import sys

# Cambia el topleft_botright.py para que solo imprima los puntos
# en el centro. Hay que pasar los siguientes argumentos al programa:
# anchura de la ventana, altura de la ventana y número de puntos.

# Ejecutar en terminal, por ejemplo:
# python new_topleft_botright.py 400 400 1000

if len(sys.argv) == 4:
    ancho = int(sys.argv[1])
    alto = int(sys.argv[2])
    npuntos = int(sys.argv[3])
else:
    print("Error: Se esperaban 3 argumentos.")


def main():
    width = ancho
    height = alto

    win = GraphWin("Ejercicio 2 - Puntos", width, height)
    win.setBackground(color_rgb(0, 0, 0))

    for i in range(npuntos):
        # Get random position
        x = randint(int(width / 3), int(width / 1.5))
        y = randint(int(height / 3), int(height / 1.5))

        p = Point(x, y)

        # Get random color
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        p.setFill(color_rgb(r, g, b))
        p.draw(win)

    win.getMouse()
    win.close()


main()
