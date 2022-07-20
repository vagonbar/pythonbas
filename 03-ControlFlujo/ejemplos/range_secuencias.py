#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# rangedemo.py: genera una progresión aritmética


print("==> Numerar los días de la semana")
semana = ['lunes','martes','miércoles','jueves','viernes','sábado','domingo']

for pos in range(0,len(semana)):
  print("Día " + str(pos) + ":   " + semana[pos])

print("\n==> Muestras de la función range():")
print("\nrange(10):")
for i in range(10):
  print(i, end=" ")
print("\nrange(3,10):")
for i in range(3,10):
  print(i, end=" ")
print("\nrange(0,10,2):")
for i in range(0,10,2):
  print(i, end=" ")
print("\nrange(10,0,-1):")
for i in range(10,0,-1):
  print(i, end=" ")
print()


