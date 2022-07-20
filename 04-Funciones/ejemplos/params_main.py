#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# params_main.py: recibe y muestra parámetros, con __main__

'''Módulo ejecutable, muestra formas para pasar parámetros a funciones.

Este módulo tiene un método C{__main__} que permite infocarlo directamente, 
corriendo las funciones según sean invocadas dentro del método __main__ 
al final del módulo.
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

if __name__ == '__main__':
  '''Ejecuta funciones que reciben parámetros, con diferentes listas de parámetros, para mostrar la forma en que se los recibe en la función.'''

  print("\n=== Función f1")
  print("--- f1('Diego el Cigala', 'flamenco', premio='Grammy')")
  f1('Diego el Cigala', 'flamenco', premio='Grammy')
  print("--- f1('Pirulo', 'perruno')")
  f1('Pirulo', 'perruno')
  
  print("\n=== Función f2")
  print('--- f2("9")')
  f2("9")
  print('--- f2("9","cuarenta")')
  f2("9","cuarenta")
  print('--- f2("9","cuarenta","a","b")')
  f2("9","cuarenta","a","b")
  print('--- f2("9","cuarenta","a","b",par3="tres", par4="cuatro")')
  f2("9","cuarenta","a","b",par3="tres", par4="cuatro")
  print('--- f2("9","","a","b",par3="tres", par5="cinco")')
  f2("9","","a","b",par3="tres", par5="cinco")
  print('--- f2("9","",par7="siete", par8="ocho")')
  f2("9","",par7="siete", par8="ocho")
  print("--- print(f3('uno','dos','tres')")
  print("  ", f3('uno','dos','tres'))
  print("--- print(type(f3('uno','dos','tres'))")
  print("  ", type(f3('uno','dos','tres')))

