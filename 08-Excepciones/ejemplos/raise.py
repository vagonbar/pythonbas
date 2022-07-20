#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# raise_py : levanta excepciones de diferentes formas

'''Muestra diversas formas de levantar excepciones.

Una excepción puede volver a levantarse. La cláusula "from" en la sentencia "raise" permite indicar a partir de qué otra excepción se levanta la actual.

Adaptado de PEW’s Corner. Python 3 Quick Reference, 
https://pewscorner.github.io/programming/python3_quick_ref.html 
'''

# levanta excepciones de diferentes formas
for case in range(1, 8):
    print('Caso', case)
    try:
        try:
            if case == 1:
                raise RuntimeError  # usa la clase
            elif case >= 2:
                raise RuntimeError('primera') # usa un objeto de la clase
        except Exception as e:      # captura cualquier excepción en e
            print('--', repr(e))
            if case == 3:
                raise               # vuelve a levantar la excepción en e
            elif case == 4:
                raise RuntimeError('nueva, tratando e')
                # nueva excepción, mientras trataba excepción e
            elif case == 5:
                raise RuntimeError('nueva, de None') from None
                # nueva excepción, olvida  la excepción e
            elif case == 6:
                raise RuntimeError('nueva, ahora de e') from e 
                # nueva excepción, indica causada por la excepción e
            elif case == 7:
                raise RuntimeError('de KeyError') from KeyError('g')
                # nueva excepción, ahora causada por KeyError('g')
    except Exception as e:
            print('---', repr(e), 'con argumentos', e.args, \
                'causada por', repr(e.__cause__))


