# -*- coding: utf-8 -*-

"""	Title: Números perfectos
	Description: Se dice que un número entero es perfecto 
	si la suma de sus divisores excepto él mismo es igual 
	al propio número. Por ejemplo, seis es número perfecto 
	porque 1 * 2 * 3 = 6 y 1 + 2 + 3 = 6. 
	Escriba un programa que obtenga los números perfectos 
	comprendidos entre 1 y 10000.
"""

print("\n–Números perfectos")
num = int(input("Ingresa un número entero\n: "))
print()

for i in range(1, num):

	suma = 0

	for j in range(1, (i//2) + 1):
		
		if i % j == 0:

			suma = suma + j

	if suma == i:
		print(i, "es número perfecto \n")