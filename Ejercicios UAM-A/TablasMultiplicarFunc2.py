# -*- coding: utf-8 -*-

"""	Title: Función de tablas de multiplicar
"""
print("\n Tablas de multiplicar")

def identifica():
	num = int(input("Dame el número\n >> "))
	return num

def tablasMult(n, m):
	for i in range(n, m+1, 1):
		print("")
		multiplica(i)		
	return

def multiplica(n):
	j = 1
	while j <= 10:
		print(n, "*", j, "=", n * j)
		j = j + 1
	return

def principal():
	n = identifica()
	m = identifica()
	tablasMult(n, m)
	print("\nAdiós\n")

principal()