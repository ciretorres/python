# -*- coding: utf-8 -*-

"""	Title: Comprar boletos
"""

def comprarBoletos(opcion):
	if opcion == 1:
		print("Costo total: $", 1295)
	elif opcion == 2:
		print("Costo total: $", 830)
	elif opcion == 3:
		print("Costo total: $", 719)
	elif opcion == 4:
		print("Costo total: $", 606)
	elif opcion == 5:
		print("Costo total: $", 492)
	else:
		print("Lo siento, esa zona no existe")
	return

def principal():
	print("\n Bienvenido!\n1. don ramon vip\n2. box superior\n3. zona fan de pie\n4. general\n5. sección c")

	opcion = int(input("\n Qué zona quieres comprar?\n>> "))

	comprarBoletos(opcion)
	return

principal()