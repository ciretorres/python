import math

""" Title: Número primo
	Author: Eric Torres
	UEA: Introducción a la programación
	Professor: Dra. Lizbeth Gallardo
	Description: Un número X es primo, siempre y cuando ese número 
				X  sea divisible solo entre el mismo y la unidad. 
				Dado un número entero que propondrá un usuario, 
				desde la línea de comandos, su programa deberá 
				indicar "el número X es primo" o "el número X no 
				es primo". 
	Update: 8/06/2019
"""
# -*- coding: utf-8 -*-

cont = 2

x = int(input("Ingresa un número entero\n: "))

while cont <= x:
	
	primo = True

	if x % cont == 0:
		primo = False
		
	cont = cont + 1

	if primo == True:
		print("\nEl", x,"es un número primo\n")
		break
	else:
		print("\nEl", x,"NO es un número primo\n")
		break




