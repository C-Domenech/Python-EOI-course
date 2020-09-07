# Crea una ventana con etiquetas y botones para un proyecto de interfaz online para 11_tests médicos
# La ventana debe tener un tamaño de 480x320px y un color de fondo gris claro. El estilo de borde debe ser "groove"
# La ventana debe tener como título "Test auditivo"
# Debe aparecer una etiqueta, en la parte superior, de fondo gris oscuro y letra en blanco, con el texto:
# 	"Pulse todos los botones que correspondan a cada sonido"
# La ventana debe tener cuatro botones: 
# 	- Botón 1 situado en el centro, arriba. Tamaño 12x5. Fondo de color azul y letra en blanco. Texto: Sonido agudo
#	- Botón 2 situado en el centro, abajo. Tamaño 12x5. Fondo de color naranja y letra en blanco. Texto: Sonido grave
#	- Botón 3 situado a la izquierda, en altura media. Tamaño 12x8. Fondo negro y letra en blanco. Texto: Oído izq
#	- Botón 4 situado a la derecha, en altura media. Tamaño 12x8. Fondo blanco y letra en negro. Texto: Oído derch

import tkinter as tk

window = tk.Tk()
window.geometry('400x320')
window.title('Test auditivo')
window.config(bg='#cccccc')

label = tk.Label(text='Pulse todos los botones que correspondan a cada sonido', fg='white', bg='#808080')
label.config(font=('Arial', 12))
label.pack()

b1 = tk.Button(text='Sonido agudo', bg='#0066ff', fg='white', width=12, height=3)
b1.config(font=('Arial', 10, 'bold'), activebackground='#80b3ff', cursor='hand2')
b1.pack()
b1.place(x=150, y=30)

b2 = tk.Button(text='Sonido grave', bg='#ff6600', fg='white', width=12, height=3)
b2.config(font=('Arial', 10, 'bold'), activebackground='#ffb380', cursor='hand2')
b2.pack()
b2.place(x=150, y=250)

b3 = tk.Button(text='Oído izq', bg='black', fg='white', width=12, height=5)
b3.config(font=('Arial', 10, 'bold'), activebackground='#bfbfbf', cursor='hand2')
b3.pack()
b3.place(x=20, y=125)

b4 = tk.Button(text='Oído derch', bg='white', fg='black', width=12, height=5)
b4.config(font=('Arial', 10, 'bold'), activebackground='#bfbfbf', cursor='hand2')
b4.pack()
b4.place(x=280, y=125)

window.mainloop()
