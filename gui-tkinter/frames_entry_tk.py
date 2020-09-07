# Crea una interfaz de usuario con dos marcos
# En uno de los marcos, utiliza los widgets Label y Entry para que el usuario introduzca nombre y apellidos
# En el otro marco, utiliza también Label y Entry para introducir nombre de usuario y contraseña
# El campo de contraseña no debe permitir que se vean los caracteres reales
# En la parte inferior de la ventana, crea un botón con el texto "Registrarse"
# Da color, dimensiones y tipo de borde a los marcos, etiquetas, campos de texto y botón
import tkinter as tk

window = tk.Tk()
window.geometry('400x200')
window.config(bg='#99ccff')
window.title('REGISTRO')

frame1 = tk.Frame(window)
frame1.config(bg='#99ccff', relief='groove', bd=5)
frame1.pack()

name = tk.Label(frame1, text='Nombre:', bg='#99ccff', font=('Arial', 12), width=10)
name.grid(row=0, column=0, sticky='e')
entry_name = tk.Entry(frame1, font=('Arial', 12))
entry_name.grid(row=0, column=1)

last_name = tk.Label(frame1, text='Apellidos:', bg='#99ccff', font=('Arial', 12), width=10)
last_name.grid(row=1, column=0, sticky='e')
entry_last = tk.Entry(frame1, font=('Arial', 12))
entry_last.grid(row=1, column=1)

frame2 = tk.Frame(window)
frame2.config(bg='#99ccff', relief='groove', bd=5)
frame2.pack()

user = tk.Label(frame2, text='Usuario:', bg='#99ccff', font=('Arial', 12), width=10)
user.grid(row=0, column=0, sticky='e')
entry_user = tk.Entry(frame2, font=('Arial', 12))
entry_user.grid(row=0, column=1)

password = tk.Label(frame2, text='Contraseña:', bg='#99ccff', font=('Arial', 12), width=10)
password.grid(row=1, column=0, sticky='e')
entry_pass = tk.Entry(frame2, font=('Arial', 12), show='*')
entry_pass.grid(row=1, column=1)

button = tk.Button(window, text='Registrarse', bg='#0073e6', fg='white')
button.config(font=('Arial', 10), activebackground='#99ccff', cursor='hand2')
button.pack(side=tk.BOTTOM, pady=20, ipadx=8)

window.mainloop()
