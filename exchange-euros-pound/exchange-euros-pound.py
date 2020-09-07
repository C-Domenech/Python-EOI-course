# Crea una interfaz que calcule el cambio de moneda entre euros y libras inglesas
# Debe tener etiquetas de título e informativas, con estilos
# Debe tener campos de texto donde introducir y mostrar las cantidades
# Debe tener un botón para calcular el cambio, con estilo configurado

import tkinter as tk


def exchange(op):
    if op == 1 and len(amount.get()) > 0:
        result.set(round(float(amount.get()) * 0.899249, 2))  # 0,899249
    elif op == 2 and len(amount.get()) > 0:
        result.set(round(float(amount.get()) * 1.11204, 2))  # 1,11204


window = tk.Tk()
window.title('Conversor')

window.iconbitmap('exchange.ico')

window.geometry('400x400')
window.config(bg='#ffcc99')
amount = tk.StringVar()
result = tk.StringVar()
tk.Label(window, font=('Arial', 18), text='Introduce una cantidad:', bg='#ffcc99', pady=10).pack(pady=(5, 0))
tk.Entry(window, justify='center', bg='#fff2e6', font=('Arial', 18), textvariable=amount).pack()
tk.Label(window, font=('Arial', 18), text='Resultado:', bg='#ffcc99', pady=10).pack(pady=(5, 0))
tk.Entry(window, justify='center', bg='#fff2e6', font=('Arial', 18), textvariable=result).pack()
tk.Button(window, text='Euros a libras', font=('Arial', 18), cursor='hand2', bg='#ff9633', fg='white',
          activebackground='#ffb066', command=lambda: exchange(1)).pack(side='left', padx=10)
tk.Button(window, text='Libras a euros', font=('Arial', 18), cursor='hand2', bg='#ff9633', fg='white',
          activebackground='#ffb066', command=lambda: exchange(2)).pack(side='right', padx=10)
window.mainloop()
