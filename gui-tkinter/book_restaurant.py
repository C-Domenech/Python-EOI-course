# Tenéis que crear la interfaz de reservas de un restaurante
# El restaurante tiene un aforo permitido de 20 personas
# Hay dos turnos de comidas: 12 a 14 y 14 a 16
# El usuario debe introducir número de comensales y hora
# La interfaz debe informar de si la reserva es posible o no
# En caso de que en la franja horaria en la que se encuentra la hora
# introducida por el usuario haya suficientes plazas, la interfaz
# debe mostrar un mensaje de confirmación y actualizar las plazas disponibles

# num comensales
# 2 turnos

import tkinter as tk
from tkinter import messagebox

comensales_t1 = 0
comensales_t2 = 0


def aforo_por_turno():
    global comensales_t1, comensales_t2
    aforo_max = 20
    if turno.get() == 1:
        if (comensales_t1 + n_comensales.get()) <= aforo_max:
            comensales_t1 += n_comensales.get()
            messagebox.showinfo(title='Reserva', message='Reserva realizada satisfactoriamente')
        else:
            messagebox.showwarning(title='Reserva', message='Se ha superado el aforo de este turno')

    elif turno.get() == 2:
        if (comensales_t2 + n_comensales.get()) <= aforo_max:
            comensales_t2 += n_comensales.get()
            messagebox.showinfo(title='Reserva', message='Reserva realizada satisfactoriamente')
        else:
            messagebox.showwarning(title='Reserva', message='Se ha superado el aforo de este turno')


window = tk.Tk()
window.geometry('350x400')
window.iconbitmap('knife-fork.ico')
window.config(bg='#9999ff')
window.title('Reservas')

n_comensales = tk.IntVar()
turno = tk.IntVar()

com_label = tk.Label(window, text='Introduzca el número de comensales:', bg='#9999ff', font=('Arial', 12, 'bold'))
com_label.pack(side='top', fill='both', expand=True, padx=10, pady=5)

comensales_spin = tk.Spinbox(window, from_=1, to=20, wrap=True, textvariable=n_comensales, state='readonly', font=('Arial', 12))
comensales_spin.pack(side='top', fill='x', expand=True, padx=20, pady=5)

turno_label = tk.Label(window, text='Seleccione un turno:', bg='#9999ff', font=('Arial', 12, 'bold'))
turno_label.pack(side='top', fill='both', expand=True, padx=10, pady=5)

p_turno = tk.Radiobutton(window, text="12 a 14 horas", variable=turno, value=1, bg='#9999ff', activebackground='#9999ff', font=('Arial', 12))
p_turno.pack(side='top', fill='both', expand=True, padx=20, pady=5)
s_turno = tk.Radiobutton(window, text="14 a 16 horas", variable=turno, value=2, bg='#9999ff', activebackground='#9999ff', font=('Arial', 12))
s_turno.pack(side='top', fill='both', expand=True, padx=20, pady=5)

reservar = tk.Button(window, text="Reservar", command=aforo_por_turno, bg='#4d4dff', fg='white', font=('Arial', 12), activebackground='#8080ff', cursor='hand2')
reservar.pack(side='left', fill='both', expand=True, padx=10, pady=15)
salir = tk.Button(window, text="Salir", command=quit, bg='#4d4dff', fg='white', font=('Arial', 12), activebackground='#8080ff', cursor='hand2')
salir.pack(side='right', fill='both', expand=True, padx=10, pady=15)

window.mainloop()
