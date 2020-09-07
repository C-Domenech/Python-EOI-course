# Crea una ventana interfaz de usuario que sirva para generar una lista con productos para ir a la compra
# Para ello, utiliza tkinter, creando la raiz, etiquetas y campo de texto
# Almacena los nombres de cinco productos como elementos de una lista, a medida que se introduzcan.
# Finalmente, muestra los elementos de la lista

import tkinter as tk


def print_function():
    e_list = [element1, element2, element3, element4, element5]
    print('Comprar:')
    for element in e_list:
        if element.get():
            print('-', element.get())
            element.delete(0, tk.END)


my_window = tk.Tk()
my_window.geometry('300x400')
my_window.title('My Shopping List')
my_window.iconbitmap('apple.ico')
my_window.config(bg='#ccff66')

my_text = tk.Label(text='Shopping List:', bg='#ccff66')
my_text.config(font=('Arial', 20))
my_text.pack(fill=tk.X)

element1 = tk.Entry(font=('Arial', 18))
element1.pack(pady=10)

element2 = tk.Entry(font=('Arial', 18))
element2.pack(pady=10)

element3 = tk.Entry(font=('Arial', 18))
element3.pack(pady=10)

element4 = tk.Entry(font=('Arial', 18))
element4.pack(pady=10)

element5 = tk.Entry(font=('Arial', 18))
element5.pack(pady=10)

button = tk.Button(my_window, text='Print', bg='#426600', fg='white', command=print_function)
button.config(font=('Arial', 15), activebackground='#639900', cursor='hand2')
button.pack(side=tk.BOTTOM, pady=20, ipadx=8)

my_window.mainloop()
