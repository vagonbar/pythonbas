#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# alcance_1.py: prueba de alcance de variables

'''Alcance de variables, pruebas.

Muestra el uso de variables definidas en distintos espacios de nombres: módulo,función, u otro módulo. Muestra el uso de global para acceder variables externas. 
Los nombres de las variables indican dónde se definieron (módulo, función), y si son de módulo o globales. 
'''

import alcance_2 as mod2      # importa módulo adicional con variables de módulo

# define variables en este módulo, algunas declaradas global
m1_var1_m = "m1_var1_m"            # módulo 1, variable 1, de módulo
global m1_var2_g 
m1_var2_g = "m1_var_2g"   # módulo 1, variable 2, de módulo, global
m1_var3_m = "m1_var_3_m"          # módulo 1, variable 3, de módulo
global m_var4_m
m1_var4_g = "m1_var_4_g"   # módulo 1, variable 4, de módulo, global


def fn1():
    '''Verifica variables disponibles en la función.
    '''
    try:
        m1_var1_m += ", reasignada en fn1"
    except UnboundLocalError as e:
        print("   ", e)
    else:
        print("   ", m1_var1_m)

    try:
        m1_var2_g += ", reasignada en fn1"
    except UnboundLocalError as e:
        print("   ", e)
    else:
        print("   ", m1_var2_g)

    return


def fn2():
    '''Verifica variables disponibles en la función declarando global.
    '''
    global m1_var3_m
    global m1_var4_g
    m1_var3_m += ", global en fn2 y reasignada en fn2"
    m1_var4_g += ", global en fn2 y reasignada en fn2"
    print("   ", m1_var3_m); print("   ", m1_var4_g)
    return


def fn3():
    '''Define variables locales y globales.

    Variables locales de igual nombre a las del módulo son otras variables.
    '''
    m1_var1_m = "m1_var1_m en fn3"
    m1_var2_g = "m1_var2_g en fn3"
    print("--- variables locales en fn3 con nombre de variables de módulo")
    print("       son otras variables distintas a las del módulo:")
    print("   ", m1_var1_m); print("   ", m1_var2_g)
    # variables global definida dentro de la función
    global f3_var5_g, f3_var6_g
    f3_var5_g = "fn3.var5 global"
    f3_var6_g = "fn3.var6 global"
    print("--- variables globales definidas en fn3, dentro de fn3:")
    print("   ", f3_var5_g); print("   ", f3_var6_g)
    return
  

def fn4():
    '''Define variable local y global desde la función.
    '''
    f4_var7_l = "f4_var7_l"
    print("--- variable local en fn4")
    print("   ", f4_var7_l)
    global f4_var8_g
    f4_var8_g = "f4_var8_g"
    print("--- variable global en fn4")
    print("   ", f4_var8_g)
    return


def fn5():
    '''Muestra variables definidas en otra función.
    '''
    print("--- en fn5, intento de acceso a variable local de fn4")
    try:
        f4_var7_l += " reasignada en fn5"
    except UnboundLocalError as e:
        print("   ", e)
    else: 
        print("   ", f4_var7_l)

    print("--- en fn5, acceso a variable global definida en fn4")
    global f4_var8_g
    try:
        f4_var8_g += " reasignada en fn5"
    except UnboundLocalError as e:
        print("   ", e)
    else: 
        print("   ", f4_var8_g)


def fn6():
    '''Muestra variables definidas en otro módulo.
    '''
    #print("--- en fn6, intento de acceso a variables de otro módulo")
    print("   ", mod2.m2_var1_m)
    print("   ", mod2.m2_var2_g)




if __name__ == "__main__":

    print("=== valores originales de las variables en el módulo:")
    print("   ", m1_var1_m); print("   ", m1_var2_g)

    print("=== asignaciones en el módulo:")
    m1_var1_m += ", reasignada en módulo"
    m1_var2_g += ", reasignada en módulo"
    print("   ", m1_var1_m); print("   ", m1_var2_g)

    print("=== asignaciones en fn1:")
    print("--- variables inaccesibles dentro de la función:")
    fn1()
    print("--- valores en el módulo, no cambiaron:")
    print("   ", m1_var1_m); print("   ", m1_var2_g)

    print("=== asignaciones en función fn2 declarando global")
    print("--- valores dentro de la función, reasignadas:")
    fn2()
    print("--- valores en el módulo, cambiaron:")
    print("   ", m1_var3_m); print("   ", m1_var4_g)

    print("=== definición de variables dentro de fn3:")
    fn3()
    print("--- variables globales definidas en fn3, desde el módulo:")
    print("   ", f3_var5_g); print("   ", f3_var6_g)
    print("--- variables de módulo, distintas a las de igual nombre en fn3:")
    print("   ", m1_var1_m); print("   ", m1_var2_g)

    print("=== acceso desde función a variables definidas en otra función:")
    fn4()
    print("--- en módulo, acceso a variable global definida en fn4")
    print("   ", f4_var8_g)
    fn5()
    print("--- en módulo, variable global definida en fn4 modificada en fn5")
    print("   ", f4_var8_g)

    print("=== acceso a variables definidas en otro módulo:")
    print("--- acceso desde este módulo:")
    print("   ", mod2.m2_var1_m)
    print("   ", mod2.m2_var2_g)
    print("--- acceso desde función fn6 de este módulo:")
    fn6()

    print("\n=== mostrar variables globales y locales:")
    print("\n--- Salida de globals().keys():")
    print(globals().keys() )
    print("\n--- Salida de locals().keys():")
    print(locals().keys()  )
