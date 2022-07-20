#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# while_mensaje.py : uso de while con y sin else


print("### while sin else: muestra mensaje 5 veces")
cont = 0
while cont < 5:
	print("Este mensaje se imprime 5 veces")
	cont += 1       # incrementa el contador

print("\n### while con else: muestra mensaje 5 veces y otro al final")
cont = 0
while cont < 5:
	print("Este mensaje se imprime 5 veces")
	cont += 1       # incrementa el contador
else:
	print("Con else : Bucle terminado")

