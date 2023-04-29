# -*- coding: utf-8 -*-

"""	Title: Función de tablas de multiplicar
"""
print("\n Tablas de multiplicar")

def identifica():
	i = int(input("Dame el mínimo\n >> "))
	num = int(input("Dame el máximo\n >> "))
	return i, num

def multiplica(i, num):

	# i = 1
	while i <= num:
		print("")
		j = 1
		while j <= 10:
			print(i, "*", j, "=", i * j)
			j = j + 1
		i = i + 1
	return

def principal():
	i, num = identifica()
	multiplica(i, num)
	print("\nAdiós\n")

principal()