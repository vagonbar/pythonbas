#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# for_estaciones.py : uso de for con y sin else

print("### for sin else : muestra estaciones del año")
estaciones = ["primavera", "verano", "otoño", "invierno"]
for estacion in estaciones:
	print(estacion)

print("\n### for con else : muestra estaciones del año y mensaje final")
estaciones = ["primavera", "verano", "otoño", "invierno"]
for estacion in estaciones:
	print(estacion)
else:
	print("Con else : Estas son todas las estaciones")


