#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# params_nomain.py: recibe y muestra parámetros, sin __main__

'''Módulo para importar, muestra formas de pasar parámetros a funciones.

Este módulo no tiene método C{__main__}, por lo que debe importarse para poder invocar las funciones definidas.
'''

def f1(nombre, genero, premio='ninguno'):
  '''Función con parámetro opcional y valor por defecto.
  
  @param nombre: un nombre
  @param genero: un género musical o literario
  @param premio: el nombre de un premio
  '''
  
  print("  Nombre: " + nombre)
  print("  Género: " + str(genero))
  print("  Premio: " + premio)
  return
  
def f2(par1, par2="nada", *args, **kwargs):
  '''Función con diversos tipos de parámetros.
  
  Admite todos los tipos de parámetros posibles: obligatorios, opcionales con valor por defecto, lista de parámetros innominados, y lista de parámetros nominados en parejas clave:valor, donde clave es el nombre del parámetro. El orden es el mostrado en la definición de la función.
  @param par1: un parámetro obligatorio
  @param par2: un parámetro opcional con valor por defecto
  @param args: una lista de valores de parámetros
  @param kwargs: una lista de clave:valor pasada como parámetros nominados
  '''
  print("  parámetros recibidos:")
  print("    obligatorio, par1: " + par1)
  print("    opcional nominado, par2=nada: " + par2)
  print("    opcionales adicionales, tupla args: ", end="")
  print(args)
  print("    nominados adicionales, diccionario kwargs: ", end="")
  print(kwargs)
  return


def f3(*args):
  '''Función que retorna varios valores en una tupla.
  
  La función recibe varios argumentos y los devuelve todos en una tupla.
  @param args: la lista de argumentos.
  '''
  print("f3. Valores recibidos: ", args)
  return args 


