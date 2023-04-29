# -*- coding: utf-8 -*-

""" Title: Tabla de multiplicar
	Author: Eric Torres
	UEA: Introducción a la programación
	Professor: Dra. Lizbeth Gallardo
	Description: Dado un valor n, obtenga la tabla de multiplicar 
	del 1 al 10 para n.
	Update: 4/06/2019
"""

n = float(input("Ingresa un número para multiplicar\n: "))
i = 1

while i <= 10:
	print(int(n), "*", i, "=", n * i)
	i = i + 1

print("\nFin del programa")