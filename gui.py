from tkinter import *
from tkinter import font
from state import State
from dfa import DFA
from derive import *

dfa = DFA()

def popup(title, message):
    top= Toplevel(ventana)
    top.geometry("500x250")
    top.title(title)
    top.config(bg='#001219')
    error_message = Label(top, text = '', justify=LEFT)
    error_message.config(font='Monospace', fg='white', bg='#001219', text=message)
    error_message.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

def generate_afd():
    user_regex = regex_input.get()
    verify_regex_error = verify_regex(user_regex)
    if not verify_regex_error[0]:
        initial_state = State(user_regex)
        dfa.create_dfa(initial_state)
        dfa_label.config(text = dfa.show_states())
    else: 
        popup('Result', verify_regex_error[1])

def validate_string():
    user_regex = regex_input.get()
    verify_regex_error = verify_regex(user_regex)
    if not verify_regex_error[0]:
        validate_string_result = dfa.verify_string(validar_input.get())
        if validate_string_result == 0:
            resultado_validacion.config(text = 'Falso')
        else:
            resultado_validacion.config(text = 'Verdadero')
    else:
        popup('Result', verify_regex_error[1])

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
button = Button(text='Validar String', width=25, command=validate_string)
button.config(bg='springgreen', borderwidth=0, font='Monospace', highlightbackground='#001219', activebackground='black', activeforeground='white')
button.grid(row=3, column=1, padx=20, pady=20)

# Label donde se mostrará el resultado
dfa_label = Label(ventana, text = '', justify=LEFT)
dfa_label.config(font='Monospace', fg='white', bg='#001219')
dfa_label.grid(row=4, column=0, padx=20, pady=20, columnspan=2)

# Label donde se mostrará el resultado de la validacion del string
resultado_validacion = Label(ventana, text = '', justify=LEFT)
resultado_validacion.config(font='Monospace', fg='white', bg='#001219')
resultado_validacion.grid(row=4, column=0, padx=20, pady=20, columnspan=2)

ventana.mainloop()
