#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# continue_letras.py: cuenta la cantidad de letras 'p' o 'P' en un texto.

palabras = "Pedro Picapiedra padre picado pePino malpaso paPa paleta tapado"
cant = 0       # cantidad de p o P encontradas

for lt in palabras:
  if lt != 'p' and lt != 'P':
    continue   # vuelve al lazo repetitivo, en el siguiente item
  cant += 1    # incrementa la cantidad encontrada

print("Hay " + str(cant) + " letras 'p' o 'P' en el texto:")
print("   '" + palabras + "'")

  
  

