#!/usr/bin/python3
# -*- coding: utf_8 -*-
# params_mod.py: parámetros recibidos por un módulo

'''Parámetros recibidos por un módulo.

Muestra un mensaje, nombre del módulo y lista de argumentos recibidos.
Sugerencias de invocación:

  - C{python paramsmod}
  - C{python paramsmod "uno" "dos" "tres"}
  - C{python paramsmod.py "uno" 2 2.55 True False, None}

La lista de argumentos recibidos queda en C{argv} del módulo C{sys}. 
El primer elemento de la lista, argv[0], es el nombre del módulo. 
Observar que todos los argumentos son recibidos como C{'str'}.
'''

import sys

print("=== params_mod.py, parámetros recibidos por un módulo.")
print("Muestra nombre de módulo y lista de argumentos.")

# muestra nombre del módulo
print("  Nombre módulo, sys.argv[0]:", sys.argv[0])

# muestra los argumentos pasados
print("Argumentos, sys.argv[1:]:")

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        print("  ", arg, "\t", type(arg))
else:
    print("  no se pasaron argumentos.")


