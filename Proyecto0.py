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
	"""
	Funcion que le pide al usuario la cantidad de jugadores que van a jugar y sus respectivos nombres.
	Entrada: Ninguna.
	Salida: La lista de jugadores que van a jugar.
	Restricciones: La cantidad de jugadores debe de ser un entero positivo.
	"""
	aceptar = False

	listadejugadores = []

	while not aceptar:
		cantidad = input("Ingrese cantidad de jugadores: ")

		if not cantidad.isnumeric():
			print("La cantidad tiene que ser un numero positivo.")
		elif cantidad.isnumeric() and int(cantidad) <= 0:
			print("La cantidad tiene que ser un numero positivo.")
		else:
			aceptar = True

	cantidad = int(cantidad)

	for jugador in range(cantidad):
		listadejugadores.append(input("Ingrese el nombre del jugador "+ str(jugador + 1) + ": "))
	return listadejugadores

def abrirPreguntas():
	archivo = open("prueba.json","r")
	for linea in archivo.readlines():
		print(linea)
	archivo.close()

#=====================================================va dentro del main=================================
listadejugadores = cantidadjugadores()
puntuaciones = []

for jugador in listadejugadores:
    puntuaciones.append(0)
#====================================================================================================	
puntuacion(listadejugadores, puntuaciones)

