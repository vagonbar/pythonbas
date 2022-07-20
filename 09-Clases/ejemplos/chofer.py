#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# chofer.py: ejemplo simple de herencia múltiple

'''Crea clases Persona y Licencia, clase Chofer hereda de ambas.

La clase Chofer invoca los constructores de las dos superclases.
El método __str__ de Chofer invoca los métodos __str__ de las superclases.
'''

class Persona():
    def __init__(self, nombre):
        self.nombre = nombre
        return
    def __str__(self):
        return self.nombre

class Licencia():
    def __init__(self, lic_tipo, lic_nro):
        self.lic_tipo = lic_tipo
        self.lic_nro = lic_nro
        return
    def __str__(self):
        return "Licencia tipo: " + self.lic_tipo + ", No. " + self.lic_nro

class Chofer(Persona, Licencia):
    def __init__(self, nombre, lic_tipo, lic_nro):
        Persona.__init__(self, nombre)
        Licencia.__init__(self, lic_tipo, lic_nro)
        return
    def __str__(self):
        return Persona.__str__(self) + ", " + Licencia.__str__(self)

if __name__ == "__main__":
    p1 = Persona("Isabel")
    print(p1)
    
    ch2 = Chofer("Braulio", "Conducir Amateur", "1234")
    ch3 = Chofer("Bárbara", "Conducir Profesional", "5678")
    print(ch2)
    print(ch3)
    
    print(p1.nombre, "es Persona?", isinstance(p1, Persona))
    print(p1.nombre, "tiene Licencia?", isinstance(p1, Licencia))
    
    print(ch2.nombre, "es Persona?", isinstance(ch2, Persona))
    print(ch2.nombre, "es Chofer?", isinstance(ch2, Chofer))
    print(ch2.nombre, "tiene Licencia?", isinstance(ch2, Licencia))

    print("Chofer es Persona?", issubclass(Chofer, Persona))
    print("Chofer tiene Licencia?", issubclass(Chofer, Licencia))
    
