# -*- coding: utf-8 -*-

"""	Title: SerieAlternante
	Description: Escriba un programa que empezando en el 
	número 2, le suma cinco, al siguiente término le suma 3; 
	y así alternadamente, hasta alcanzar el nímero 2500.
"""

serie = 2
cambio = 1

while serie <= 2500:

	print("%d\t", serie)
	
	if cambio == 1:
		serie += 5
		cambio = 0
	else:
		serie += 3
		cambio = 1