#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Ejemplo de documentación en Python generada con U{pydoctor <https://github.com/twisted/pydoctor/>}.

Un paquete es un directorio con un archivo C{__init__.py}, necesario para que se reconozca el directorio como un paquete de Python. Este archivo suele contener la descripción del paquete, pero también puede ser vacío. El nombre del paquete es el nombre del directorio.

Un módulo de este paquete es un archivo de extensión C{.py} colocado en este directorio.

El directorio de este paquete::

    epytext_example         # directorio del paquete, da nombre al paquete
        __init__.py         # archivo que define el paquete
        html                # directorio donde se genera la documentación
        modulo_a.py         # un módulo de este paquete
        modulo_a_run.py     # módulo con una función de prueba
        paquete_2           # un sub paquete
            __init__.py     # archivo que define el sub paquete
            modulo_b.py     # otro módulo dentro de este sub paquete

La línea anterior terminada con '::' indica que viene un bloque 'literal', a presentar tal cual. El bloque literal se escribe entre dos líneas en blanco. El código en los archivos C{*.py} muestran lo esencial para generar documentación con C{pydoctor}.

Para generar la documentación con pydoctor se requiere:

    1. instalar pydoctor.

    2. escribir la documentación en el código tal como se muestra en este ejemplo.

    3. generar las páginas HTML.

Las páginas HTML se pueden crear con un comando similar al siguiente, invocado desde el directorio inmediato superior a C{epytext_example}::
    
    $ pydoctor --make-html --html-output=epytext_example/html --add-package=epytext_example --project-name="Ejemplo pydoctor"

El lenguaje de marcado usado en pydoctor por defecto es Epytext, simple y expresivo; reStructuredText, usado por Sphinx, es más complejo y veboso. Epytext respeta la convención de documentación de Python (Python docstrings), que puede visualizarse en Python con el comando C{help}:

    >>> import epytext_example
    >>> help(epytext_example)
    >>> from epytext_example import modulo_a
    >>> help(modulo_a)
    >>> help(modulo_a.ClaseA) 

Usar el formato de este ejemplo produce un Epytext válido para generar la documentación en HTML.

B{Lecturas recomendadas:}

    - The Epytext Markup Language, manual U{http://epydoc.sourceforge.net/manual-epytext.  html}

B{Referencias:}

    - pydoctor en Github: U{https://github.com/twisted/pydoctor}

    - U{Epydoc, Python Docstrings<http://epydoc.sourceforge.net/manual-docstring.html>}

    - U{Epydoc, The Epytext Markup Language<http://epydoc.sourceforge.net/manual-epytext.html>}

    - U{Epydoc Fields<http://epydoc.sourceforge.net/manual-fields.html>} 

"""



