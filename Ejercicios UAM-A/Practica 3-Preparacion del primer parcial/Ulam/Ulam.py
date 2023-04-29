# -*- coding: utf-8 -*-

"""	Title: Sucesión de ULAM
	Author: Eric Torres
	UEA: Introducción a la programación
	Professor: Dra. Lizbeth Gallardo López
	Description: Consiste en iniciar con un valor numérico
	entero dado por el usuario. Si el número es par, se divide
	entre 2. Si el número es impar, se multiplica por 3 y se
	agrega 1. Finalmente se repiten los dos pasos anteriores,
	hasta obtener el número 1.
	Update: 15/06/2019
"""

print("\n La sucesión de S. ULAM")
entero = int(input(" Dame un número entero\n>> "))

m = ""
while entero > 1:
	
	if entero % 2 == 0:
		entero = entero / 2
	else:
		entero = entero * 3 + 1
	
	m += str(int(entero))+" "

print("\n", m, "\n")