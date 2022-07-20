#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# alcance.py: muestra la definición de variables globales y locales

'''Módulo para mostrar el alcance de variables.

Intenta modificar variables de módulo dentro de una función; muestra uso de C{global}.
'''

# variables de módulo
mi_nombre = "Antonio"
'''Variable de módulo, string.'''
mi_lista = [1, 2, 3]
'''Variable de módulo, lista.'''
mi_nro = 13
'''Variable de módulo, número entero.'''


def fn_mod(par_1, ls_1):  # parámetros: una variable y una lista
    '''Muestra modificación de variables globales.

    @param par_1: un parámetro inmutable, string o número.
    @param ls_1: un parámetro lista.
    @return: par_1 y ls_1 modificados localmente.
    '''
    global mi_nro     # declara mi_nro como global
    print("=== fn_mod")
    print("  Recibidos, par_1:", par_1, "; ls_1:", ls_1, "; mi_nro:", mi_nro)
    mi_nro = mi_nro * 3     # modifica variable global
    par_1 = "Santiago"     # cambia el valor de la variable
    ls_1 += [33]              # agrega un elemento a la lista
    print("  Modificados, par_1:", par_1, "; ls_1:", ls_1, \
        "; mi_nro:", mi_nro)
    print()
    return par_1, ls_1        # devuelve variable y lista


if __name__ == "__main__":
    '''Prueba la modificación de variables de módulo en una función.
    '''
    print("=== En módulo, inicialización")
    print("  Valores iniciales")
    print("    mi_nombre:", mi_nombre, "; mi_lista:", mi_lista, \
        "; mi_nro", mi_nro)
    print()

    res_1, res_2 = fn_mod(mi_nombre, mi_lista)
    print("=== En módulo, después de fn_mod")
    print("  retornos de fn_mod:", res_1, res_2)
    print("  valores en módulo:")
    print("    mi_nombre:", mi_nombre, "; mi_lista:", mi_lista, \
        "; mi_nro", mi_nro)



