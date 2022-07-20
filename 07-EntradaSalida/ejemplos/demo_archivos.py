#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# demo_archivos.py: demo de manejo de archivos

'''Muestra manejo de archivos en Python: 
        - abrir y cerrar archivos,
        - leer, escribir y agregar en archivos,
        - recorrer archivos.
'''

import sys




def f_leer():
    '''Abrir, leer y cerrar archivos; sentencias open, close, read.
    '''
    print('=== f_leer: abre, lee y cierra un archivo.')
    print('--- abre el archivo "lineas.txt" y muestra su tipo:')
    f = open('lineas.txt','r')
    print('  type(f): ' + str(type(f)))
    print('--- lee todo el archivo y lo muestra, f.read():')
    print(f.read())
    print('--- vuelve a leer, no obtiene nada, es fin de achivo, f.read():')
    print(f.read())
    print('--- cierra e intenta leer archivo cerrado, levanta excepción:')
    f.close()
    try:
        f.read()
    except Exception as e:
        print("  fracasa intento de leer un archivo cerrado, error:")
        print("  ", e)
    print()
    return


def f_lineas():
    '''Leer un archivo por líneas.
    '''
    print('=== f_lineas: lee un archivo por líneas')
    print('--- lee todas las líneas juntas, f.readlines()')
    f = open('lineas.txt','r')
    for ln in f.readlines():
        print("  ", ln, end="")
    f.close()
    print('--- lee línea a línea recorriendo el archivo con for')
    f = open('lineas.txt','r')
    for ln in f:
        print("  ", ln, end="")
    f.close()
    print('--- lee línea a línea, con readline()')
    f = open('lineas.txt','r')
    ln = f.readline()
    while ln:
        print("  ", ln, end="")
        ln = f.readline()
    f.close()
    print('--- lee líneas con with y readlines(), cierra solo')
    with open('lineas.txt','r') as f:
        print(f.readlines())
    print('--- verifica que el archivo quedó cerrado')
    print('  f.closed:', f.closed)
    print()
    return


def f_posicion():
    '''Control de posición en el archivo.
    '''
    print('=== f_posicion: control de posición en el archivo.')
    print('--- muestra archivo cars101.txt con caracteres de posición:')
    with open("cars101.txt", "r") as f:
        print(f.read())
    print('--- abre el archivo cars101.txt')
    f = open('cars101.txt','r') 
    print('--- lee 10 caracteres, avanza a 30, lee otros 10')
    print('  cars: "' + f.read(10) + '" ; pos: '+ str(f.tell()))
    f.seek(30)
    print('  cars: "' + f.read(10) + '" ; pos: '+ str(f.tell()))
    print('--> vuelve el archivo a posición 0, lee 10 caracteres')
    f.seek(0)
    print('  cars: "' + f.read(10) + '" ; pos: '+ str(f.tell()))
    print('--> mueve más allá de fin de archivo, intenta leer')
    f.seek(2000)
    print('  cars: "' + f.read(10) + '" ; pos: '+ str(f.tell()))
    print('--> largo del archivo, con f.seek(0, 2):')
    f.seek(0, 2)
    print('  ', f.tell())
    print('--> últimos 20 caracteres, no muestra \\n final')
    fin = f.seek(0, 2)    # posición final del archivo
    print('  pos final: '+ str(f.tell()))
    f.seek(fin - 20)       # últimos 20 caracteres
    print('  pos: '+ str(f.tell())  )
    print('  cars: "' + f.read(20)[:-1] + '" ; pos: '+ str(f.tell()) )    
    f.close()
    print()


def f_escribir():
    '''Escritura de archivos.
    '''
    print('=== f_escribir: escribir en archivo.')
    print('--- abre archivo para escritura, escribe cadenas')
    f = open('escribe.txt','w')
    for i in range(0,3):
        f.write('línea ' + str(i))
    print('--- cierra archivo, abre para lectura y muestra')
    f.close()
    f = open('escribe.txt','r')
    print(f.readlines())
    f.close()
    print('--- repite escritura. ahora con \\n al fin de línea')
    f = open('escribe.txt','w')
    for i in range(0,3):
        f.write('nueva línea ' + str(i) + '\n')
    f.close()
    with open('escribe.txt','r') as f:
        print(f.read())
    print('--> abre archivo para agregar, agrega y muestra')
    f = open('escribe.txt','a')
    for i in range(3,5):
        f.write('línea agregada ' + str(i) + '\n')
    f.close()
    with open('escribe.txt','r') as f:
        print(f.read()  )
    return


def f_todas():
    '''Corre todas las funciones.
    '''
    for op in lsops[:-1]:   # [-1] para no volver a ejecutar f_todas
        print("### Acción: ", op[0], "\n")
        op[1]()
    return 

def f_ayuda():
    '''Muestra opciones de menú para invocación del módulo.
    '''
    print("Uso: dmarchivos <número> :")
    for i in range(0,len(lsops)):
        print("  ", i+1, lsops[i][0])
    return


# tuplas para presentar menú y controlar ejecución
global lsops
lsops = [ \
    ('Abrir, leer y cerrar archivo', f_leer), \
    ('Leer todas las líneas',f_lineas), \
    ('Control de posición en el archivo',f_posicion), \
    ('Escritura de archivos',f_escribir), \
    ('Ejecutar todas las funciones', f_todas) ]


if __name__ == "__main__":

    if len(sys.argv) <= 1:    # no hay argumentos
        f_ayuda()
    else:
        print("### Demo de manejo de archivos en Python ###")
        try:
            op = lsops[int(sys.argv[1]) - 1]
            print("### Acción: ", op[0], "\n")
            op[1]()
        except:
            fn_ayuda()
        finally:
            sys.exit()
    
    



