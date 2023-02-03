# -*- coding: utf-8 -*-

""" Title: Miscelánea Flor de Jamaica
	Author: Eric Torres
	UEA: Introducción a la programación
	Professor: Dra. Lizbeth Gallardo
	Description: Programa para la Miscelánea Flor de Jaimarca, que
	tiene promociones de descuento para sus clientes.
	Update: 4/06/2019
"""

compra = float(input("Bienvenido a la Flor de Jamaica\nIngresa el monto de compra\n: "))

if compra >= 100 and compra <= 200:
	print("\nCantidad a pagar: $", compra * .97)
elif compra > 200 and compra <= 500:
	print("\nCantidad a pagar: $", compra * .95)
elif compra > 500 and compra <= 800:
	print("\nCantidad a pagar: $", compra * .92)
elif compra > 800:
	print("\nCantidad a pagar: $", compra * .90)
else: 
	print("\nDisculpa, no hay descuento para tu monto de compra")
	print("Cantidad a pagar: $", compra)

print("Regresa pronto!")