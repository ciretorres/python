# -*- coding: utf-8 -*-

"""	Title: Listas en python
"""

# Declara una lista
thelist = ["uno", "dos", "tres"]

# Imprime toda la lista
print(thelist)

# Imprime el elemento 1
print(thelist[1])

# Cambia el valor del elemento 1 y reasigna un nuevo valor
thelist[1] = "cero"

for i in thelist:
	# Recorre una lista e imprime los valores
	print(i)

if "dos" in thelist:
	# Busca un elemento en la lista
	print("Yes, 'dos' is in the list")


# Imprime el tamaño de la lista
print(len(thelist))

# Agrega al final de la lista
thelist.append("cinco")

# Agrea un elemento en un lugar específico
thelist.insert(1, "ocho")

# Remueve el elemento deseado
thelist.remove("dos")

# Borra el último elemento de la lista
thelist.pop()

# Borra el elemento 0
del thelist[0]

# Borra toda la lista
del thelist

# Deja sin elementos la lista
thelist.clear()

# Copia una lista
newlist = thelist.copy()
newlist = list(thelist)

# Contruye una lista

otherlist = list(("nueve", "ocho", "siete", "seis"))

















