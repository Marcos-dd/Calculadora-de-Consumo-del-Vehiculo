from tkinter import *
from tkinter import messagebox as MessageBox
import os, sys
# -------------------Raíz------------------------------
# creación de la raíz con tkinter, se dejan fijas las dimensiones y se establece el título
root=Tk()

root.resizable(0,0)
root.title('Calculadora de consumo')

# -------------------Icono Raíz------------------------------
#Esta función permite que el icono se carge al convertir el .py en .exe
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

path = resource_path('coche2.ico')


root.iconbitmap(path)


# ---------------------Frame---------------------------
# se crea el Frame y se empaqueta en la raíz -> se establecen color y dimensiones
miFrame=Frame(root, bg='#FFECCA', bd=35, width=500, height=400)
miFrame.pack()

# -------------------Variables de entrada-----------------------------
# creación de variables vacías que se usarán más adelante para mostrar los resultados por pantalla
valorCuadroKm = IntVar()
valorCuadroConsumo = IntVar()
valorCuadroPrecioComb = IntVar()

costeComb = IntVar()
costeMto = IntVar()
costeTotal = IntVar()

# --------------------Labels----------------------------
# creación de los textos (Labels)
# se establece para cada uno de ellos título, color, fuente y su posición en la rejilla (grid), alineación del texto y separación con elementos adyacentes. 
titulo = Label(miFrame, text='Calcula el consumo de tu vehículo', bg='#FFECCA', font=('Calibri',15))
titulo.grid(row=0, columnspan=2, sticky='w')

tipoComb = Label(miFrame, text='Selecciona tipo de combustible:', bg='#FFECCA')
tipoComb.grid(row=4, column=0, sticky='e', padx=10, pady=10)

km = Label(miFrame, text='Km totales del trayecto:', bg='#FFECCA')
km.grid(row=1, column=0, sticky='e', padx=10, pady=10)

consumo = Label(miFrame, text='Consumo medio (l/100km):', bg='#FFECCA')
consumo.grid(row=2, column=0, sticky='e', padx=10, pady=10)

precioComb = Label(miFrame, text='Precio (€/l) combustible:', bg='#FFECCA')
precioComb.grid(row=3, column=0, sticky='e', padx=10, pady=10)

resultadoCosteComb = Label(miFrame, text='Gasto de combustible:', bg='#FFECCA')
resultadoCosteComb.grid(row=6, column=0, sticky='e', padx=10, pady=10)

resultadoCosteMto = Label(miFrame, text='Coste de mantenimiento:', bg='#FFECCA')
resultadoCosteMto.grid(row=7, column=0, sticky='e', padx=10, pady=10)

resultadoCosteTotal = Label(miFrame, text='Coste total del trayecto:', bg='#FFECCA', font='bold')
resultadoCosteTotal.grid(row=8, column=0, sticky='e', padx=10, pady=10)


# -------------------Funciones-----------------------------
# función que se ejecutará al pulsar el botón 'Ayuda'
def BotonAyuda():
    
    # mostrará un mensaje con el texto descrito
    MessageBox.showinfo("Ayuda",
    """
- En el cuadro 'Km totales del trayecto' deberás introducir los kilómetros totales que vas a recorrer y para los cuales quieres hacer el cálculo. NO separar los millares con puntos ni comas.

- En el cuadro 'Consumo medio(l/100km)' deberás introducir el consumo medio que tiene tu vehículo en litros por cada 100km. Este dato lo podrás encontrar en la consola de tu vehículo o en Internet.

- En el cuadro 'Precio(€/l) combustible' deberás introducir el precio por litro del combustible que utilice tu vehículo.

- A continuación tendrás que seleccionar el tipo de combustible que usa tu vehículo (Diesel o Gasolina) ya que el coste de mantenimiento varía en función del tipo de combustible.

- Pulsa 'Calcular' para ver los resultados.
- Pulsa 'Reset' para poner todos los valores a 0.

Introducir sólo valores numéricos.
Acepta valores decimales con ',' o '.'
""")


# función que se ejecutará al pulsar 'Calcular'
def Calculadora_de_consumo():

    # se establece una excepción que cubre el código ante caracteres no permitidos introducidos por el usuario (tales como letras en lugar de números)
    try:
        # obtiene los datos introducidos por el usuario y permite que pueda utilizar . o , indistintamente
        kilometros = float(cuadroKm.get().replace(',','.'))
        consumomedio = float(cuadroConsumo.get().replace(',','.'))
        precioporlitro = float(cuadroPrecioComb.get().replace(',','.'))
        
        # efecúa el cálculo de consumo a partir de los datos introducidos por el usuario
        calculoConsumo = round((kilometros * consumomedio * precioporlitro / 100),2)
        
        # se establece otra excepción para el caso en que el usuario no seleccione tipo de combustible
        try:
            # obtiene la selección del usuario en 'Tipo de combustible'
            combustible = cuadroTipoComb.get(cuadroTipoComb.curselection())
            
            # realiza el cálculo según el combustible seleccionado
            if combustible == 'Diesel':
                calculoMto = round((0.039 * kilometros),2)
            elif combustible == 'Gasolina':
                calculoMto = round((0.056 * kilometros),2)
            else:
                calculoMto = 0
            
            # almacena los valores resultantes en las variables vacías creadas al inicio
            costeComb.set(f'{calculoConsumo}€')
            costeMto.set(f'{calculoMto}€')

            calculoTotal = calculoConsumo + calculoMto

            costeTotal.set(f'{calculoTotal}€')

        except:
            # muestra mensaje de alerta al llegar a esta excepción
            MessageBox.showwarning("Alerta", 
            "Seleccione tipo de combustible.")
    except:
        # muestra mensaje de alerta al llegar a esta excepción
        MessageBox.showwarning("Error", 
            "El formato introducido no es correcto. Introduce en todos los campos sólo números (enteros o decimales).")


# función que se ejecutará al pulsar 'Reset'
def Reset():
    
    # pone todos los valores a 0
    valorCuadroKm.set('0')
    valorCuadroConsumo.set('0')
    valorCuadroPrecioComb.set('0')


# función que se ejecutará al seleccionar 'Salir'
def salirAplicación():
    
    # muestra un mensaje con respuesta de 'Sí' o 'No'
    respuesta = MessageBox.askquestion("Salir","¿Deseas salir de la aplicación?")
    
    if respuesta == 'yes':
        root.destroy()


# función que se ejecutará al seleccionar 'Acerca de...'
def AcercaDe():

    # muestra mensaje informativo
    MessageBox.showinfo("Calculadora de Consumo de tu vehículo",
    """Bienvenido a tu Calculadora de Consumo de tu vehículo.

Este programa te dará una estimación de gastos de combustible y mantenimiento para un trayecto determinado.

COSTES DE MANTENIMIENTO*:
Los costes de mantenimiento se calculan según la siguiente tabla:

     Para Diésel(estimado 30.000km/año):
        - Mantenimiento:
           - cada -> 15.000km
           - coste medio de la revisión -> 175€
           - coste imputable por km -> 0.011€ 
        - Reparación:
           - se estima un 20% sobre el coste total(21.500€ estimado) -> 4.300€
           - coste por reparación/año -> 537€
           - coste imputable por km -> 0.018€
        - Cambio de neumáticos:
           - cada -> 40.000km
           - precio medio -> 450€
           - coste imputable por km -> 0.01€
        - Factor de Cálculo Total Diésel ->  0.011€ + 0.018€ + 0.01€ = 0.039€/km   

    Para Gasolina(estimado 15.000km/año):
        - Mantenimiento:
           - cada -> 15.000km
           - coste medio de la revisión -> 175€
           - coste imputable por km -> 0.011€ 
        - Reparación:
           - se estima un 20% sobre el coste total (21.200€ estimado) -> 4.240€
           - coste por reparación/año -> 530€
           - coste imputable por km -> 0.035€
        - Cambio de neumáticos:
           - cada -> 40.000km
           - precio medio -> 450€
           - coste imputable por km -> 0.01€
        - Factor de Cálculo Total Gasolina ->  0.011€ + 0.035€ + 0.01€ = 0.056€/km
        
        
*Datos tomados de un estudio de la AEA(Automovilistas Europeos Asociados)
 """)


# función que se ejecutará al seleccionar 'Licencia'
def AvisoLicencia():
    
    #muestra un mensaje de alerta
    MessageBox.showwarning("Licencia","Producto bajo Licencia GNU")


# -------------------Barra de Menú-----------------------------
# configuración de la barra de menú
barraMenu = Menu(root)
root.config(menu=barraMenu)

# creación del submenú Archivo
menuArchivo = Menu(barraMenu, tearoff=0)
menuArchivo.add_command(label='Salir', command=salirAplicación)

# creación del submenú Ayuda y sus opciones del desplegable
menuAyuda = Menu(barraMenu, tearoff=0)
menuAyuda.add_command(label='Licencia', command=AvisoLicencia)
menuAyuda.add_command(label='Acerca de...', command=AcercaDe)

# añadimos los submenús a la barra de menú
barraMenu.add_cascade(label='Archivo', menu=menuArchivo)
barraMenu.add_cascade(label='Ayuda', menu=menuAyuda)

# -----------------Botones-------------------------------
# creación y ubicación de botones seleccionables
# también se determinan las funciones que ejecutará cada botón
botonCalculo = Button(miFrame, text='Calcular', command=Calculadora_de_consumo, cursor='hand2')
botonCalculo.grid(row=5, column=1, sticky='w', padx=10, pady=10)

botonReset = Button(miFrame, text='Reset', command=Reset, cursor='hand2')
botonReset.grid(row=5, column=1, sticky='e', padx=10, pady=10)

botonAyuda = Button(miFrame, text='?', command=BotonAyuda, cursor='hand2')
botonAyuda.grid(row=0, column=1, sticky='e', padx=10, pady=10)

# ------------------Cuadros de entrada------------------------------
# creación y ubicación de los cuadros de entrada de texto
# también se asignan los input del usuario a las variables vacías creadas al inicio para poder extraer y trabajar con esos input
cuadroKm = Entry(miFrame, textvariable=valorCuadroKm)
cuadroKm.grid(row=1,column=1)
cuadroKm.config(justify='center')

cuadroConsumo = Entry(miFrame, textvariable=valorCuadroConsumo)
cuadroConsumo.grid(row=2,column=1)
cuadroConsumo.config(justify='center')

cuadroPrecioComb = Entry(miFrame, textvariable=valorCuadroPrecioComb)
cuadroPrecioComb.grid(row=3,column=1)
cuadroPrecioComb.config(justify='center')

# este cuadro de texto es especial porque no recibe texto sino que establece las opciones que puede seleccionar el usuario
cuadroTipoComb = Listbox(miFrame, height=2, cursor='plus',
                        selectforeground="#ffffff",
                        selectbackground="#00aa00",
                        selectborderwidth=5)
cuadroTipoComb.insert(0, "Diesel")
cuadroTipoComb.insert(1,"Gasolina")
cuadroTipoComb.grid(row=4,column=1)
cuadroTipoComb.config(fg='red', justify='center')

cuadroCosteComb = Entry(miFrame, bg = 'black', textvariable=costeComb)
cuadroCosteComb.grid(row=6,column=1)
cuadroCosteComb.config(fg='white', justify='center')

cuadroCosteMto = Entry(miFrame, bg = 'black', textvariable=costeMto)
cuadroCosteMto.grid(row=7,column=1)
cuadroCosteMto.config(fg='white', justify='center')

cuadroCosteTotal = Entry(miFrame, bg = 'black', textvariable=costeTotal)
cuadroCosteTotal.grid(row=8,column=1)
cuadroCosteTotal.config(fg='yellow', justify='center', font='bold', width=13)


# ------------------------------------------------
# mantenemos el programa en ejecución
root.mainloop()
