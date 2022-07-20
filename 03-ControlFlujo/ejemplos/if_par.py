#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# if_par.py : uso de if con y sin else


print("### if con else : determina si número es par")
num = input("Ingrese un número entero: ")    # ingresa como string
num = int(num)                               # convierte a entero
if num % 2 == 0:                             # si el resto es 0...
    print(num, "es par")                     # ...entonces es par  

print("\n### if con else : determina si número es par o impar")
num = input("Ingrese un número entero: ")    # ingresa como string
num = int(num)                               # convierte a entero
if num % 2 == 0:                             # si el resto es 0...
    print(num, "es par")                     # ...entonces es par  
else:                                        # de lo contrario (else)...
    print(num, "es impar")                   #...es impar

