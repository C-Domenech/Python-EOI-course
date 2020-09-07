# Escribe el código necesario para crear una ventana utilizando tkinter
# Debe mostrar un texto de presentación o una advertencia

import tkinter as tk

my_window = tk.Tk()
my_window.geometry('400x400')
my_window.title('My awesome window')

my_text = tk.Label(text='Welcome to my empty window!', bg='#ff99cc')
my_text.config(font=('Arial', 22))
my_text.pack(fill=tk.X)

my_window.mainloop()
