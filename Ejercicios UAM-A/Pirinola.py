import random

""" Title: Pirinola
	Author: Eric Torres
	UEA: Introducción a la programación
	Professor: Dra. Lizbeth Gallardo
	Description: Se desea simular el juego de la pirinola. 
				Hay siete valores que se pueden asociar a un 
				número aleatorio entre 1 y 7.
	Update: 8/06/2019
"""
# -*- coding: utf-8 -*-

play = True

while play == True:
	op = int(input("Elige una opción:\n1. Rodar la Pirinola\n2. Salir\n>> "))

	if op == 1:
		val = random.randint(1,7)

		if val == 1:
			print("\nToma uno\n")
		elif val == 2:
			print("\nToma dos\n")
		elif val == 3:
			print("\nToma todo\n")
		elif val == 4:
			print("\nPon uno\n")
		elif val == 5:
			print("\nPon dos\n")
		elif val == 6:
			print("\nPierdes todo\n")
		else:
			print("\nTodos ponen\n")

	else:
		play = False

print("\nChao!")

