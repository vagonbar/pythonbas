#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# break_frutas.py: pide un nombre de fruta y lo busca en una lista

frutas = ['uva', 'pera', 'melón', 'manzana', 'banana', 'naranja', 'palta', \
  'sandía', 'kiwi']

buscada = input("Fruta a buscar: ")
buscada = buscada.lower()  # convierte a minúscula, por si vino en mayúscula

hallado = False

for fr in frutas:
  if fr == buscada:
    hallado = True;
    break           # evita continuar recorriendo la lista inútilmente

if hallado:
  print ("'" + buscada + "'" + " está en la lista")
else:
  print ("'" + buscada + "'" + " no está en la lista")
  

