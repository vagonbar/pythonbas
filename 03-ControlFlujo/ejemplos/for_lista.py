#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# for_lista.py: demo de for

# Define una lista de elementos de diferentes tipos.
# Recorre la lista mostrando valor y tipo de cada elemento.
# Muestra el largo de la lista.

print("### crea una lista")
ls = [ 'martes', "dos palabras", True, False, 32, 87.98, 3/2**3, 12., \
        12 + 3j, 1j, None, [0, 1, 2] ]
print("Lista:")
print("  ", ls)
print()

print("### recorre la lista mostrando valor y tipo de dato")
for item in ls:                          # para cada elemento en la lista ls
  print ("  ", item, " :  ", type(item)) #   imprime elemento y su tipo 

print ("Largo de la lista:", len(ls))    # imprime el largo de la lista


