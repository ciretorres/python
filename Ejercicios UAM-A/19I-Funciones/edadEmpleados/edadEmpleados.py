# -*- coding: utf-8 -*-

"""	Title: Asignar un puesto según el nombre y la edad de la persona
	Author: Eric Torres
	UEA: Introducción a la programación
	Professor: Dra. Lizbeth Gallardo López
	Update: 22/06/2019
"""

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
puesto = ""

if edad >= 15 and edad <= 18:
	puesto = "Call center"
elif edad >= 19 and edad <= 25:
	puesto = "Administrador"
elif edad >= 25 and edad <= 45:
	puesto = "Jefe de piso"
else:
	puesto = "No hay chamba para mayores de 45 :("

print("Nombre: ", nombre, "\nEdad: ", edad, "\nPuesto: ", puesto)
