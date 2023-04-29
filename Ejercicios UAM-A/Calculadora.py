# -*- coding: utf-8 -*-

""" Title: Calculadora
	Author: Eric Torres
	UEA: Introducción a la programación
	Professor: Dra. Lizbeth Gallardo
	Description: 
	Update: 4/06/2019
"""

op = 0

while op != 5:
	a = float(input("Ingresa el primer número\n: "))
	b = float(input("Ingresa el segundo número\n: "))

	print("\n1.Suma\n2.Resta\n3.Producto\n4.División\n5.Salir")

	op = int(input("Ingresa la operación\n: "))

	if op == 1:
		print(a + b)
	elif op == 2:
		print(a - b)
	elif op == 3:
		print(a * b)
	elif op == 4:
		if b == 0:
			print("No puedo dividir entre cero")			
		else:
			print(a / b)
	elif op == 5:
		print("Adiós")
	else:
		print("Ingresa una opción válida")
		
