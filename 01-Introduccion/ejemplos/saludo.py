#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# saludo.py : primer módulo en Python, saludo.
#
# comentario de una línea; lo que viene después de # no se ejecuta.

'''El siguiente código define algunas funciones de ejemplo.

Este es un comentario de varias líneas; se llama "docstring".
'''

def personal():
    '''Pregunta nombre y saluda.

    Este docstring dice lo que hace la función.
    '''
    nombre = input("¿Cómo te llamas? ")       # asignación a una variable
    print("Hola", nombre, "; bienvenido a Python.")  # uso de la variable
    return

def al_mundo():
    '''Saluda a todo el mundo.
    '''
    print("Hola Mundo")
    return

def contar(n):
    '''Imprime números de 0 a n-1. 

    @param n: un entero, hasta dónde contar.
    '''
    for i in range(0,n):     # la variable i recorre de 0 a n-1
        print(i, end=" ")    # imprime el número sin cambiar de línea
    return
    
if __name__ == "__main__":    
    al_mundo()          # ejecuta esta función
    nro_hasta = 10      # asigna 10 a la variable nro_hasta
    contar(nro_hasta)   # invoca la función con nro_hasta como parámetro
