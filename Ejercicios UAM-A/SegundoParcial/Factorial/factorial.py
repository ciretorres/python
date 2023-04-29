# -*- coding: utf-8 -*-

"""	Title: Factorial
	Description: Calcular el factorial de un número e 
	imprimir la serie de números involucrados en el cálculo 
	de fractorial. Ejemplo:
	$factorial 3
	3*2*1 =6.
"""

# factorial = int(input("\n Ingresa factorial\n>> "))
# fac = 1
# fact = ""
# for i in range(factorial, 0, -1):
# 	fac *= i
# 	if(i == 1):
# 		fact += str(i)	
# 	else:
# 		fact += str(i) + "*"
# print(fact + " = " + str(fac))

def calcularFactorial(factorial):
	"""	Esta función calcula el factorial de un número entero.
	"""
	
	fac = 1
	fact = ""
	for i in range(factorial, 0, -1):
		fac *= i
		fact += imprimirSerie(i)
		
	return fac, fact

def imprimirSerie(i):
	"""	Esta función imprime la serie números involucrados
		en el cálculo de factorial de i de calcularFactorial()
	"""

	fact = ""
	if(i == 1):
		fact += str(i)	
	else:
		fact += str(i) + "*"
	
	return fact

def leerDato():
	f = int(input("\n Ingresa factorial\n>> "))
	return f

def principal():
	print("\nCALCULA EL FACTORIAL\nDE UN NÚMERO ENTERO")
	factorial = leerDato()
	fac, fact = calcularFactorial(factorial)
	print(fact + " = " + str(fac))
	return

principal()