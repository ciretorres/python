import random

# -*- coding: utf-8 -*-

"""	Title: Juego de dados
	Author: Eric Torres
	UEA: Introducción a la programación
	Professor: Dra. Lizbeth Gallardo López
	Description: Dos niños están jugando a los dados. Cada uno
	tiene un dado, y los lanzan a la vez. El dado que tenga un
	valor mayor, gana. Pero también es posible que ambos dados
	tenga el mismo valor. Simular el juego de los dados y
	determinar el ganador o empate.
	Update: 15/06/2019
"""

play = input("\n Jugar a los dados?(si/no)\n>> ")

while play == "" or play == "si":

	dado1 = random.randint(1, 6)
	dado2 = random.randint(1, 6)

	if dado1 > dado2:
		print("\nGanador= dado1")
	elif dado1 < dado2:
		print("\nGanador= dado2")
	else:
		print("\n ¡¡¡¡¡¡¡¡\n  EMPATE\n !!!!!!!!\n:0\n")

	play = input("Jugar nuevamente?")