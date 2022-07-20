#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# test_paqs : prueba estructura de paqutes paqs.

'''Módulo para prueba de estructura de paquetes C{paqs}.
'''

print("=== Paquete paqs")
print("--- Módulo mod_igual")
import paqs.mod_igual as p_igual
print(p_igual.var_igual)
p_igual.fn_igual()
print()

print("=== Paquete paqs.paq_a")
print("--- Módulo_mod_igual")
import paqs.paq_a.mod_igual as pa_igual
print(pa_igual.var_igual)
pa_igual.fn_igual()
print()
print("--- Módulo_mod_a1")
import paqs.paq_a.mod_a1 as pa_a1
print(pa_a1.var_igual)
print(pa_a1.var_a1)
pa_a1.fn_a11()
pa_a1.fn_a12()
pa_a1.fn_igual()
print()
print("--- Módulo_mod_a2")
import paqs.paq_a.mod_a2 as pa_a2
print(pa_a2.var_igual)
pa_a2.fn_a21()
pa_a2.fn_a22()
pa_a2.fn_igual()
print()

print("=== Paquete paqs.paq_b")
print("--- Módulo_mod_igual")
import paqs.paq_b.mod_igual as pb_igual
print(pb_igual.var_igual)
pb_igual.fn_igual()
print()
print("--- Módulo_mod_b1")
import paqs.paq_b.mod_b1 as pb_b1
print(pb_b1.var_igual)
pb_b1.fn_b11()
pb_b1.fn_igual()
print()




