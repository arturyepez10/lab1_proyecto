#SUB-FUNCIONES CREADAS PARA REALIZAR LOS TRABAJOS PRINCIPALES DEL PROGRAMA (Análisis Descendente)

#Funciones que se utiizan para Cargar un Archivo, donde la primera es la encargada de cargar el archivo y
#	ponerlo del tipo manejable de music21 y la segunda se encarga de almacenarlo en la variable asignada para esa parte.
def cargar_archivo(nombre_cargar):
	s = converter.parseFile('%s' %(nombre_cargar))
	return s
	#En esta función se pasa un entero que es el encargado de asignar al archivo correspondiente del arreglo 'archivo_de_parte'
def cargar_aux(nombre_cargar: str, num: int):
	global archivo_de_parte
	archivo_de_parte[num].append(cargar_archivo(nombre_cargar))
	print('Se ha guardado el archivo en la Parte ',num+1)
	return

#Función dedicada a cargar un Reproducir una Parte mediante la libreria de music21
	#Se le pasa un string que representa el nombre del 'archivo_de_parte' correspondiente
def reproducir_parte(arch: str):
	sp = midi.realtime.StreamPlayer(arch)
	print('Se está Reproduciendo una Parte')
	return sp.play()

#Función dedicada a Reproducir una Composición hecha de las 4 partes en 'archivo_de_parte' con los comandos de music21
def reproducir_composicion():
	cancion = stream.Score()
	for i in range(0,4):
		cancion.insert(0, archivo_de_parte[i])
	sp = midi.realtime.StreamPlayer(cancion)
	print('Se está Reproduciendo la Composición')
	return sp.play()

#Función asignada que Borra la parte seleccionada [REVISAAAAAAAR]
	#Se le pasa un entero que es el que se encarga de asignar al 'archivo_de_parte' correspondiente.
def borrar_parte(num: int):
	archivo_de_parte[num] = stream.Part()
	archivo_de_parte[num].append(None)
	print('Se ha borrado la Parte ',num+1)

#Función que transporta una Parte cargada
	#se le pasa un num para modificar ese num del 'archivo_de_parte' correspondiente
def transportar_parte(num: int, nombreinter: str):
	global archivo_de_parte
	archivo_de_parte[num] = archivo_de_parte[num].transpose("%s" %(nombreinter))
	print('Se transportó la Parte ',num+1,' en un intervalo de ',nombreinter)

#Función para Crear un Arpegio
	#El string 'nota_piano' se obtiene de los datos introducidos de la nota del piano para formar el string.
	#Se le pasa un entero que es el que se encarga de asignar al 'archivo_de_parte' correspondiente.
	#Entra el string 'transporte_arpegio' del intervalo asignado para transportar las notas del Arpegio.
def crear_arpegio(nota_piano: str, num: int, ran: int, transporte_arpegio: str):
	global archivo_de_parte
	nota = note.Note("%s" %(nota_piano.upper()))
	for i in range(0,ran):
		archivo_de_parte[num].append(nota)
		nota = nota.transpose('%s' %(transporte_arpegio))
	print('Se ha creado un Arpegio en la Parte ',num+1)
