#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Documentación de módulo C{modulo_a} descripción breve.

La primera línea es una descripción breve del módulo, terminada en '.'. Debe dejarse una línea en blanco luego de la primera línea, para ser reconocida como descripción breve. El texto siguiente (este texto) es la descripción detallada del módulo.

Para probar este módulo::

    $ python3 modulo_a_run.py

Las líneas en blanco indican inicio de un nuevo párrafo. El indentado adicional presenta el docstring como código. Observar los dos C{ :: }.

Los docstrings reconocidos por C{pydoctor} son los de módulo, clase y función.

@var mod_var_1: una variable de módulo.
"""

mod_var_1 = 0

def fn_mod():
  """Una función de módulo.

  Descripción detallada de la función. 
  @return: una cadena de caracteres (string).
  @rtype: string.
  """
  return ("fn_mod es una función de módulo.")

class ClaseA:
  """Descripción breve de la clase ClaseA, una línea.
  
  Descripción detallada de la clase ClaseA, varias líneas.
  @cvar cl_var1: variable) de clase C{cl_var1}, asociada a la clase. Cuenta las instancias creadas de objetos de esta clase. Un atributo de clase es una variable asociada a la clase. Todos los objetos comparten esta misma variable; si un objeto la modifica, todos los objetos de esa clase ven el valor modificado.
  @ivar in_var1: atributo o variable de instancia. Documentación más detallada de la variable de instancia C{in_var1}. Una variable de instancia es propia de cada objeto; objetos distintos de la misma clase tienen atritubos de instancia diferentes.
    """

  cl_var1 = 0
  cl_var2 = 0
  """Variable) de clase C{cl_var2}, otra forma de documentar; preferible usar @cvar en el docstring del módulo. """
  
  def __init__(self):
    """Descripción breve del constructor, una línea.
    
    Descripción detallada del constructor, varias líneas.
    """
    self.in_var1 = None
    self.in_var2 = None
    """Variable de instancia, otra forma de documentar; preferible usar @ivar en el docstring del módulo.
    """
    ClaseA.cl_var1 += 1  # incrementa variable de clase al crearse un objeto

    return

    
  def __str__(self):
    """Representación de la clase con C{print}.
    """
    return 'Objeto de la clase ClaseA, cl_var1={0}, in_var1={1}'.format(self.cl_var1, self.in_var1)

    
  def __eq__(self, ob):
    """Definición de igualdad entre objetos de ClaseA.
    
    Dos objetos de ClaseA serán iguales si su valor de atributo in_var1 es igual.
    @param ob: objeto de la clase ClaseA.
    @return: boolean True o False, según los objetos sean iguales o no.
    """
    if self.in_var1 == ob.in_var1:
      return True
    else:
      return False

      
  def fn1(self, par1='el uno', par2=22):
    """Descripción breve de la función fn1.
    
    Descripción detallada de la función fn1. 
    @type par1: string, tipo de parámetro, opcional.
    @param par1: descripción del parámetro 1.
    @type par2: int, tipo de parámetro, opcional.
    @param par2: descripción del parámetro 2.
    @rtype: tipo de valor de retorno, opcional.
    @return: descripción del valor de retorno.
    """
    print("Función fn1, par1: ", par1, ", par2: ", par2)
    return


'''
if __name__ == '__main__':
  """Programa main para prueba.

  Invocar como: python3 modulo_a.py
  """
  a1 = ClaseA()
  """@var a1: instancia 1 de la ClaseA."""
  a2 = ClaseA()
  """@var a2: instancia 2 de la ClaseA."""
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
  """@var a3: instancia 3 de la ClaseA."""
  print ('Objeto a3: ', a3)
  a3.in_var1 = a2.in_var1
  print ('   a3 == a2 ?:', a3 == a2)  
'''
  

