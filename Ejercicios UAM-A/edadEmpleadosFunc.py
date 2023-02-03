# -*- coding: utf-8 -*-

"""	Title: Edad Empleados Función
"""

def calculaPuesto(edad):
	# puesto = ""
	if edad >= 15 and edad <= 18:
		puesto = "Call center"
	elif edad >= 19 and edad <= 25:
		puesto = "Administrador"
	elif edad >= 25 and edad <= 45:
		puesto = "Jefe de piso"
	else:
		puesto = "No hay chamba para mayores de 45 :("
	return puesto

def principal():

	nombre = input("Ingresa tu nombre: ")
	edad = int(input("Ingresa tu edad: "))

	print("\nNombre: ", nombre, "\nEdad: ", edad, "\nPuesto: ", calculaPuesto(edad))
	return

principal()
