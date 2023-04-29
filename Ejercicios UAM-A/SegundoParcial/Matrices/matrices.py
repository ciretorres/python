# -*- coding: utf-8 -*-

"""	Title: Matrices
	Description: El código de matrices.py resuelve el problema 
	C=A-B. Donde A, B y C son matrices de tamaño nxm. El código 
	está desordenado, escríbalo nuevamente en el orden correcto 
	para que sea interpretado por python sin errores.
"""

def restaMatriz(A, B, C, n, m):
	for i in range(0,n):
		C.append([])
		for j in range(0,m): 
			valor = A[i][j] - B[i][j]
			C[i].append(valor)


