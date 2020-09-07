# Crea una interfaz de usuario para solicitar cita previa en una peluquería
# Debe contener todas las etiquetas de texto e imagen que creas necesarias para proporcionar una buena experiencia de usuario
# Debe permitir elegir entre tres tramos horarios a través de Radiobuttons
# Debe permitir marcar los servicios o tratamientos que se desea recibir:
#		- Cortar
#		- Peinar
#		- Teñir o mechas
#		- Permanente
#		- Mascarilla
#		- Tratamiento anticaida 
# Debe contener una etiqueta o campo de texto al final en el que indicar la estimación del coste
# Debe mostrar en una etiqueta o campo de texto el resumen de la cita: tramo horario y tratamientos que se recibirán.

import tkinter as tk
from tkinter import messagebox

def date():
    cost = 0
    tratamientos = []
    if hora.get():
        if cortar.get():
            cost += 10
            tratamientos.append('cortar')
        if peinar.get():
            cost += 10
            tratamientos.append('peinar')
        if mechas.get():
            cost += 20
            tratamientos.append('teñir')
        if perm.get():
            cost += 25
            tratamientos.append('permanente')
        if masc.get():
            cost += 26
            tratamientos.append('mascarilla')
        if antic.get():
            cost += 30
            tratamientos.append('tratamiento anticaída')

        if hora.get() == 1:
            cita_label.config(text='Tiene una cita de 10 a 12.')
        elif hora.get() == 2:
            cita_label.config(text='Tiene una cita de 12 a 14.')
        elif hora.get() == 3:
            cita_label.config(text='Tiene una cita de 17 a 19.')

        tratamiento_label.config(text='Va a recibir los siguientes tratamientos:\n {}'.format('\n'.join(tratamientos)))
        coste_label.config(text='El coste será de: {}€'.format(cost))
    else:
        messagebox.showinfo('Aviso', 'No ha seleccionado una hora.')


window = tk.Tk()
window.title('Y yo con estos pelos')
window.geometry('500x600')

# scrollbar = tk.Scrollbar(window).pack(side='right', fill='y')
window.config(bg='#ff5050')

hora = tk.IntVar()
cortar = tk.IntVar()
peinar = tk.IntVar()
mechas = tk.IntVar()
perm = tk.IntVar()
masc = tk.IntVar()
antic = tk.IntVar()

f_frame = tk.Frame(window, bg='#ff5050')
f_frame.pack()
tk.Label(f_frame, text='Seleccione la hora:', bg='#ff5050', font=('Arial', 12, 'bold')).pack(side='top', fill='both', expand=True, padx=10, pady=5)
tk.Radiobutton(f_frame, text='10 a 12', variable=hora, value=1, bg='#ff5050', activebackground='#ff5050', font=('Arial', 12)).pack(side='top', fill='both', expand=True, padx=20, pady=5)
tk.Radiobutton(f_frame, text='12 a 14', variable=hora, value=2, bg='#ff5050', activebackground='#ff5050', font=('Arial', 12)).pack(side='top', fill='both', expand=True, padx=20, pady=5)
tk.Radiobutton(f_frame, text='17 a 19', variable=hora, value=3, bg='#ff5050', activebackground='#ff5050', font=('Arial', 12)).pack(side='top', fill='both', expand=True, padx=20, pady=5)

s_frame = tk.Frame(window, bg='#ff5050')
s_frame.pack()
tk.Label(s_frame, text='Seleccione los tratamientos que desea:', bg='#ff5050', font=('Arial', 12, 'bold')).pack()
tk.Checkbutton(s_frame, text='Cortar', variable=cortar, onvalue=1, offvalue=0, bg='#ff5050', activebackground='#ff5050', font=('Arial', 12)).pack(side='top', fill='both', expand=True, padx=20, pady=5)
tk.Checkbutton(s_frame, text='Peinar', variable=peinar, onvalue=1, offvalue=0, bg='#ff5050', activebackground='#ff5050', font=('Arial', 12)).pack(side='top', fill='both', expand=True, padx=20, pady=5)
tk.Checkbutton(s_frame, text='Teñir o mechas', variable=mechas, onvalue=1, offvalue=0, bg='#ff5050', activebackground='#ff5050', font=('Arial', 12)).pack(side='top', fill='both', expand=True, padx=20, pady=5)
tk.Checkbutton(s_frame, text='Permanente', variable=perm, onvalue=1, offvalue=0, bg='#ff5050', activebackground='#ff5050', font=('Arial', 12)).pack(side='top', fill='both', expand=True, padx=20, pady=5)
tk.Checkbutton(s_frame, text='Mascarilla', variable=masc, onvalue=1, offvalue=0, bg='#ff5050', activebackground='#ff5050', font=('Arial', 12)).pack(side='top', fill='both', expand=True, padx=20, pady=5)
tk.Checkbutton(s_frame, text='Tratamiento anticaída', variable=antic, onvalue=1, offvalue=0, bg='#ff5050', activebackground='#ff5050', font=('Arial', 12)).pack(side='top', fill='both', expand=True, padx=20, pady=5)

tk.Button(window, text='Solicitar', command=date, bg='#f2f2f2', font=('Arial', 12), activebackground='#ff9999', cursor='hand2').pack()

t_frame = tk.Frame(window, bg='#ff5050')
t_frame.pack()

cita_label = tk.Label(t_frame, bg='#ff5050', font=('Arial', 12))
cita_label.pack()

tratamiento_label = tk.Label(t_frame, bg='#ff5050', font=('Arial', 12))
tratamiento_label.pack()

coste_label = tk.Label(t_frame, bg='#ff5050', font=('Arial', 12))
coste_label.pack()

window.mainloop()
