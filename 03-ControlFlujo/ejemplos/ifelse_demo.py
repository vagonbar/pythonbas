#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ifelse_demo.py: demo de if..else

'''Realiza varias pruebas con la sentencia if..else.
'''

print()
print("==> valores booleanos True==1, False==0")
if True == 1:
  print("True equivale a 1")

if False == 0:
  print("False equivale a 0")
  
if 1:
  print("1 es True")
else:
  print("1 no es True")
  
if 0:
  print("0 no es True")
else:
  print("0 es False")
  
print()
print("==> valores booleanos de las cadenas de caracteres")
if "":
  print("La cadena vacía tiene valor True")
else:
  print("La cadena vacía tiene valor False")
  
if "aa":
  print("Una cadena no vacía tiene valor True")
else:
  print("Una cadena no vacía tiene valor False")
  
print("\n==> valores booleanos de lista llena y vacía")
lsllena = [0,10,20]
lsvacia = []
if lsllena:
  print("La lista llena tiene valor True")
else:
  print("La lista llena tiene valor False")

if lsvacia:
  print("La lista vacía tiene valor True")
else:
  print("La lista vacía tiene valor False")

print("\n==> Operador in en listas")
print("Lista:", lsllena) 
for j in 10, 100:
  if j in lsllena:
    print(j, "está en la lista")
  else:
    print(j, "no está en la lista")
print()

