#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# try_finally.py : captura exceptiones, trata en try...except exterior

'''Levanta excepciones en "try ... finally".

El bloque interno "try...finally" levanta una excepción pero no la trata, pero es capturada por un bloque "try...except" externo.

Adaptado de PEW’s Corner. Python 3 Quick Reference, 
https://pewscorner.github.io/programming/python3_quick_ref.html 
'''

import sys

# este "try" exterior captura todas las excepciones no tratadas 
#    en el "try" interior
try:
    # el "try" interior, solo con la parte "finally"
    try:
        print('--- en "try" interno, levanta una excepción con sys.exit()')
        sys.exit()
        # levanta la excepción SystemExit, pero no la trata
        print('--- esto no llega a ejecutarse nunca por la excepción')
    finally:
    # este bloque se ejecuta aunque haya habido excepción y no se trate
        print('--- en "finally" del "try" interno')
except:
    # captura la excepción SystemExit ocurrida en el "try" interno.
    # el "except" no indica tipo de excepción, captura todos los tipos;
    # "except Exception" captura solo las de tipo "Exception",
    # "SystemExit" es de tipo "BaseException", no "Exception".
    print('--- en "except" del "try" eexterior')



