import math
"""
	Tema: Area de un hexagono regular
	Autor: Eric
	UEA: Introduccion a la programacion
	Profesora: Dra. Lizbeth Gallardo Lopez
	Descripcion: 
	Este es un ejercicio para calcular el area de un hexagono regular. 
	El area de un hexagono regular es igual al perimetro de la figura 
	por la altura de la apotema dividida entre dos.

	Fecha: 24/05/2019
"""

lon = float(input("Ingresa la longitud de lados de un hexagono\n: "))
# ap = float(input("Ingresa la altura de la apotema\n: "))

ap = math.sqrt(math.pow(lon, 2) - math.pow(lon/2, 2))
p = lon * 6
area = p * ap / 2

print("Perimetro:", p, "cm")
print("Apotema:", ap, "cm")

print("\nArea:", area, "cm")