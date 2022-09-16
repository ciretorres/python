import math

# Tema: Area de un circulo
# Autor: Eric Torres Velasco
# UEA: Introduccion a la programacion
# Profesora: Dra. Lizbeth Gallardo Lopez
# Fecha: 21/05/2019

radio = float(input("Ingresa el radio de un circulo: "))

# area = 3.141592653589793 * radio**2
area = math.pi * math.pow(radio, 2)

print("\nArea:", area)