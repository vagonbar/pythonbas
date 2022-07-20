#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# try_except.py : detección y tratamiento de excepciones

'''Detección y tratamiento de excepciones.

Define una lista de expresiones, recorre la lista evaluando cada una, levanta una excepción según el ressultado; incluye cláusulas opcionales "else" y "finally", emite mensajes para mostrar el flujo de ejecución. 

Adaptado de PEW’s Corner. Python 3 Quick Reference, 
https://pewscorner.github.io/programming/python3_quick_ref.html 
'''

import sys

lst_expr = (
    '1/0',          # división por 0
    '[][1]',        # índice más allá de límite de la lista, aquí vacía
    '{}[2]',        # clave inválida en un diccionario, aquí vacío
    '(3).a',        # atributo 'a' inexistente en el tipo entero
    ')',            # error de sintaxis, paréntesis sin pareja 
    'sys.exit(5)',  # salida del sistema, termina la ejecución 
    '6'             # número entero, no levanta excepción
    )
print("Lista de expresiones a evaluar:")
print(lst_expr)
print()

# recorre una lista de expresiones, fija cada una en la variable "expr"
for expr in lst_expr:
    print('Comprobando la expresión :', expr)

    # prueba todas las cĺáusulas: "except", "else", "finally"
    try:
        eval(expr)
        # evalua la expresión, eventualmente levantando excepciones
        # continúa en este bloque si no hubo excepciones
        print('      -- no hubo excepciones')
    except ZeroDivisionError:   # no guarda la excepción
        # sigue aquí si hubo excepción ZeroDivisionError en el bloque "try"
        print('      -- división por 0')
    except (IndexError, KeyError, AttributeError) as e:
        # sigue aquí si en el bloque "try" de dio alguna de esas excepciones
        # retiene la excepción en la variable "e"
        print('      -- ', repr(e))
    except Exception as e:
        # sigue aquí con cualquier excepción de clase Exception 
        # no tratada antes
        print('      -- captura excepción genérica de tipo "Exception":')
        print('        ', repr(e))
        print('         -- "continue" salta el resto del "for"')  
        continue
        # saltea el resto del "for" después de ejecutar "finally",
        #     continúa con el siguiente item en la lista del "for"
    except SystemExit as e:
        # sique aquí con la excepción SystemExit, 
        #    que es subclase de BaseException, no de Exception
        print('      -- excepción de salida, subclase de "BaseException"')
        print('      -- ', repr(e))
    else:
        # opcional, sigue aquí si no hubo excepciones en "try",
        #    es lo mismo que agregar código al final del "try",
        #    pero si aparecen excepciones aquí no se tratan
        print('      -- "else", no hubo excepciones en try, todo OK')
        print('         -- "break" sale del "for"')  
        break
        # sale del for después de ejecutar "finally",
        #     no continúa trata los restantes items en la lista del "for"
    finally:
        # opcional; se ejecuta aún si hubo excepciones no tratadas o
		# sentencias return/break/continue en las partes try/except/else
        print('      -- "finally", ejecuta el bloque final')
    print('   -- ejecuta el resto del bloque repetitivo "for"')



