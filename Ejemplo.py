from HuGui import HuGui # Importamos la clase HuGui(la librería)
import tkinter as tk # La librería de interfaz gráfica para algunos elementos adicionales(SOLO ADICIONALES, REPITO, SOLO ADICIONALES)

hg = HuGui() # Creamos una instancia de la clase HuGui

def sumar(a, e):
    return a + e

def restar(a, e):
    return a - e

def multiplicar(a, e):
    return a * e

def dividir(a, e):
    return a / e

def presionado(): # Creamos la función presionado del botón
    hg.mostrar_mensaje_gui_info("BIENVENIDO", "BIENVENIDO A MI LIBRERÍA DE INTERFAZ GRÁFICA") # NO NECESITAS NINGÚN COMENTARIO PARA ESTO EEEEEH

def calculadora(): # Creamos la función calculadora del botón

    def enviar_igual(): # Creamos la función de igual para calcular el resultado
        if textfield_operador.get('1.0', 'end-1c') == '+': # Con el get conseguimos el texto
            hg.mostrar_mensaje_gui_info('Resultado de la suma', 'El resultado de la suma es: '+ str(sumar(float(textfield_num1.get('1.0', 'end-1c')), float(textfield_num2.get('1.0', 'end-1c'))))) # BÁSICAMENTE SE SUMA, NO ME PREGUNTES

        elif textfield_operador.get('1.0', 'end-1c') == "-":
            hg.mostrar_mensaje_gui_info('Resultado de la resta', 'El resultado de la resta es: '+ str(restar(float(textfield_num1.get('1.0', 'end-1c')), float(textfield_num2.get('1.0', 'end-1c'))))) # BÁSICAMENTE SE RESTA, NO ME PREGUNTES

        elif textfield_operador.get('1.0', 'end-1c') == '*':
            hg.mostrar_mensaje_gui_info('Resultado de la resta', 'El resultado de la resta es: '+ str(multiplicar(float(textfield_num1.get('1.0', 'end-1c')), float(textfield_num2.get('1.0', 'end-1c'))))) # BÁSICAMENTE SE MULTIPLICA, NO ME PREGUNTES

        elif textfield_operador.get('1.0', 'end-1c') == '/':
            hg.mostrar_mensaje_gui_info('Resultado de la división', 'El resultado de la división es: '+ str(dividir(float(textfield_num1.get('1.0', 'end-1c')), float(textfield_num2.get('1.0', 'end-1c'))))) # BÁSICAMENTE SE DIVIDE, NO ME PREGUNTES

        else:
            hg.mostrar_mensaje_gui_error('ERROR', 'Operador erróneo')


    hg.crear_ventana_main('white', '660x550', 'Calculadora')
    tk.Label(hg.root, text='Introduce un número:', wraplength=500).grid(row=0, column=0, padx=10, pady=10) # La única diferencia es que creas un label(NO ME PREGUNTES, REPITO, NO ME PREGUNTES)
    textfield_num1 = tk.Text(hg.root, height='2', width='25') # Otra vez, la única diferencia es que creas un campo de texto(NO ME PREGUNTES, REPITO, NO MRE PREGUNTES)
    textfield_num1.grid(row=0, column=1, padx=10, pady=10) # No necesitas que comente esto
    tk.Label(hg.root, text='Introduce un operador:', wraplength=500).grid(row=1, column=0, padx=10, pady=10) # Uffff, no necesitas que comente ESTO AAAAAAAAAAAAAAAAA
    textfield_operador = tk.Text(hg.root, height='2', width='25') # OTRA VEZ, QUE NO VOY A COMENTAR ESTOOOOOOO
    textfield_operador.grid(row=1, column=1, padx=10, pady=10) # No necesitas que comente esto
    tk.Label(hg.root, text='Introduce el último número:', wraplength=500).grid(row=2, column=0, padx=10, pady=10) # TAMPOCO NECESITAS QUE COMENTE ESTO
    textfield_num2 = tk.Text(hg.root, height='2', width='25') # TAMPOCO NECESITAS QUE COMENTE ESTOOOOOOOOOO
    textfield_num2.grid(row=2, column=1, padx=10, pady=10) # No necesitas que comente esto
    tk.Button(hg.root, text='=', height='2', width='25', command=enviar_igual).grid(row=3, column=0, padx=10, pady=10) # No necesitas que comente esto


hg.mostrar_mensaje_gui_info('Mensaje', 'Hola') # Crear mensaje de interfaz gráfica con el símbolo de información
hg.crear_ventana_main('white', '660x550', 'Ventana Gui') # Crear la ventana principal(color de fondo blanco, 660 de ancho y 550 de alto, y Ventana Gui de nombre de la ventana)
tk.Button(hg.root, text='Botón bonito y humilde', height='2', width='40', command=presionado).grid(row=0, column=0, padx=10, pady=10) # Creamos un botón en el root de HuGui, el texto del botón es Botón bonito y humilde, 2 de altura y de ancho 40, y al hacer click, se va a ejecutar una función llamada presionado(ADICIONAL, REPITO, ADICIONAL), y hacemos que esté en la altura de 0, columna 0, ancho x 10, ancho y 10(ESTOY CANSADO JEFE SDHJFAAKFGDSUHG)
tk.Button(hg.root, text='Calculadora', height='2', width='25', command=calculadora).grid(row=1, column=0, padx=10, pady=10) # No necesitas ningún comentario MÁS AAAAAAAAJASDOKFHSA
hg.root.mainloop() # Hacemos que la ventana NUNCA SE CIERRE, SALVO QUE EL USUARIO LE DE CLICK A CERRAR(OBVIAMENTE, REPITO, OBVIAMENTE asuydfgasdjfgasdfjk)

# POR FIN HE TERMINADO MI EJEMPLO, SI NO LO ENTENDISTE ME VOY A PEGAR UN TI
# Bueno, ADIÓS :)