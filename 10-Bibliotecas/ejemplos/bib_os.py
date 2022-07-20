#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bib_os.py: biblioeca os, ejemplos

# importar el módulo, no importar todo para no chocar con funciones builtin
import os


print("=== Directorios")

print("Dir actual, absoluto:", os.getcwd())

print("Dir actual, relativo:", os.curdir)
print("Contenido del directorio actual, con curdir y con '.' :")
print("  ", os.listdir(os.curdir))  # lista contenido de directorio actual
# print(os.listdir(.))        # ERROR, sintaxis inválida
print("  ", os.listdir("."))        # toma el scring "." como directorio actual
print("  Contenido del directorio superior al actual, con '..' :")
print("  ", os.listdir(".."))       # string ".." directorio superior al actual

print("Crea directorio dir_prueba: ")
os.mkdir("dir_prueba")        # crea directorio
print( "  ¿Existe dir_prueba?", "dir_prueba" in os.listdir(os.curdir) ) 
print("Borra directorio dir_prueba: ")
os.rmdir("dir_prueba")        # borrar directorio
print( "  ¿Existe dir_prueba?", "dir_prueba" in os.listdir(os.curdir) )     
print()

print("=== Archivos")
print("Crea archivo arch_prueba.txt con open() de builtin, NO os.open()")
fp = open("arch_prueba.txt", "w")
fp.close()
print( "  ¿Existe arch_prueba?", "arch_prueba.txt" in os.listdir(os.curdir) )
print("Borra archivo arch_prueba.txt con os.remove()")
os.remove("arch_prueba.txt")
print( "  ¿Existe arch_prueba.txt?", "arch_prueba.txt" in os.listdir(os.curdir))
print()

print("=== Rutas y nombres de archivos")
fp = open("arch_prueba.txt", "w")
fp.close()
rt = os.path.abspath("arch_prueba.txt")
print("  ruta absoluta:", rt)
print("  ruta, nombre:", os.path.split(rt))
print("  directorio:", os.path.dirname(rt))
print("  nombre archivo:", os.path.basename(rt))
print("  nombre, extensión:", os.path.splitext(os.path.basename(rt)))
print("  archivo existe?", os.path.exists(rt))
print("  es archivo?", os.path.isfile(rt))
print("  es directorio?", os.path.isdir(rt))
print("  expande dir usuario '~/.local' :", os.path.expanduser("~/.local"))
print("  crea ruta:", os.path.join(os.path.expanduser('~'), 'local', 'bin'))
print("Recorrer un directorio:")
for dirpath, dirnames, filenames in os.walk(os.curdir):
    for fp in filenames:
        print(os.path.abspath(fp))



# chdir chmod chown getuid getgid kill link listdir rename setuid setgid synmlink
# sys: exit path stdin stdut stderr

