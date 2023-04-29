# -*- coding: utf-8 -*-
"""
	Tema: Estructura condicional repetitiva while
	Autor: Eric
	UEA: Introduccion a la programacion
	Profesora: Dra. Lizbeth Gallardo Lopez

	Fecha: 27/05/2019
"""

print("Ejemplificado la estructura condicional repetitiva While.")

limite = float(input("\nIngresa un número límite para empezar\n: "))
decre = float(input("Ingresa el decremento\n: "))

a = limite

while a > 0:
	print(a, "Sigo adentro")
	a = a - decre

print("\nEso fue todo, adiós!")