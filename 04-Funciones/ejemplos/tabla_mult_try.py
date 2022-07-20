#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tablas3.py: muestra la tabla del número que se le pida, trata errores

def tabla_mult():
  '''Muestra la tabla del número que se le pida.

  Pide un número entero, muestra la tabla de multiplicar de ese número, devuelve el número ingresado.
  @return: el número pedido; indica qué valor se devuelve.
  @rtype: int; indica el tipo de valor devuelto.
  '''
  
  # el ingreso interactivo con raw_input devuelve una cadena
  snro = input('Ingrese un número (0 para terminar):')
  # convierte la cadena a entero
  # captura y trata el error si el usuario no digita un número
  try:                    # probará si no hay errores, llamados "excepciones"
    nro = int(snro)
  except ValueError:      # si se produce la excepción llamada ValueError
    print("Error: " + snro + " no es un número; intente nuevamente.")
    return snro
 
  print("Tabla del " + snro + ":")
  for i in range(0,11):    # muestra la tabla hasta el 10
    print(i, "x", snro, "=", i * nro)
  return nro

if __name__ == '__main__':
  # si el módulo fue invocado directamente su nombre es __main__
  print("=== Tablas de multiplicar ===")
  while tabla_mult() != 0:   # repite hasta que el retorno sea el 0
    pass


