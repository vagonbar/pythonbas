#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# multiplos.py : detecta múltiplos en secuencia aleatoria
#                muestra uso de break, continue y pass

'''Genera una lista de 100 enteros aleatorios entre 0 y 99,
 pide un número para buscar múltiplos de él, y una cantidad de múltiplos
 a buscar; imprime un mensaje cada 10 números examinados.
'''

from random import random    # generador aleatorio entre 0.0 y 1.0

mult = int(input("Múltiplos a buscar: "))
cant = int(input("Cantidad de múltiplos a buscar: "))

ls_nros = []                 # lista vacía
for i in range(50):
    nro_decimal = random()               # nro aleatorio entre 9.0 y 1.0
    nro_entero = int(nro_decimal * 100)  # entero entre 0 y 99
    ls_nros = ls_nros + [nro_entero]     # agrega entero a la lista
print(ls_nros)

cont_mult = 0    # contador de múltiplos de mult hallados
dc_mult = {}     # diccionario vacío { múltiplo : posición en la lista }
print("Examinados: ", end=" ")  # para mostrar el avance

for i in range(len(ls_nros)):   # recorre la lísta usando el índice i
    if ls_nros[i] % mult == 0:  # es múltiplo de mult
        dc_mult[ls_nros[i]] = i     # agrega múltiplo:posición 
        cont_mult += 1              # incrementa contador de encontrados
    else:                       # no es múltiplo de mult
        pass                        # no hace nada
    if cont_mult == cant:       # ya encontró la cantidad pedida, cant_mult
        print(i)                    # último item de la lista examiando
        break                       # sale del lazo, no imprimirá examinados
    if i % 10 == 0:             # múltiplo de 10 para indicar el progreso
        print(i, end= " ")          # muuestra el avance, cantidad examinada
    else:                       # no es múltimplo de 10
        continue                    # sigue con el siguiente i 
    # otros posibles procesamientos
else:                           # terminó el lazo sin hallar los múltiplos
    print(i)                    # último item de la lista examinado 
    print("No se encontró la cantidad de múltiplos pedida:", cant)
    
print("\nMúltiplos de " + str(mult) + " y posiciones:", dc_mult)
    
