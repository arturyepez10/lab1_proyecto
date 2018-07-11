# lab1_proyecto
Proyecto de Laboratorio de Algoritmos y Estructuras 1

ENTREGA FINAL - PROYECTO DE LABORATORIO DE ALGORITMOS 1
Autores: Arturo Yepez 15-11551
		 Carlos Carrasquel 13-10233

Ultima Modificación: 11/07/2018.

DESCRIPCION: Este es un programa cuyo proposito sirve para la creación de una pieza musical mediante varias funciones 
			 del analizador, donde una Composición puede estar hecha de 4 partes y para cada parte se tiene que se puede
			 cargar un archivo con la extensión .tinynotation o crear un arpegio y transportar una parte cargada o arpegio. 

			 Luego de estas configuraciones se puede escuchar todas estas partes juntas o cada parte por separada. 

FUNCIONES DISPONIBLES:
	Todas las funciones planteadas inicialmente están disponibles, se puede manipular cada parte por separado con las funciones de:
	- Cargar un Archivo.
	- Crear un Arpegio.
	- Transportar.
	- Escuchar una Parte.
	- Borrar una Parte.
	- Cerrar la Extensión de la Parte abierta.

	Por afuera, se puede escuchar todas las partes juntas al unísono.

A lo largo del codigo se pueden ver varias extensiones de la libreria de tkinter u de otras librerias comunes como:
	- '.grid()' - Extensión usada comunmente para poner los widgets de tkinter en el frame.
	- La función 'lambda' es una clase de pseudo-función que utilizamos en el codigo para a la hora de hacer ciertos llamados los 
		haga solo cuando se le pide al codigo que ejecute un comando, de por ejemplo, un botón para que se ejecute la función solo
		cuando presionemos el botón y no para que se ejecute cuando la línea de comando lea el codigo.
