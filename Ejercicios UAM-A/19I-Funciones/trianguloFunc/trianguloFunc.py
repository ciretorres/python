# -*- coding: utf-8 -*-

"""	Title: Programa que calcula si se forma un triángulo y de qué tipo es
	Author: Eric Torres
	UEA: Introducción a la programación
	Professor: Dra. Lizbeth Gallardo López
	Update: 22/06/2019
"""

def esTriangulo(ladoA, ladoB, ladoC):
	if(ladoA + ladoB > ladoC
		or ladoB + ladoC > ladoA
		or ladoC + ladoA > ladoB): # Con los paréntesis puede dar salto de línea
		return True
	else:
		return False

def tipoTriangulo(ladoA, ladoB, ladoC):
	if ladoA == ladoB and ladoB == ladoC:
		return "Es un triángulo equilatero"
	elif ladoA != ladoB and ladoB != ladoC and ladoA != ladoC:
		return "Es un triángulo escaleno"
	else:
		return "Es un triángulo isóceles"

def principal():
	ladoA = input("Dame el lado A: ")
	ladoB = input("Dame el lado B: ")
	ladoC = input("Dame el lado C: ")
	band = esTriangulo(ladoA, ladoB, ladoC)
	if band == True:
		tipo = tipoTriangulo(ladoA, ladoB, ladoC)
		print(tipo)
	else:
		print("Los lados no forman un triángulo")

principal()