#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# dia_semana.py : uso de if ... elif .... else

dia = input("Día de la semana: ")
if dia == "sábado":
	print(dia, ": medio horario")
elif dia == "domingo":
	print(dia, ": no laborable")
elif dia == "1 de mayo" or dia == "25 de agosto":
	print(dia, ": feriado no laborable")
elif dia in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
	print(dia, ": laborable")
else:
	print("No es un día válido:", dia)
