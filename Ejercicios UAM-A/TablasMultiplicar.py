# -*- coding: utf-8 -*-

"""	Title: Tablas de Multiplicar
"""

print("\n Tablas de multiplicar")

num = int(input("Hasta qué número de tablas quieres multiplicar?\n >> "))

for i in range(1, num+1, 1):
	print("")
	for j in range(1, 11, 1):
		print(i, "*", j, "=", i * j)

print("\nAdiós!\n")

i = 1
while i <= num:
	print("")
	j = 1
	while j <= 10:
		print(i*j)
		j = j + 1
	i = i + 1