# Sois el equipo encargado de crear la interfaz de usuario que tendrá el módulo tripulable
#  de la primera expedición humana a Marte
# La interfaz debe tener 8 botones distribuidos en dos columnas de 4
# Los botones (podéis ponerlos en el orden que queráis) deben servir para:

#	- Botón 1: Despegue de emergencia. Al presionarlo debe aparecer un mensaje advirtiendo de que
#		se debe activar el sistema de navegación automático para alcanzar una orbita estable

#	- Botón 2: Apagado de motor principal. Al presionarlo debe aparecer un mensaje preguntando
#		si, de verdad, se quiere apagar el motor (SI/NO)

#	- Botón 3: Activación de sistema de expulsión de residuos. Al presionarlo debe aparecer un mensaje
#		confirmando que los residuos han sido expulsados

#	- Botón 4: Apertura de patas de soporte del módulo. Al presionarlo, debe aparecer un mensaje de confirmación
#		de que las patas de aterrizaje están desplegadas

#	- Botón 5: Test de atmósfera viable. Al presionarlo, debe aparecer un mensaje que pregunta si la atmósfera es compatible
#		con la vida humana, y el usuario debe responder Si o No
#	- Botón 6: Apagado del sistema de soporte vital. Al presionarlo, aparecerá un mensaje de confirmación 
#		en caso de que el motor ppal esté apagado, las patas de aterrizaje extendidas y el test de atmósfera sea positivo
#		En caso contrario, debe mostrar un mensaje de error informando de que no es posible el apagado del sistema

#	- Botón 7: Encendido de motor principal. Al presionarlo, debe aparecer un mensaje que pregunte si se desea seguir adelante
#		con OK/CANCEL como posibles respuestas
#	- Botón 8: Autodestrucción de la nave en 1 minuto. Al presionarlo, debe aparecer un mensaje desaconsejando optar por
#		la autodestrucción, dando las opciones de "reintentar" o "cancelar". Si se pulsa reintentar, se cierra la aplicación.

import tkinter as tk
from tkinter import messagebox

main_engine = False
landing_gear = False
atmosphere = False


def emergency_launch():
    messagebox.showwarning("Navigation Error!",
                           "Warning: Automatic Navigation System must be enabled to reach a stable Orbit ")


def main_shutdown():
    global main_engine
    if main_engine:
        answer_1 = messagebox.askyesno("Confirmation", "Are you shure you want to shut down the main engine")
        if answer_1:
            main_engine = False
            messagebox.showinfo("Engine Status", "Shuting Down main Engine")
    else:
        messagebox.showinfo("Engine Status", "Engine is already stopped!")


def poop():
    messagebox.showinfo("Waste Management", " Waste ejection completed! ")


def land_1():
    global landing_gear
    if not landing_gear:
        landing_gear = True
        messagebox.showinfo("Landing Gear Status", "Landing Gear locked")
    else:
        messagebox.showinfo("Landing Gear Status", "Landing Gear is already locked!")


def atmosphere_test():
    global atmosphere
    answer = messagebox.askquestion('Viable atmosphere test', 'Is the atmosphere suitable for human life?')
    if answer:
        atmosphere = True
    else:
        atmosphere = False


def life_support():
    if not main_engine and landing_gear and atmosphere:
        messagebox.showinfo('Life Support', 'Life Support shut down successfully.')
    else:
        messagebox.showerror('ERROR - Life Support',
                             'Life Support can not be shut down.\nRemember: It is only possible if the landing gear is locked, the main engine is not running and the atmosphere is suitable.')


def start_engine():
    global main_engine
    if not main_engine:
        answer = messagebox.askokcancel(title='Start Engine',
                                        message='Are you sure you want to start the engine?')
        if answer:
            messagebox.showinfo('Engine Status', 'Starting engine...')
            main_engine = True
        elif not answer:
            messagebox.showinfo('Engine Status', 'Cancelling order...')
    else:
        messagebox.showinfo("Engine Status", "Main Engine is already running!")


def self_destruction():
    answer = messagebox.askretrycancel('Self-destruction',
                                       'The spaceship is going to self-destruct in a minute. It is a really dangerous '
                                       'option.')
    if answer:
        window.quit()


window = tk.Tk()
window.title('Trip to Mars')
window.geometry('380x300')
window.config(bg='lightgrey')

button_7 = tk.Button(window, text='START Engine', command=start_engine, font=('Arial', 12, 'bold'), anchor='center', bg='#006600', fg='white', activebackground='#4dff4d', cursor='hand2').grid(row=0, column=0, pady=(20, 20), padx=20)
button_2 = tk.Button(window, text="STOP Engine", command=main_shutdown, font=('Arial', 12, 'bold'), anchor='center', bg='#ff0000', fg='white', activebackground='#ff6666', cursor='hand2').grid(row=0, column=1, pady=(20, 20), padx=20)

button_4 = tk.Button(window, text="Landing Gear Down", command=land_1, font=('Arial', 12), bg='#334d4d', fg='white', activebackground='#669999', cursor='hand2').grid(row=1, column=0, pady=20, padx=20)
button_5 = tk.Button(window, text='Atmosphere Test', command=atmosphere_test, font=('Arial', 12), bg='#334d4d', fg='white', activebackground='#669999', cursor='hand2').grid(row=1, column=1, pady=20, padx=20)

button_6 = tk.Button(window, text='Life Support', command=life_support, font=('Arial', 12), bg='#334d4d', fg='white', activebackground='#669999', cursor='hand2').grid(row=2, column=0, pady=20, padx=20)
button_3 = tk.Button(window, text="Waste Ejection", command=poop, font=('Arial', 12), bg='#334d4d', fg='white', activebackground='#669999', cursor='hand2').grid(row=2, column=1, pady=20, padx=20)

button_1 = tk.Button(window, text="Emergency Launch", command=emergency_launch, font=('Arial', 12), bg='#ff0000', fg='white', activebackground='#ff6666', cursor='hand2').grid(row=3, column=0, pady=20, padx=20)
button_8 = tk.Button(window, text='Self-destruction', command=self_destruction, font=('Arial', 12), bg='#ff0000', fg='white', activebackground='#ff6666', cursor='hand2').grid(row=3, column=1, pady=20, padx=20)


window.mainloop()
