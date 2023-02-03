# -*- coding: utf-8 -*-

respuesta = input("Hola, ¿tienes hambre?: ")

if respuesta == "Si":
	print("Menu\n1. Hamburguesa\n2. Tlacoyo\n3. Ensalada\n4. Enchiladas\n5. Pastel de fresas\n6. Malteada")

	op = int(input("\nElige una opción: "))
	if op == 1:
		print("Preparando hamburguesa")
	elif op == 2:
		print("Preparando tlacoyo")
	elif op == 3:
		print("Preparando ensalada")
	elif op == 4:
		print("Preparando enchiladas")
	elif op == 5:
		print("Sirviendo pastel de fresas")
	elif op == 6:
		print("Preparando malteada")
	else:
		print("No tienes hambre")
else:
	print("Adiós")	