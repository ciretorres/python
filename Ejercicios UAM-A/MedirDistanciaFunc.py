# -*- coding: utf-8 -*-

"""	Title: Medir Distancia Función
"""

def leerVector():
	# x = float(input("Ingresa vector x: "))
	# y = float(input("Ingresa vector y: "))
	# z = float(input("Ingresa vector z: "))
	# return [x, y, z]
	vector = []	
	for i in range(3):
		vector.append(int(input("Valor: ")))

	return vector

def sumaVector(vector_a, vector_b):
	# sumaX = vector_1[0] + vector_2[0]
	# sumaY = vector_1[1] + vector_2[1]
	# sumaZ = vector_1[2] + vector_2[2]
	# return [sumaX, sumaY, sumaZ]
	vector_c = []	
	for i in range(3):
		vector_c.append(vector_a[i] + vector_b[i])

	return vector_c	

def principal():
	vector_a = leerVector()
	vector_b = leerVector()
	vector_c = sumaVector(vector_a, vector_b)
	print(vector_a)
	print(vector_b)
	print(vector_c)
	return

principal()