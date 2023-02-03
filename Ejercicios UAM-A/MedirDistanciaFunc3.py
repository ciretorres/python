# -*- coding: utf-8 -*-

import random

"""	Title: Operación con vectores
"""

def leerVector(n):
	vector = []	
	for i in range(n):
		# vector.append(int(input("Valor: ")))
		vector.append(random.randint(0,10000000))

	return vector

def sumaVector(vector_a, vector_b, n):
	vector_c = []	
	for i in range(n):
		vector_c.append(vector_a[i] + vector_b[i])

	return vector_c	

def restaVector(vector_a, vector_b, n):
	vector_d = []	
	for i in range(n):
		vector_d.append(vector_a[i] - vector_b[i])

	return vector_d

def multiVector(vector_a, vector_b, n):
	vector_e = []	
	for i in range(n):
		vector_e.append(vector_a[i] * vector_b[i])

	return vector_e

def divideVector(vector_a, vector_b, n):
	vector_f = []		
	for i in range(n):
		if vector_b[i] == 0:
			vector_f.append(-1)
		else:
			vector_f.append(vector_a[i] / vector_b[i])

	return vector_f

def principal():
	n = int(input(" Dame el tamaño de vectores\n>> "))

	vector_a = leerVector(n)
	vector_b = leerVector(n)

	vector_c = sumaVector(vector_a, vector_b, n)
	vector_d = restaVector(vector_a, vector_b, n)
	vector_e = multiVector(vector_a, vector_b, n)
	vector_f = divideVector(vector_a, vector_b, n)

	print("\nVectores")
	print(vector_a)
	print(vector_b)
	print("\nSuma")
	print(vector_c)
	print("\nResta")
	print(vector_d)
	print("\nMultiplica")
	print(vector_e)
	print("\nDivide")
	print(vector_f)
	return

principal()