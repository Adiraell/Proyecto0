#----------- Proyecto 0 - Michael Araya Murcia - Jose Julian Araya Castillo -------

print(" %%%%%%  %%%%%    %%%%%%  %%       %%  %%%%%%     %%%% ")
print("      %%        %%      %%      %%        %%       %%       %%         %%     %%")
print("      %%        %%%%%          %%        %%      %%       %%         %%%%%%")
print("      %%        %%      %%       %%          %%%%           %%         %%      %%")
print("      %%        %%      %%  %%%%%%       %%        %%%%%%    %%      %%")
print("        										  ")



print("Descripción: Trivia es un juego en donde jugadores se reunen para ver quien sabe mas sobre un tema en especifico.")
print("Reglas: ")
print("1) Cada jugador debe responder 5 preguntas, durante 3 rondas \n   al final del juego el que haya acertado mas preguntas es el ganador.")

<<<<<<< HEAD

global listadejagadores


def puntuacion(listadejugadores, puntuaciones):
    #Funcion que se encarga de imprimir la puntuacion en pantalla de cada jugador
    #
    #
    #
    i = 0
    print("-"*100)
    for jugadores in listadejugadores:
        print("| "+str(listadejugadores[i])+": " , puntuaciones[i])
        i+= 1
    print("-"*100)
def cantidadjugadores():
=======
def cantidadJugadores():
>>>>>>> upstream/master
	"""
	Funcion que le pide al usuario la cantidad de jugadores que van a jugar y sus respectivos nombres.
	Entrada: Ninguna.
	Salida: La lista de jugadores que van a jugar.
	Restricciones: La cantidad de jugadores debe de ser un entero positivo.
	"""
	aceptar = False

	listadejugadores = {}

	while not aceptar:
		cantidad = input("Ingrese cantidad de jugadores: ")

		if not cantidad.isnumeric():
			print("La cantidad tiene que ser un numero positivo.")
		elif cantidad.isnumeric() and int(cantidad) <= 0:
			print("La cantidad tiene que ser un numero positivo.")
		else:
			aceptar = True

	cantidad = int(cantidad)

<<<<<<< HEAD
	for jugador in range(cantidad):
		listadejugadores.append(input("Ingrese el nombre del jugador "+ str(jugador + 1) + ": "))
	return listadejugadores
=======
	for i in range(0,cantidad):
		nombre = input("Ingrese el nombre del jugador " + str(i + 1) + ": ")
		listadejugadores["jugador"+str(i+1)] = {}
		listadejugadores["jugador"+str(i+1)]["nombre"] = nombre 
		listadejugadores["jugador"+str(i+1)]["puntuacion"] = 0

	return listadejugadores

def mostrarPuntuacion(listadejugadores):
	"""
	Función que muestra en pantalla la lista de jugadores con sus puntuaciones.
	Entrada: Un diccionario con los jugadores.
	Salidas: Ninguna.
	Restricciones: La entrada tiene que ser un diccionario. 
	"""
	for key in (listadejugadores):
		print(listadejugadores[key])
>>>>>>> upstream/master

def abrirPreguntas():
	archivo = open("prueba.json","r")
	for linea in archivo.readlines():
		print(linea)
	archivo.close()

<<<<<<< HEAD
#=====================================================va dentro del main=================================
listadejugadores = cantidadjugadores()
puntuaciones = []

for jugador in listadejugadores:
    puntuaciones.append(0)
#====================================================================================================	
puntuacion(listadejugadores, puntuaciones)

=======

def main():
	mensajeBienvenida()
	lista = cantidadJugadores()
	mostrarPuntuacion(lista)

main()
>>>>>>> upstream/master
