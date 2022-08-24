from tkinter import *
from tkinter import font
from state import State
from dfa import DFA

def generate_afd():
    # Obtenemos el valor del input
    value = regex_input.get()
    # Creamos estado con la expresion regular ingresada
    initial_state = State(value)
    # Creamos afd a partir de la expresion regular
    dfa = DFA()
    dfa.create_dfa(initial_state)
    
    resultado.config(text = dfa.show_states())

def validate_string():
    pass

# Ventana principal
ventana = Tk()
ventana.title('Practica')
ventana.geometry('550x700')
ventana.config(bg='#001219')

# Label del titulo
titulo = Label(ventana, text='AFD en base a Expresión Regular')
titulo.config(font=('Monospace', 18, font.BOLD), fg='white', bg='#001219')
titulo.grid(row=0, column=0, padx=20, pady=40, columnspan=2)

# Label de el input
mensaje = Label(ventana, text='Ingrese la expresión regular')
mensaje.config(font='Monospace', fg='white', bg='#001219')
mensaje.grid(row=1, column=0, padx=20, pady=20, columnspan=2)

# Input
regex_input = Entry(ventana)
regex_input.config(font='Monospace', bg='#001219', fg='white')
regex_input.grid(row=2, column=0, padx=20, pady=20)

# Boton
button = Button(text='Generar AFD', width=25, command=generate_afd)
button.config(bg='springgreen', borderwidth=0, font='Monospace', highlightbackground='#001219', activebackground='black', activeforeground='white')
button.grid(row=2, column=1, padx=20, pady=20)

# Input para validar string
validar_input = Entry(ventana)
validar_input.config(font='Monospace', bg='#001219', fg='white')
validar_input.grid(row=3, column=0, padx=20, pady=20)

# Boton para validar string
button = Button(text='Validar String', width=25, command=validar_string)
button.config(bg='springgreen', borderwidth=0, font='Monospace', highlightbackground='#001219', activebackground='black', activeforeground='white')
button.grid(row=3, column=1, padx=20, pady=20)

# Label donde se mostrará el resultado
resultado = Label(ventana, text = '', justify=LEFT)
resultado.config(font='Monospace', fg='white', bg='#001219')
resultado.grid(row=4, column=0, padx=20, pady=20, columnspan=2)

ventana.mainloop()
