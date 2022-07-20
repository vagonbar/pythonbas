#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# rectangulo.py : ejemplo de clase y objetos.

'''Clases y objetos: define clase Rectangulo y crea objetos.
'''

class Rectangulo:
    '''Clase para para definir objetos de tipo Rectangulo.
    '''
    def __init__(self, nom, a, b):
        '''Constructor, crea un objeto Rectangulo.
        '''
        self.nombre = nom    # nombre, para identificar cada rectángulo
        self.lado_a = a      # longitud de un lado
        self.lado_b = b      # longitud del otro lado
    def area(self):
        '''Calcula el área del rectángulo.
        '''
        return self.lado_a * self.lado_b
    def __str__(self):
        '''Devuelve una cadena para imprimir con "print".
        '''
        mens = "Rectangulo " + self.nombre
        mens += ", lado a: " + str(self.lado_a)
        mens += ", lado b: " + str(self.lado_b)
        mens += ", área: " + str(self.area())
        return mens

if __name__ == "__main__":
    r1 = Rectangulo("R-uno", 2.4, 3.6)   # crea un rectángulo
    r2 = Rectangulo("R-dos", 6, 3)       # crea otro rectángulo
    print(r1); print(r2)  # muestra ambos rectángulos




