import math
"""
	Tema: Volumen de un cono
	Autor: Eric
	UEA: Introduccion a la programacion
	Profesora: Dra. Lizbeth Gallardo Lopez
	Descripcion: 
	Este es un ejercicio para calcular el volumen de un cono. 
	El volumen de un cono es igual a la altura por pi por el radio
	al cuadrado sobre tres.

	Fecha: 24/05/2019
"""

radio = float(input("Ingresa el radio de un cono\n: "))
height = float(input("Ingresa la altura de un cono\n: "))

vol = math.pi * math.pow(radio, 2) * height / 3

print("Volumen:", vol, "cm^3")
