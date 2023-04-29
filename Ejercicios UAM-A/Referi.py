import random

# -*- coding: utf-8 -*-
"""	Title: Referi
	Description: Retomando el juego de piedra-papel-tijera, 
	vamos a reformular el código, empleando una función 
	llamada “referi“, la cual estará encargada de 
	determinar al ganador de la jugada.
"""

print("Juguemos a piedra papel o tijera \n 1. Piedra \n 2. Papel \n 3. Tijera \n")

yours = int(input("Cual es tu tirada: "))

mine = random.randint(1,3)

print("Mi tirada es: ", mine)

def referi(mine, yours):
	ganador = ""
	if mine == yours:
		ganador = "Empate entre tu y yo \n"
	else:
		if yours == 1:
			if mine == 2:
				ganador = "Gane !!!! \n"
			else:
				ganador = "Ganaste!!! \n"
		elif yours == 2:
			if mine == 1:
				ganador = "Gane !!!! \n"
			else:
				ganador = "Ganaste!!! \n"
		elif yours == 3:
			if mine == 1:
				ganador = "Gane !!!! \n"
			else:
				ganador = "Ganaste!!! \n"
		else:
			ganador = "ERROR en tu tiro!!! \n"

	return ganador

print(referi(mine,yours))

