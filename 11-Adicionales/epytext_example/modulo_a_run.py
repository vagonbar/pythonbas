#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Módulo para prueba de modulo_a.

Contiene una función para probar la ClaseA del módulo_a.
"""

from modulo_a import ClaseA

def module_a_run():
  """Función de módulo para probar el modulo_a.

  Invocar como::

    $ python3 modulo_a_run.py

  @return: devuelve 0.
  @rtype: int.
  """
  a1 = ClaseA()
  a2 = ClaseA()
  print ('Instancias creadas, contadas en la variable de clase:')
  print ('   ClaseA.cl_var1={0}, a1.cl_var1={1}, a2.cl_var1={2}'. \
    format(ClaseA.cl_var1, a1.cl_var1, a2.cl_var1 ) )

  print ('Operaciones sobre variables en objetos:')
  print ('   a1.cl_var1 += 10; a2.cl_var1 += 20')
  a1.cl_var1 += 10; a2.cl_var1 += 20
  print ('Valores modificados de variables en objetos y en clase:')
  print ('   a1.cl_var1={0}, a2.cl_var1={1}, ClaseA.cl_var1={2}'. \
     format(a1.cl_var1, a2.cl_var1, ClaseA.cl_var1) )

  print ('Variables de instancia')
  a1.in_var1 = 'objeto a1'
  print ('Objeto a1: ', a1); print ('Objeto a2: ', a2)
  print ('   a1 == a2 ?:', a1 == a2)
  a3 = ClaseA()
  print ('Objeto a3: ', a3)
  a3.in_var1 = a2.in_var1
  print ('   a3 == a2 ?:', a3 == a2)
  return 0

if __name__ == '__main__':
  module_a_run()

