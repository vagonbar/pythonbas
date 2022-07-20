#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# list_demo.py: demuestra métodos de list


print("=== Listas, demostración de métodos\n")
letras = ["h", "g", "c", "d", "c", "b", "f", "g"]  # define lista
print("letras", letras)
print()

print("-- append(x), agrega A al final")
letras.append("A")         # agrega "A" al final
print("letras:", letras)
print()

print("-- extend(lista), agrega otra lista al final")
ls_otras = ["W", "X", "Y"] # define otra lista
letras.extend(ls_otras)    # agrega la lista ls_otras al final
print ("ls_otras:", ls_otras)
print("letras", letras)
print()

print("-- insert(i, x), agrega M en lugar 3 de ls_otras")
ls_otras.insert(2, "M")    # inserta "M" con índice 2, lugar 3
print("ls_otras:", ls_otras)
print("-- insert, A al principio, Z al final")
ls_otras.insert(0,"A")     # inserta "A" al principio, índice 0
ls_otras.insert(len(ls_otras), "Z") # inserta "Z" al final
print("ls_otras", ls_otras)
print()

print("-- remove(x), quitar elemento de valor X en letras")
letras.remove("X")         # quita elemento de valor "X", si está
print("letras:", letras)
print("-- remove, quitar elemento de valor X que no está")
try:
    letras.remove("X")     # devuelve ValueError si no está
except ValueError:
    print("   ValueError: X no está en la lista:")
print("letras:", letras)
print()

print("-- pop(): quita y devuelve último elemento de la lista")
pop_ult = letras.pop()     # quita y devuelve último valor de la lista
print(pop_ult, " ; ", letras)
print("-- pop(3): quita y devuelve elemnto en lugar 4, índice 3")
pop_3 = letras.pop(3)      # quita y devuelve elemento de índice 3, lugar 4
print(pop_3, " ; ", letras)
print("-- pop(0): quita y devuelve primer elemento, índice 0")
pop_0 = letras.pop(0)      # quita y devuelve primer elemento, índice 0
print(pop_0, " ; ", letras)
print()

print("-- index( x [, ini [,fin]] ): devuelve elemento valor X")
i = letras.index("b")      # índice de elemento de valor "b"
print("'b' en lugar", i, "letras[" + str(i) + "] =", letras[i])
try:
    j = letras.index("b", 5, 7)  # índice de "b" entre 5 y 7
                                 # ValueError si no está
except ValueError:
    print("'b' no está en letras.index('b', 5, 7), entre índices 5 y 7")
i = letras.index("A", 5, 7) # devuelve índice si está entre 5 y 7
print("'A' en lugar", i, "letras[" + str(i) + "] =", letras[i])
print()

print("-- count(x) : cantidad de veces que aparece x en la lista")
cnt_c = letras.count("c")  # cantidad de veces que aparece "c"
cnt_X = letras.count("X")  # 0 si "X" no está
print("c está", cnt_c, "veces; X está", cnt_X, "veces")
print()

print("-- sort : ordena la lista en sitio")
print("letras", letras)
letras.sort()              # ordena la lista en sitio
print("letras", letras)
print()

print("-- reverse : invierte el orden en sitio")
letras.reverse()           # invierte el orden en sitio
print("letras", letras)
print()

print("--- clear: borra eleemntos de lista ls_otras")
ls_otras.clear()           # borra elementos, deja la lista vacía
print("ls_otras:", ls_otras)
print("... del letras[:]: igual, borra elementos de lista letras")
del letras[:]              # lo mismo con notación de rebanadas ("slices")
print("letras:", letras)
print()



