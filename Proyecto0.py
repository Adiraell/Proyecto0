#----------- Proyecto 0 - Michael Araya Murcia - Jose Julian Araya Castillo -------
def mensajeBienvenida():
	"""
	Procedimiento que imprime un mensaje de bienvenida con la descripción y las reglas del juego.
	Entradas: Ninguna
	Salidas: Ninguna
	Restricciones: Ninguna
	"""
	print(" %%%%%%  %%%%%   %%%%%%  %%  %%  %%%%%%   %%%% ")
	print("   %%    %%  %%    %%    %%  %%    %%    %%  %%")
	print("   %%    %%%%%     %%    %%  %%    %%    %%%%%%")
	print("   %%    %%  %%    %%     %%%%     %%    %%  %%")
	print("   %%    %%  %%  %%%%%%    %%    %%%%%%  %%  %%")
	print("        										  ")

	print("Descripción: Trivia es un juego en donde jugadores se reunen para ver quien sabe mas sobre un tema en especifico.")
	print("Reglas: ")
	print("1) Cada jugador debe responder 5 preguntas, durante 3 rondas \n   al final del juego el que haya acertado mas preguntas es el ganador.")

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

def abrirPreguntas():
	archivo = open("prueba.json","r")
	for linea in archivo.readlines():
		print(linea)
	archivo.close()

cantidadjugadores()
abrirPreguntas()