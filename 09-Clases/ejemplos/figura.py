#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# rectangulo.py : ejemplo de clases y objetos con herencia.

class Figura():                     # clase superior
    nom_fig = "Figura"              # variable de clase Figura
    fig_cnt = 0                     # variable de clase, cuenta instancias
    def __init__(self, id_fig):     # constructor de Figura
        self.id_fig = id_fig        # identificador, atributo de instancia
        Figura.fig_cnt += 1         # incrementa variable de clase
        print("   [ejecuta constructor en Figura]")
    def __del__(self):              # destructor de Figura
        Figura.fig_cnt -= 1         # decrementa variable de clase
        print("   [ejecuta destructor en Figura]")
    def area():                     # método a sobreescribir en subclase
        return 0
    def __str__(self):              # devuelve cadena para imprimir Figura
        return "Figura " + self.id_fig + ", cantidad: " + str(Figura.fig_cnt)
    
class Triangulo(Figura):              # subclase de Figura
    nom_fig = "Triángulo"             # variable de clase Triangulo
    def __init__(self, id_fig, b, h): # constructor de Triangulo
        super().__init__(id_fig)      # constructor de clase superior
        self.base = b
        self.altura = h
        print("     [ejecuta constructor en Triangulo]")
    def __del__(self):                # destructor de Triangulo
        super().__del__()             # destructor de clase superior Figura
        print("     [ejecuta destructor en Triangulo]")
    def area(self):                   # sobreescribe método de Figura
        return self.base * self.altura / 2
    def __str__(self):                # cadena para imprimir Triangulo
        mens = super().__str__()      # invoca método de la clase superior
        mens += " - " + self.nom_fig + ", área = " + str(self.area())
        return mens                   # devuelve cadena de caracteres
    
class Rectangulo(Figura):             # subclase de Figura
    nom_fig = "Rectángulo"            # variable de clase Rectangulo
    def __init__(self, id_fig, a, b): # constructor de Rectangulo
        super().__init__(id_fig)      # constructor de clase superior
        self.lado_a = a
        self.lado_b = b
        print("     [ejecuta constructor en Rectangulo]")
    def __del__(self):                # destructor de Rectangulo
        super().__del__()             # destructor de clase superior Figura
        print("     [ejecuta destructor en Rectangulo]")
    def area(self):                   # sobreescribe método de Figura
        return self.lado_a * self.lado_b
    def __str__(self):                # cadena para imprimir Rectangulo
        mens = super().__str__()      # invoca método de la clase superior
        mens += " - " + self.nom_fig + ", área = " + str(self.area())
        return mens                   # devuelve cadena de caracteres

if __name__ == "__main__":

    print("=== Construcción de objetos, muestra cantidad")
    r1 = Rectangulo("RR-1", 1, 2)
    r2 = Rectangulo("RR-2", 5, 4)
    t1 = Triangulo("TR-1", 5, 4)
    for fig in [r1, r2, t1]:
        print(fig)
    print("Cantidad de figuras:", Figura.fig_cnt)
    print()

    print("=== Verifica sobreescritura de variables de clase")
    print("r1.nom_fig:", r1.nom_fig, ", t1.nom_fig:", t1.nom_fig)
    print("Figura.nom_fig:", Figura.nom_fig)
    print("    Triangulo.nom_fig:", Triangulo.nom_fig, \
        ", Rectangulo.nom_fig:", Rectangulo.nom_fig)
    print()


    print("=== Destrucción de objetos, muestra cantidad")
    del r1                            # borra r1, ejecuta __del__ de Rectangulo
    print("Borrada r1; cantidad de figuras:", Figura.fig_cnt)
    print()

    print("=== Jerarquía de clases")
    print("Rectangulo es Figura:", issubclass(Rectangulo, Figura))
    print("Triangulo es Figura:", issubclass(Triangulo, Figura))
    print("Triangulo es Rectangulo:", issubclass(Triangulo, Rectangulo))
    print("Rectangulo es Triangulo:", issubclass(Rectangulo, Triangulo))
    print("r2 es Rectangulo:", isinstance(r2, Rectangulo))
    print("r2 es Figura:", isinstance(r2, Figura))
    print("t1 es Triangulo:", isinstance(t1, Triangulo))
    print("t1 es Figura:", isinstance(t1, Figura))
    print("r2 es Triangulo:", isinstance(r2, Triangulo))
    print("t1 es Rectangulo:", isinstance(t1, Rectangulo))
    print()

    print("=== Finaliza el programa, el intérprete ejecuta destructores")


