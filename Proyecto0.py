#----------- Proyecto 0 - Michael Araya Murcia - Jose Julian Araya Castillo -------

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
    #Funcion que le pide al usuario la cantidad de jugadores que van a jugar y sus respectivos nombres
    #   Entrada: ninguna
    #   Salida: La lista de jugadores que van a jugar
    #   Restricciones: -La cantidad de jugadores debe de ser un entero positivo
    listadejugadores = []
    cantidad = int(input("Cuantos jugadores van a jugar: "))
    while cantidad <= 0:
        print("El numero de jugadores que ingreso es invalido. \nPorfavor ingrese un numero de jugadores valido")
        cantidad = int(input("Cuantos jugadores van a jugar: "))
    for jugador in range(cantidad):
        listadejugadores.append(input("Ingrese el nombre del jugador "+ str(jugador + 1) + ": "))
    
    
