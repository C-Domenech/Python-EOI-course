import tkinter as tk
from tkinter import filedialog

path = ''
words = 0


# lógica
def new():
    global path
    message.set('New document - Welcome to your text editor')
    path = ''
    text.delete(1.0, 'end')


def open_file():
    global path
    global words
    message.set('Opening file')
    path = filedialog.askopenfilename(initialdir='.', filetype=(('Text files', '*.txt'),), title='Open')
    if path != '':
        file = open(path, 'r')
        content = file.read()
        all_words = content.split()
        words = len(all_words)
        counter.set('{} words'.format(words))
        text.delete(1.0, 'end')
        text.insert('insert', content)
        file.close()
        window.title(path + ' - My Text Editor')
    message.set('Welcome to your text editor')


def save():
    message.set('Saving file')
    if path != '':
        content = text.get(1.0, 'end-1c')
        file = open(path, 'w+')
        file.write(content)
        file.close()
        message.set('File successfully saved - Welcome to your text editor')
    else:
        save_as()


def save_as():
    global path
    message.set('Save as... - Welcome to your text editor')
    file = filedialog.asksaveasfile(title='Save as', mode='w', defaultextension='.txt',
                                    filetype=(('Text files', '*.txt'),))
    if file is not None:
        path = file.name
        content = text.get(1.0, 'end-1c')
        file = open(path, 'w+')
        file.write(content)
        file.close()
        message.set('File successfully saved - Welcome to your text editor')
        window.title(path + ' - My Text Editor')
    else:
        message.set('Error saving file!')
        path = ''


def short_new(event):
    new()


def short_open(event):
    open_file()


def short_save(event):
    save()


def short_save_as(event):
    save_as()


def short_exit(event):
    window.quit()


def words_counter(event):
    global words
    # words += 1
    # counter.set('{} words'.format(words))
    all_text = text.get(1.0, 'end-1c')
    all_words = all_text.split()
    words = len(all_words)
    counter.set('{} words'.format(words))


window = tk.Tk()
window.title('My Text Editor')
window.iconbitmap('quill-ink.ico')

# Menú
menubar = tk.Menu(window)
window.config(menu=menubar)

# Etiqueta 1 del menú
filemenu = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='New', command=new, accelerator='Ctrl+N'.rjust(30))
filemenu.add_separator()
filemenu.add_command(label='Open...', command=open_file, accelerator='Ctrl+O'.rjust(30))
filemenu.add_separator()
filemenu.add_command(label='Save', command=save, accelerator='Ctrl+S'.rjust(30))
filemenu.add_command(label='Save as...', command=save_as, accelerator='Ctrl+Shift+S'.rjust(25))
filemenu.add_separator()
filemenu.add_command(label='Exit', command=quit, accelerator='Ctrl+W'.rjust(28))

window.bind('<Control-n>', short_new)
window.bind('<Control-o>', short_open)
window.bind('<Control-s>', short_save)
window.bind('<Control-Shift-KeyPress-S>', short_save_as)
window.bind('<Control-w>', short_exit)

window.bind('<Key>', words_counter)

# Etiqueta 2 del menú
# editmenu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Edit', menu=editmenu)
#
# # Etiqueta 3 del menú
# helpmenu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Help', menu=helpmenu)

text = tk.Text(window)
text.pack(fill='both', expand=1)
text.grid(column=1, columnspan=2)
text.config(padx=6, pady=4, bd=0, font=('Courier New', 12))

message = tk.StringVar()
message.set('New document - Welcome to your text editor')

display_main = tk.Label(window, textvar=message)
# display_main.pack()
display_main.grid(row=1, column=1)

counter = tk.StringVar()
counter.set('0 words')

display_counter = tk.Label(window, textvar=counter)
# display_counter.pack()
display_counter.grid(row=1, column=2)

window.mainloop()
