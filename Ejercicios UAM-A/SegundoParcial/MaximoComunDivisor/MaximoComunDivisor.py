# -*- coding: utf-8 -*-

"""	Title: Máximo Común Divisor (MCD)
	Description: El Máximo Común Divisor (MCD) de tres 
	números enteros, es aquel que divide de forma entera a 
	los tres números. Por ejemplo, para 6, 4 y 2 el MCD es 2; 
	para 32, 16 y 24 el MCD es 8; para 15, 21 y 27 el MCD es 3.
	
	El usuario ingresa la tupla de números n1, n2 y n3, y el 
	programa calcula e imprime en la pantalla el MCD.
"""

# tup = [6, 4, 2]
# tup = [32, 16, 24]
# tup = [15, 21, 27]
# tup = tuple(tupla)

tup = []

tup.append(int(input("Dame n1\n>> ")))
tup.append(int(input("Dame n2\n>> ")))
tup.append(int(input("Dame n3\n>> ")))

mcd = 1

for i in range(2,10):
	if(tup[0] % i == 0 and tup[1] % i == 0 and tup[2] % i == 0):
		tup[0] = tup[0] / i
		tup[1] = tup[1] / i
		tup[2] = tup[2] / i
		mcd *= i

if(mcd == 1):
	print("Los valores de la tupla no tienen un Máximo Común Divisor")
else:
	print("El Máximo Común Divisor es:", mcd)

