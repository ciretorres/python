# Tema: Operaciones aritmeticas
# Autor: Eric Torres Velasco
# UEA: Introduccion a la programacion
# Profesora: Dra. Lizbeth Gallardo Lopez
# Fecha: 21/05/2019

valor1 = input("Ingresa dos valores enteros \nValor 1: ")

valor2 = input("Valor 2: ")

# Cast: forzar a un valor convertirse en otro tipo de dato
valor1 = int(valor1)
valor2 = int(valor2)

suma = valor1 + valor2
rest = valor1 - valor2
multi = valor1 * valor2

print('\nSuma:', suma, ', Resta:', rest,
	', Multiplicacion:', multi)
