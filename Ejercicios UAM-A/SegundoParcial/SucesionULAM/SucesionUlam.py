# -*- coding: utf-8 -*-

"""	Title: Sucesión de ULAM
	Author: Eric Torres
	UEA: Introducción a la programación
	Professor: Dra. Lizbeth Gallardo López
	Description: La sucesión de ULAM consiste en

	a) Inicia con cualquier entero positivo (dado por el usuario).

	b) Si el número es par, divídelo entre 2. Si es impar, 
	multiplícalo por 3 y agrégale 1 

	c) Repetir el paso b hasta que se obtenga un valor 1.

	El programa deberá imprimir en la pantalla la sucesión 
	de ULAM.
"""

print("\n La sucesión de S. ULAM")
entero = int(input("\n Dame un número entero positivo\n>> "))

m = ""
while entero > 1:
	
	if entero % 2 == 0:
		entero = entero / 2
	else:
		entero = entero * 3 + 1
	
	m += str(int(entero))+" "

print("\n", m, "\n")