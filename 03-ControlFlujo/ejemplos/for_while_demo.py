#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# for_while_demo.py: uso de for, while, else, break, continue, pass.

'''Muestra el uso de for...else y while...else.
Muestra también un uso sencillo de break, continue y pass.
Notar uso de , en print, y \n para cambio de línea.
'''

print("Demo simple de control de flujo\n")
print("==> for...else")
for i in range(0,10):
  print(i, end=" ")
else:
  print("\nfor...else: fin\n")


print("==> while...else")
i = 0
while i < 10:
  print(i, end=" ")
  i = i + 1
else:                # else para el while
  print("\nwhile..else: fin\n")


print("==> for...else con continue y pass, muestra sólo pares")
for i in range(0,10):
  if i % 2 != 0:
    continue         # vuelve al siguiente elemento del for
  else:              # else para el if
    pass
  print(i, end=" ")  # el continue evita llegar a esta sentencia
else:                # else para el for
  print("\nfor...else, sólo pares: fin\n")


print("==> for...else con break: fin de repetición al hallar un cierto valor")
valor = 7
for i in range(0,10):
  if i == valor:
    print("\ncorte en valor buscado: ", valor)
    break           # sale del bucle for
  else:
    print(i, end=" ")
    
