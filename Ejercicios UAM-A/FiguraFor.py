# -*- coding: utf-8 -*-

"""	Title: FiguraFor
	Author: Eric Torres
	UEA: Introducción a la programación
	Professor: Dra. Lizbeth Gallardo López
	Description: A partir del valor de "n", determinado por el
	usuario, construir la siguiente figura, por ejemplo, n=6:
		123456
		12345
		1234
		123
		1
	Update: 15/06/2019
"""

n = int(input("\n Dame un número\n>> "))
print()

for i in range(n, 0, -1):
	m = ""

	for j in range(1, i+1, 1):
		m += str(j)
	
	print(m)

print()