import math
"""
	Tema: Distancia a partir de dos puntos
	Autor: Eric
	UEA: Introduccion a la programacion
	Profesora: Dra. Lizbeth Gallardo Lopez
	Descripcion: 
	Este es un ejercicio para calcular la distancia a partir de dos puntos:
	punto1 - (x1, y1) y punto2 - (x2, y2).
	El la distancia entre dos puntos es igual la raíz cuadrada de 
	la coordenada A al cuadrado más la coordenada B al cuadrado.

	Fecha: 24/05/2019
"""

coord_a = input("Ingresa las coordenadas (x, y) de A\n: ").split(',')
x1 = float(coord_a[0])
y1 = float(coord_a[1])

coord_b = input("Ingresa las coordenadas (x, y) de B\n: ").split(',')
x2 = float(coord_b[0])
y2 = float(coord_b[1])

dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print("\nCoordenada A:", coord_a)
print("Coordenada B:", coord_b)

print("\nDistancia:", dist, "u.")