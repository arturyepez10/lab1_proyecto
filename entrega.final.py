#-----------------------------------------------------------------
#LIBRERIAS
#-----------------------------------------------------------------

#Se hace un llamado a las Librerias necesarias para correr el Programa.
	#tkinter para la interfaz gráfica
from tkinter import *
from tkinter import ttk 
	#music21 para correr las especificaciones del proyecto
from music21 import *
	#Funciones de analisis descendente
from funciones import cargar_aux, reproducir_parte, reproducir_composicion, borrar_parte, transportar_parte, crear_arpegio
	#sys para poder cerrar el programa
import sys


#-----------------------------------------------------------------
#CODIGO PRINCIPAL
#-----------------------------------------------------------------

#Comandos basicos para generar la ventana principal de la Interfaz Gráfica
	#La extensión '.title()' sirve para poner el titulo a la ventana.
root = Tk()
root.title('Interpretador Musical')
	#Se crea otro Frame aparte del root (frame principal) que contendrá el menu principal
mainframe = ttk.Frame(root, padding="10 5 10 5")
mainframe.grid(column=1, row=1)


#Son los archivos donde se cargan las melodias o se generan los arpegios en las 4 Partes disponibles a manipular.
#	Cada archivo está asignado a una parte en especifico.
archivo_de_parte = []
	#En este 'for' se asigna a cada 'archivo_de_parte' la propiedad para ser una Parte
for i in range(0,4):
	archivo_de_parte.append(stream.Part())

#Función dedicada a la funcionalidad de los Sub-Menu de las Partes
	#Se le pasa un entero que es el que se encarga de asignar al 'archivo_de_parte' correspondiente.
def parte(num: int):
		#Se crea otro Frame para que contenga las opciones del menu de configuración de cada parte.
	frame = ttk.Frame(root)
	frame.grid(column=11, row=1)

		#Una etiqueta que es la encargada de decirnos cual Parte estamos configurando
	label = ttk.Label(frame, text='MENU CONFIGURACION - PARTE %s' %(num+1))
	label.grid(pady=5, padx=5)

		#El 'Entry' donde introducimos el nombre del archivo que vamos a cargar (Contenido en la carpeta del programa)
	nombrearch = StringVar()
	nombre_cargar = ttk.Entry(frame, textvariable= nombrearch)
	nombre_cargar.grid()
		#Botón para que, dado el nombre del archivo lo cargue y lo guarde como el tipo de archivo reconocido en music21
	button_cargar = ttk.Button(frame, text='Cargar Archivo', 
		command=lambda: cargar_aux(nombre_cargar.get(), num))
	button_cargar.grid(pady=5, padx=5) 

		#'Entry' donde ponemos la nota que usaremos para el Arpegio 
	entryarpegionota = StringVar() 
	entry_arpegio_nota = ttk.Entry(frame, textvariable= entryarpegionota)
	entry_arpegio_nota.grid()
		#Para introducir el número del Intervalo para el arpegio
	entryarpegiointervalo = StringVar()
	entry_arpegio_intervalo = ttk.Entry(frame, textvariable= entryarpegiointervalo)	
	entry_arpegio_intervalo.grid()
		#Para introducir intervalo Ascendente/Descendente a Transponer el Arpegio
	entrytransportearpegio = StringVar()
	entry_transporte_arpegio = ttk.Entry(frame, textvariable=entrytransportearpegio)
	entry_transporte_arpegio.grid()
		#Botón donde dado una nota, un intervalo númerico y un intervalo ascendente/descendente genera un arpegio y lo guarda
	button_arpegio = ttk.Button(frame, text='Generar Arpegio',
		command=lambda: crear_arpegio(entry_arpegio_nota.get(),num,
			int(entry_arpegio_intervalo.get()),entrytransportearpegio.get()))
	button_arpegio.grid(pady=5, padx=5)

		#'Entry' para introducir el intervalo ascendete/descendente 
	nombreinter = StringVar()
	nombre_inter = ttk.Entry(frame, textvariable= nombreinter)
	nombre_inter.grid()
		#Boton que ejecuta el comando para Transportar una parte cargada luego de insertar un intervalo ascendente/descendente
	button_transportar = ttk.Button(frame, text='Transportar',
		command=lambda: transportar_parte(num, nombre_inter.get()))
	button_transportar.grid(pady=5, padx=5)

		#Luego de cargar una Parte o generar un Arpegio, este botón ejecuta la sub-función para reproducir la Parte Seleccionada
	button_escuchar = ttk.Button(frame, text='Escuchar Parte',
		command=lambda: reproducir_parte(archivo_de_parte[num]))
	button_escuchar.grid(pady=5, padx=5)

	button_borrar = ttk.Button(frame, text='Borrar Parte', 
		command=lambda: borrar_parte(num))
	button_borrar.grid(pady=5, padx=5)

		#Cierra la extensión del menu de configuración correspondiente
	button_anterior = ttk.Button(frame, text='Cerrar Extensión', command=frame.grid_forget)
	button_anterior.grid(pady=5, padx=5)

#Dada la función del los submenus aquí se almacenan los llamados para cada Parte de la composición de forma individual
	#Es un arreglo que maneja 4 sub-menus con la función lambda para que se ejecute cuando son llamados
parte_submenu = [lambda: parte(0), lambda: parte(1), lambda: parte(2), lambda: parte(3)]

#Los botones de la interfaz Gráficas con cada 'command=' con la acción que realizará al presionar el boton
	#Este Botón abre el sub-menu de la Parte 1 de la Composición
parte1 = ttk.Button(mainframe, text='Parte 1', command= parte_submenu[0])
parte1.grid(pady=5, padx=5, ipady=5, ipadx=5, column=3)
	#Este Botón abre el sub-menu de la Parte 2 de la Composición
parte2 = ttk.Button(mainframe, text='Parte 2', command= parte_submenu[1])
parte2.grid(pady=5, padx=5, ipady=5, ipadx=5, column=3)
	#Este Botón abre el sub-menu de la Parte 3 de la Composición
parte3 = ttk.Button(mainframe, text='Parte 3', command= parte_submenu[2])
parte3.grid(pady=5, padx=5, ipady=5, ipadx=5, column=3)
	#Este Botón abre el sub-menu de la Parte 4 de la Composición
parte4 = ttk.Button(mainframe, text='Parte 4', command= parte_submenu[3])
parte4.grid(pady=5, padx=5, ipady=5, ipadx=5, column=3)
	#Al ejecutarse este botón se pasa el comando para llamar a la función que reproduce toda la Composición
composicion = ttk.Button(mainframe, text='Escuchar Composicion', command=reproducir_composicion)
composicion.grid(pady=5, padx=5, ipady=5, ipadx=5, column=3)
	#Presionado, este botón llama la función importada de la libreria 'sys' y permite cerrar el programa.
salir = ttk.Button(mainframe, text='Salir del Programa', command=sys.exit)
salir.grid(pady=5, padx=5, ipady=5, ipadx=5, column=3)

#Comando asignado del tkinter para mantener el loop principal de la ventana y el programa.
root.mainloop()