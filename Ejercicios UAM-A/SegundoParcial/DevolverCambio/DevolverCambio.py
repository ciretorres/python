# -*- coding: utf-8 -*-

"""	Title: Generar Vector
	Description: Después de pagado el importe en una 
	máquina expendedora de galletas, se requiere devolver 
	el cambio. La máquina cuenta con monedas y billetes de 
	las denominaciones actuales de México. El objetivo del 
	programa es devolver el mínimo número de monedas y 
	billetes posible. Suponga que la máquina expendedora 
	tiene monedas y billetes infinitos.
	
	El usuario ingresa: el importe a pagar por las galletas 
	y la denominación del billete o de la moneda con la 
	cual realizó el pago. La salida en pantalla será la 
	descripción del cambio devuelto, con el mínimo número 
	de billetes y de monedas.
"""

importe = float(input("\n Ingresa el importe\n>> "))
billete = float(input(" Ingresa el billete ó moneda\n>> "))

sobrante = billete - importe

print("\nTome su cambio:")

while sobrante != 0:

	if sobrante == .50:
		sobrante -= .50
		print(.50)
	elif sobrante == 1:
		sobrante -= 1
		print(1)
	elif sobrante == 2:
		sobrante -= 2
		print(2)
	elif sobrante >= 5 and sobrante < 10:
		sobrante -= 5
		print(5)
	elif sobrante >= 10 and sobrante < 20:
		sobrante -= 10
		print(10)
	elif sobrante >= 20 and sobrante < 50:
		sobrante -= 20
		print(20)
	elif sobrante >= 50 and sobrante < 100:
		sobrante -= 50
		print(50)
	elif sobrante >= 100 and sobrante < 200:
		sobrante -= 100
		print(100)
	elif sobrante >= 200 and sobrante < 500:
		sobrante -= 200
		print(200)
	elif sobrante >= 500 and sobrante < 1000:
		sobrante -= 500
		print(500)
	elif sobrante >= 1000:
		sobrante -= 1000
		print(1000)

print("\n Vuelva pronto por galletas!\n")

