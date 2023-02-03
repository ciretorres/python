# -*- coding: utf-8 -*-

"""	Title: Programa que saluda al usuario
	Author: Eric Torres
	UEA: Introducción a la programación
	Professor: Dra. Lizbeth Gallardo López
	Update: 22/06/2019
"""

def saludo(nombre):
	print("Buenos días " + nombre)
	return

def identifica():
	nombre = input("Cuál es tu nombre ")
	return nombre

def principal():
	nombre = identifica()
	saludo(nombre)
	return

principal()

