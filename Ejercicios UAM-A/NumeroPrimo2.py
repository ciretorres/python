# -*- coding: utf-8 -*-

"""	Title: Números primos
	Description: Construir un programa que determine los 
	números primos menores a cincuenta. Un número es primo, 
	si sus únicos divisores son él mismo y la unidad
"""

print("Números primos comprendidos entre 1 y", 50, "\n\n")

cont = 0

for num in range(1, 50):

	band = 0

	for i in range(2, (num//2) + 1):

		if num % i == 0:
			band = 1

	if band == 0:
		print(num, "es primo \n")
		cont = cont + 1

print(cont, "Números primos en el rango de 1 a",  50)