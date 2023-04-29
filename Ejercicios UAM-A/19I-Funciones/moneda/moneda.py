# -*- coding: utf-8 -*-

"""	Title: Tirar una moneda al aire 1000000
	Author: Eric Torres
	UEA: Introducción a la programación
	Professor: Dra. Lizbeth Gallardo López
	Update: 22/06/2019
"""

import random

def calcularFrec(lim):
	cara = 0
	cruz = 0
	for i in range(1, lim, 1):
		moneda = random.randint(0,1)
		if moneda == 0:
			cara = cara + 1
		else:
			cruz = cruz + 1
	return cara, cruz # Para regresar dos variables

def calcularPorc(cara, cruz, lim):
	pcara = 0
	pcruz = 0
	pcara = (cara / lim) * 100
	pcruz = (cruz / lim) * 100
	return pcara, pcruz

def principal():
	lim = 1000000
	cara, cruz = calcularFrec(lim) # Cuando la función regresa dos variables
	pcara, pcruz = calcularPorc(cara, cruz, lim)
	print(cara, pcara)
	print(cruz, pcruz)
	return

principal()
