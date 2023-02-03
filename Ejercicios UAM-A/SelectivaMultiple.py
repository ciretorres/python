# -*- coding: utf-8 -*-
"""
	Tema: Estructura condicional selectiva múltiple
	Autor: Eric
	UEA: Introduccion a la programacion
	Profesora: Dra. Lizbeth Gallardo Lopez

	Fecha: 27/05/2019
"""

resp = input("Hola, ¿cómo te llamas?\n: ")
profesion = input("¿Cuál es tu profesión?\n: ")

if profesion == "Diseñador":
	print("Tu profesión es del área de Artes!")
elif profesion == "Físico":
	print("Tu profesión es del área de Físico-Matemáticas!")
elif profesion == "Médico":
	print("Tu profesión es del área de Ciencias Biológicas!")
else:
	print("Tu profesión no me es familiar...")