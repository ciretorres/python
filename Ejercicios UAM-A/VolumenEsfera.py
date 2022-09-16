import math

# Tema: Volumen de una esfera
# Autor: Eric Torres Velasco
# UEA: Introduccion a la programacion
# Profesora: Dra. Lizbeth Gallardo Lopez
# Fecha: 21/05/2019

radio = float(input("Ingresa el radio de una esfera: "))

# area = 3.141592653589793 * radio**2
volumen = (4 * math.pi * math.pow(radio, 3)) / 3

print("\nVolumen:", volumen)