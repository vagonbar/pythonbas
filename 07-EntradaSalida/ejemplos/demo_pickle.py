#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# demo_pickle.py: demo de persistencia de objetos con pickle

'''Muestra el uso del módulo pickle para persistencia de objetos,

Permite guardar objetos en un archivo y recuperarlos luego del archivo reconstruyendo los objetos originales.
'''

import pickle
import sys

class Persona():
    '''Clase demostrativa simple con nombre y edad.
    '''
    def __init__(self, nombre='Anónimo', edad=0):
        self.nombre = nombre
        self.edad = edad
        return
    def __str__(self):
        return '  Nombre: ' + self.nombre + '; edad: ' + str(self.edad)


def pickdump():
    '''Crea objetos y los guarda en un archivo usando pickle.
    '''
    p1 = Persona()
    p1.nombre = 'Apolonio de Rodas'
    p1.edad = 1715

    p2 = Persona('Luciano de Samosata', 1885)

    print('--- objetos creados:')
    print(p1)
    print(p2)
    
    f = open('pick_personas.pkl','bw')     # acepta bytes, para escritura
    pickle.dump(p1, f)
    pickle.dump(p2, f)
    f.close()
    return


def pickload():
    '''Recupera objetos de un archivo creado con pickle.
    '''
    f = open('pick_personas.pkl','br')
    p1 = pickle.load(f)
    p2 = pickle.load(f)
    try:
        p3 = pickle.load(f)
    except EOFError as e:
        print("p3, fin de archivo, ERROR")
        print(e)
    f.close()

    print('--- objetos recuperados:')
    print(p1)
    print(p2)


def pickver():
    '''Muestra el archivo pickle en crudo.
    '''
    with open('dmpickle.pkl', 'br') as f:
        print(f.read())
    return


def ayuda():
    '''Muestra el uso del módulo.
    '''  
    print("Uso: python demo_pickle.py { --pickdump | --pickload |" + \
        " --pickver }")
    print("  pickdump: crea objetos y los guarda en archivo pickle.")
    print("  pickload: recupera los objetos del archivo pickle.")
    print("  pickver:  muestra el archivo pickle 'en crudo'.")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        ayuda()
    elif sys.argv[1] == '--pickload':
        pickload()
    elif sys.argv[1] == '--pickdump':
        pickdump()
    elif sys.argv[1] == '--pickver':
        pickver()
    else:
        ayuda()
    
