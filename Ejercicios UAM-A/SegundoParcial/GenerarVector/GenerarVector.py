# -*- coding: utf-8 -*-

import random

"""	Title: Generar Vector
	Description: Sea A un vector de tamaño n. Donde n es un 
	valor definido por el usuario. Los valores son enteros y 
	deberán generarse de manera aleatoria. Obtener un 
	vector B con los valores representativos de A; es decir, 
	no deben guardarse los valores repetidos del vector A.
"""

def generarVector(n):
	vector = []	
	for i in range(n):
		vector.append(random.randint(0,100))

	return vector

def generaVectorB(vectorA, n):
	vectorB = []
	print(vectorA)
	

	# for i in range(1, n):
	# 	if(vectorA[i] == vectorB[j]):
	# 		i = i + 1
	# 	else:
	# 		j=j+1

	# 		vectorB[j].insert(j, vectorA[i])
	# 		j = 0

	return vectorB


def principal():
	n = int(input(" Dame el tamaño de vectores\n>> "))
	vector_a = generarVector(n)
	vector_b = generaVectorB(vector_a, n)

	# print("Vector A", vector_a)
	# print("Vector B", vector_b)
	return

principal()