# Introducción a la Minería de Datos

[![Build Status](https://api.travis-ci.org/mariosky/databook.svg?branch=master)](https://travis-ci.org/mariosky/databook)

Actualmente vivimos una nueva [fiebre del oro](https://es.wikipedia.org/wiki/Fiebre_del_oro). Todos corremos apresurados en busca de la fortuna que nos espera en nuestros servidores (o en la nube), emocionados por los términos que acaparan los titulares: *Data Science*, *Big Data*, *Artificial Intelligence*. A diario nos llegan noticias de  *startups* o grandes empresas que han encontrado *oro* aplicando esa nueva técnica para explotar sus datos. El reciente *boom* ha despertado el interés de profesionistas y estudiantes por conocer y aplicar estas técnicas. Sin embargo, al empezar a leer sobre el tema muchos se desaniman al darse cuenta que para entenderlo a fondo deben estudiar temas de estadística, álgebra lineal, cálculo y por supuesto programación. Este libro pretende darte un panorama general del tema de minería de datos, con un énfasis en los conceptos más que en las matemáticas (pero de que se ven, se ven). Seguiremos un enfoque práctico con ejemplos y ejercicios de programación utilizando el lenguaje [python](https://www.python.org/). El objetivo es que al final cuentes con el conocimiento y herramientas necesarias para poder aplicar las técnicas de minería de datos y aprendizaje automático a la solución de problemas reales.

## A quién va dirigido

El libro va dirigido principalmente a estudiantes de ingeniería,
posgrado y desarrolladores. Se asume que ya sabes programar en algún
lenguaje, y tienes nociones de las matemáticas que vimos en la
preparatoria. En algunos casos se verán temas opcionales en los que si
requerimos los conocimientos de álgebra lineal, cálculo o estadística
pero no pasa nada si te los saltas para verlos después.


## Contenido

1. Introducción
    1. [Introducción](txt/00.introduccion.md)
    2. [Ejemplo Práctico de KDD](txt/01.ejercicio_python.md)  
2. Los Datos
    1. [Conjuntos de Datos](txt/02.los_datos.md)
    2. [Pandas](txt/03.pandas.md)
    3. [NumPy](txt/04.numpy.md)
    4. [NetworkX](txt/05.networkx.md)
3. Preprocesamiento
    1. [Calidad de los Datos](txt/06.calidad.md)
    2. [Preprocesamiento](txt/07.preprocesamiento.md)
4. [Visualización](txt/08.visualizacion.md)
5. [Clasificación](txt/09.classification.md)
6. Evaluación de Modelos
7. Métodos *ensemble* o de conjuntos.
8. Agrupación
9. Sistemas de Recomendación

### Python para análisis de datos
1. Python para programadores
2. SciPy
3. Pandas
4. SciKit
5. TensorFlow

### Para generar el libro en formato ePUB 
#### Pre requisitos
1. Git [Guía de Instalación](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git)
2. Pandoc [Guía de Instalación](https://pandoc.org/installing.html)

#### Generación
```
git clone https://github.com/mariosky/databook.git
```
```
cd databook/txt 
```
```
pandoc -o databook.epub title.txt \
00.00.md \
00.01.md \
00.introduccion.md \
01.ejercicio_python.md \
02.los_datos.md \
06.calidad.md \
07.preprocesamiento.md \
03.pandas.md \
04.numpy.md \
08.visualizacion.md \
13.inferenciaFuzzy.md \
09.classification.md \
10.tecnicasdeclasificacion.md \
11.asoc.md \
12.clusters.md \
00.02.md \
99.bibliografia.md --webtex --bibliography databook.bib --toc
```

## Licencia
El contenido del libro tiene una licencia
[`cc-by-sa`](https://creativecommons.org/licenses/by-sa/3.0/es/) y el código incluido la licencia [MIT](LICENSE).  

![cc-by-sa](https://i.creativecommons.org/l/by-sa/3.0/es/88x31.png)
