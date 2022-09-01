from tkinter import *
from tkinter import font
from estado import Estado
from afd import AFD
from derivar import *

dfa = AFD()

# Esta función crea una nueva ventana con el titulo y el mensaje ingresado
def popup(titulo, mensaje):
    top= Toplevel(ventana)
    top.geometry("650x250")
    top.title(titulo)
    top.config(bg='#001219')
    mensaje_error = Label(top, text = '', justify=LEFT)
    mensaje_error.config(font='Monospace', fg='white', bg='#001219', text=mensaje)
    mensaje_error.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

# Esta función se encarga de crear el AFD y mostrarlo en pantalla
def generar_afd():
    user_regex = regex_input.get()
    verificacion_errores = verificar_errores(user_regex)
    if not verificacion_errores[0]:
        estado_inicial = Estado(user_regex)
        dfa.crear_afd(estado_inicial)
        dfa_label.config(text = dfa.mostrar_estados())
    else: 
        popup('Resultado', verificacion_errores[1])

# Esta función se encarga de validar la cadena de texto sobre el AFD ingresado y mostrar el resultado en pantalla
def validar_string():
    user_regex = regex_input.get()
    verificacion_errores = verificar_errores(user_regex)
    if not verificacion_errores[0]:
        estado_inicial = Estado(user_regex)
        dfa.crear_afd(estado_inicial)
        validate_string_result = dfa.verificar_expresion(validar_input.get())
        if validate_string_result == 0:
            popup('Validacion de String', 'Falso')
        else:
            popup('Validacion de String', 'Verdadero')
    else:
        popup('Resultado', verificacion_errores[1])

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
button = Button(text='Generar AFD', width=25, command=generar_afd)
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
dfa_label = Label(ventana, text = '', justify=LEFT)
dfa_label.config(font='Monospace', fg='white', bg='#001219')
dfa_label.grid(row=4, column=0, padx=20, pady=20, columnspan=2)

ventana.mainloop()
