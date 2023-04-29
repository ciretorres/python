# -*- coding: utf-8 -*-

""" Title: Impares
	Author: Eric Torres
	UEA: Introducción a la programación
	Professor: Dra. Lizbeth Gallardo
	Description: Se desea imprimir en pantalla la serie de 
				números impares que existen en un rango que
				el usuario especifica.
	Update: 11/06/2019
"""

print("Números impares\n")

r = int(input(" A partir de dónde quieres iterar?\n>> "))

s = int(input(" Hasta dónde quieres iterar?\n>> "))

rango = [r, s]

# for i in range(rango[0], rango[1], 1):
for i in range(r, s, 1):
	# if not i % 2 == 0:
	if i % 2 != 0:
		print(i)

print("\nYa terminé\n")





# r = 1

# while r <= 10000:
# 	if not r % 2 == 0:
# 		print(r)

# 	r = r + 1