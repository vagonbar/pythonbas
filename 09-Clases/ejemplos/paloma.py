#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# paloma.py : ejemplo simple de variables de clase y de instancia


class Paloma:
    especie = "Ave"  # variable de clase, común a todos los objetos Paloma
    ave_cnt = 0      # variable de clase, contador de objetos existentes
    def __init__(self, p_nombre):  # constructor, crea objeto Paloma
        self.nombre = p_nombre     # variable de instancia
        Paloma.ave_cnt += 1        # incrementa contador de palomas
    def __del__(self):             # destructor, borra objeto Paloma
        Paloma.ave_cnt -= 1        # decrementa contador de palomas
    def mostrar(self):      # muestra especie, nombre y cantidad de objetos
        print(Paloma.especie, self.nombre, Paloma.ave_cnt)

if __name__ == "__main__":

    print("--- Crea dos objetos, muestra cantidad de objetos existentes:")
    plm_1 = Paloma("Gertrudis")
    plm_2 = Paloma("Milena")
    plm_1.mostrar()               # total 2 objetos
    plm_2.mostrar()

    print("--- Cambia variable de clase, todos ven el mismo valor:")
    Paloma.especie = "Paloma de Monte"  # cambia variable de clase
    plm_1.mostrar()                     # cambia en todos los objetos
    plm_2.mostrar()                     # cambia en todos los objetos

    print("--- Borra un objeto, actualiza contador de objetos existentes:")
    del plm_1                           # borra un objeto de 2
    plm_2.mostrar()                     # ... queda 1 

