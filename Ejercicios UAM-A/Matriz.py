# -*- coding: utf-8 -*-

import random

"""	Title: Matriz
"""

def generarMatriz(n):
	matriz = []

	for i in range(n):
		matriz.append([])
		for j in range(n):
			matriz[i].append(random.randint(1,10))	

	return matriz

def principal():
	n = int(input("\n Dame un número para la matriz\n>> "))
	matriz = generarMatriz(n)
	print(matriz)

principal()