=====================
Esto é unha cabeceira
=====================


Título h1
*********

Título h2
=========

Titulo h3
---------

Título h4
+++++++++


Marcado dentro de texto
+++++++++++++++++++++++
Escribimos texto en varias liñas e esto forma un paragrafo.
Lembrade que o tabulado é importante para que o entenda sphinx.
mediante *cursiva*, ou **negriña** e ``dobre comiñas para o codigo``

Lista non numeradas
+++++++++++++++++++
* Podemos facer listas.
* De distintos elementos.
* Utilizando o <*>.

Lista numeradas
+++++++++++++++
1. Outra lista numerada
2. Utilizando o número seguido do punto.
#. Seguimos numerando a lista.
#. Neste caso utilizamos #.

Cun novo paragrafo no medio comeza a numeración

#. Nova lista.

Tipo de listas
++++++++++++++

1
+

* Lista
* con elementos

  * En novas sublistas

    * Con distintos niveis

* E subir niveis

2
+

* Lista
* con elementos
    * En novas sublistas
        * Con distintos niveis
* E subir niveis

3
+

* Lista
* con elementos

    * En novas sublistas
        * Con distintos niveis
* E subir niveis

Definicións
+++++++++++

Termino
    Definición do termino.

    Pode ter varios parágrafos.

Outro termino.
    Coa súa definición

Saltos de liña
++++++++++++++

| Estas liñas se mostraran
| cos saltos de liña marcados
| de forma exacta.

Bloques de texto literales
++++++++++++++++++++++++++

1
+

O texto normal de paragrafo. O texto que se mostra a
continuación sería un bloque literal:

    import sys

    class MinhaClase:
           # Por facer

Continuamos o texto o mesmo nivel de paragrafro a continuación.

2
+

O texto normal de paragrafo. O texto que se mostra a
continuación sería un bloque literal::

    import sys

    class MinhaClase:
           # Por facer

Continuamos o texto o mesmo nivel de paragrafro a continuación.

3
+
>>> intérprete de python
hola

Taboas
++++++
1
+
+---------------------------+---------------------------+
| Cabeceira fila, columna 1 | cabeceira fila, columna 2 |
+===========================+===========================+
| Fila 1, columna 1         | Fila 1, columna 2         |
+---------------------------+---------------------------+

2
+

==========  ==========  ==========
Lista 1     Lista 2     Lista 3
==========  ==========  ==========
Elemento 1  Elemento 2  Elemento 3
Elemento 4  Elemento 5  Elemento 6
Elemento 7  Elemento 8  Elemento 9
==========  ==========  ==========

Enlaces
+++++++
.. _colea:  http://www.danielcastelao.org/

Os enlaces non é necesario marcalos http://www.danielcastelao.org salvo
que queiramos etiqueta para o enlace o `cole <http://www.danielcastelao.org/>`_

Outra forma de acceder é facendo unha definición antes é nombrarla `colea`_.

#doc en https://www.sphinx-doc.org/es/stable/rest.html


Enlace a listas numeradas `Lista non numeradas`_

Creamos una figura accediendo a una foto que hemos puesto en la carpeta static:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. figure:: _static/carta1.jpg
    :align: center

    Este é o pe da imaxe


    :download: `Baixate o ejemploSphinx1.rst` `<source/ejemploShpinx1.rst>`_

    .. note::
        Esto es una nota

    .. warning::
        Cuidado !!!

    .. versionchanged::
        0.0.1
