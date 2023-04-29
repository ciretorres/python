# -*- coding: utf-8 -*-

"""	Title: Estructura condicional repetitiva for
	Author: Eric
	UEA: Introduccion a la programacion
	Professor: Dra. Lizbeth Gallardo Lopez

	Update: 11/06/2019
"""

print("\nEstructura de control de flujo\n condicional repetitiva For.\n")

maximo = int(input(" ¿Cuántas veces quieres iterar?\n>> "))

# for i in range(maximo):
# for i in range(0, maximo, +1):
for i in range(maximo, 0, -1):
	print(i)

print("\nYa terminé de iterar!\n")