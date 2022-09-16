# Tema: Divison con condicional
# Autor: Eric Torres Velasco
# UEA: Introduccion a la programacion
# Profesora: Dra. Lizbeth Gallardo Lopez
# Fecha: 29/01/2019

print("Ingresa dos valores enteros")

a = input("Valor 1: ")
b = input("Valor 2: ")

suma = a + b
resta = a - b
mult = a * b

if(b > 0):
	div = a / b
else:
	div = 0
	print("Indeterminado")

print("Suma: " + str(suma) 
	+ "\nResta: " + str(resta)
	+ "\nMult: " + str(mult)
	+ "\nDiv: " + str(div)
	)