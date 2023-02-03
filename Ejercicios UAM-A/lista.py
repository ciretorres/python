# -*- coding: utf8 -*-
print("Hagamos una lista")

def menu():
	print("i. insertar\nr. remover\no. ordenar\np. imprimir\nx.salir")
	return

def insertar(lista):
	actividad=input("ingresa una nueva actividad")
	lista.append(actividad)
	return 

def  remover(lista):
	for i in range(len(lista)):
		print(i, lista[i])
	
	actividad= int(input("que numero de la lista quieres eliminar"))
	lista.pop(actividad)

	return
def ordenar(lista):
	lista.sort()
	imprimir(lista)
	return

def imprimir(lista):
	print(lista)
	return

def principal():
	lista = []
	x=1
	while x==1:
		menu()
		opcion=input("Escribe una opcion")
		if opcion=="i":
			insertar(lista)
		elif opcion=="r":
			remover(lista)
		elif opcion=="o":
			ordenar(lista)
		elif opcion=="p":
			imprimir(lista)
		elif opcion=="x":
			x=0

	return
 
principal()


