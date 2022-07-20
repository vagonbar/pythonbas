#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# list_comp.py: comprensión de listas

print("=== Listas, comprensión\n")

ls = ['z', 'q', 'p', 'd', 'c', 'c', 'a']
print("Lista:", ls)
print()

print("comprensión simple con for:")
ls3 = [x+x+x for x in ls]    # concatena 3 veces cada elemento
print("  ", ls3)
print()

print("comprensión con for e if con condición or:")
ls3az = [x+x+x for x in ls if x == 'z' or x == 'a']  # idem, solo para 'a' o 'z'
print("   ", ls3az)
print()

print("creación de lista de listas de dos elementos:")
lsls = [ [x, x+x] for x in ls if x == 'z' or x == 'a']  # lista de listas
print("   ", lsls)
print()

print("apareo de listas:")
lsn = [11, 22, 33]
print("   lsn:", lsn)
lsap = [ x+str(y) for y in lsn for x in ls ]  # todas las combinaciones
print("   lsap:", lsap)
print("   len(ls), len(lsn), len(lsap):", len(ls), len(lsn), len(lsap))
print()

lsap = [ x+str(y) for y in lsn for x in ls[:3] ]  # 3 x 3 = 9
print("   lsap:", lsap)
print("   len(lsap):", len(lsap))
print()

lsap = [ ls[i] + str(lsn[i]) for i in range(0, len(lsn)) ]  # solo 3 items
print("   lsap:", lsap)
print()

print("=== Matrices.")
print("Creacíón de matríz 3*3 con for")
mat = []
for i in range(0, 9, 3):
    fil = []
    for j in range(0, 3):
        fil += [i + j]
    mat += [fil]
print("   mat :", mat)


print("Creación de matriz 3*3 con comprensión de listas")
mat = []
mat = [ [i+j for i in range(0,3)] for j in range(0, 9, 3) ]
print("   mat :", mat)

print("Creación de matriz n*n con comprensión de listas, n=5")
n = 5
mat = []
mat = [ [i+j for i in range(0,n)] for j in range(0, n*n, n) ]
print("   n :", n, " ; mat :", mat)
print()
