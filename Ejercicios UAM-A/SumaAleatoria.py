import random

# -*- coding: utf-8 -*-

"""	Title: Suma Aleatoria
	Author: Eric Torres
	UEA: Introducción a la programación
	Professor: Dra. Lizbeth Gallardo López
	Description: Realizar la suma de números aleatorios 
	generados en un rango [1...100]. La suma deberá detenerse,
	cuando el acumulado (la suma) de esos números sea igual o
	mayor a 10,000.
	Update: 15/06/2019
"""

suma = 0

while suma <= 10000:

	rand = random.randint(1,100)
	
	suma += rand

	# print(suma)

print("\nFin\n")