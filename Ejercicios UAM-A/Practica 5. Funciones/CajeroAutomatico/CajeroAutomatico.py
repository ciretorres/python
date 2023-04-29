# -*- coding: utf-8 -*-

import random

"""	Title: Cajero Automático
"""

def generarSaldo():
	saldo = random.randint(0, 10000)
	return saldo

def retirar(saldo):
	r = int(input("Cuánto quieres retirar\n >> "))
	saldo = saldo - r
	print("Monto a retirar:", r)
	print("Monto actual:", saldo)
	return saldo

def depositar(saldo):
	d = int(input("Cuánto quieres depositar\n >> "))
	saldo = saldo + d
	print("Monto a depositar:", d)
	print("Monto actual:", saldo)
	return saldo

def consultar(saldo):
	print("\nMonto actual:", saldo)
	return

def imprimirMenu():
	print("\n1. Retirar dinero\n2. Depositar dinero\n3. Consultar saldo\n4. Salir del menú")
	return

def principal():
	saldo = generarSaldo()
	opcion = 0
	while opcion != 4:
		imprimirMenu()
		opcion = int(input("\nElige una opción: "))
		if opcion == 1:
			saldo = retirar(saldo)
		elif opcion == 2:
			saldo = depositar(saldo)
		elif opcion == 3:
			consultar(saldo)

	return		

principal()
	