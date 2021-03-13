
from bs4 import BeautifulSoup
import json

html_doc = """<h1>
<a id="user-content-introducción-a-la-minería-de-datos" class="anchor" href="#introducci%C3%B3n-a-la-miner%C3%ADa-de-datos" aria-hidden="true"><span aria-hidden="true" class="octicon octicon-link"></span></a>Introducción a la Minería de Datos</h1>
<p><a href="https://travis-ci.org/mariosky/databook" rel="nofollow"><img src="https://camo.githubusercontent.com/bd28caf9fbc5fb6b202d22c490549fe189b3cbb81ec3a6e47a282eb3f34cb41c/68747470733a2f2f6170692e7472617669732d63692e6f72672f6d6172696f736b792f64617461626f6f6b2e7376673f6272616e63683d6d6173746572" alt="Build Status" data-canonical-src="https://api.travis-ci.org/mariosky/databook.svg?branch=master" style="max-width:100%;"></a></p>
<p>Actualmente vivimos una nueva <a href="https://es.wikipedia.org/wiki/Fiebre_del_oro" rel="nofollow">fiebre del oro</a>. Todos corremos apresurados en busca de la fortuna que nos espera en nuestros servidores (o en la nube), emocionados por los términos que acaparan los titulares: <em>Data Science</em>, <em>Big Data</em>, <em>Artificial Intelligence</em>. A diario nos llegan noticias de  <em>startups</em> o grandes empresas que han encontrado <em>oro</em> aplicando esa nueva técnica para explotar sus datos. El reciente <em>boom</em> ha despertado el interés de profesionistas y estudiantes por conocer y aplicar estas técnicas. Sin embargo, al empezar a leer sobre el tema muchos se desaniman al darse cuenta que para entenderlo a fondo deben estudiar temas de estadística, álgebra lineal, cálculo y por supuesto programación. Este libro pretende darte un panorama general del tema de minería de datos, con un énfasis en los conceptos más que en las matemáticas (pero de que se ven, se ven). Seguiremos un enfoque práctico con ejemplos y ejercicios de programación utilizando el lenguaje <a href="https://www.python.org/" rel="nofollow">python</a>. El objetivo es que al final cuentes con el conocimiento y herramientas necesarias para poder aplicar las técnicas de minería de datos y aprendizaje automático a la solución de problemas reales.</p>
<h2>
<a id="user-content-a-quién-va-dirigido" class="anchor" href="#a-qui%C3%A9n-va-dirigido" aria-hidden="true"><span aria-hidden="true" class="octicon octicon-link"></span></a>A quién va dirigido</h2>
<p>El libro va dirigido principalmente a estudiantes de ingeniería,
posgrado y desarrolladores. Se asume que ya sabes programar en algún
lenguaje, y tienes nociones de las matemáticas que vimos en la
preparatoria. En algunos casos se verán temas opcionales en los que si
requerimos los conocimientos de álgebra lineal, cálculo o estadística
pero no pasa nada si te los saltas para verlos después.</p>
<h2>
<a id="user-content-contenido" class="anchor" href="#contenido" aria-hidden="true"><span aria-hidden="true" class="octicon octicon-link"></span></a>Contenido</h2>
<h3>
<a id="user-content-minería-de-datos" class="anchor" href="#miner%C3%ADa-de-datos" aria-hidden="true"><span aria-hidden="true" class="octicon octicon-link"></span></a>Minería de Datos</h3>
<ol>
<li>Introducción
<ol>
<li><a href="txt/00.introduccion.md">Introducción</a></li>
<li><a href="txt/01.ejercicio_python.md">Ejemplo Práctico de KDD</a></li>
</ol>
</li>
<li>Los Datos
<ol>
<li><a href="txt/02.los_datos.md">Conjuntos de Datos</a></li>
<li><a href="txt/03.pandas.md">Pandas</a></li>
<li><a href="txt/04.numpy.md">NumPy</a></li>
<li><a href="txt/05.networkx.md">NetworkX</a></li>
</ol>
</li>
<li>Preprocesamiento
<ol>
<li><a href="txt/06.calidad.md">Calidad de los Datos</a></li>
<li><a href="txt/07.preprocesamiento.md">Preprocesamiento</a></li>
</ol>
</li>
<li><a href="txt/08.visualizacion.md">Visualización</a></li>
<li><a href="txt/09.classification.md">Clasificación</a></li>
<li>Evaluación de Modelos</li>
<li>Métodos <em>ensemble</em> o de conjuntos.</li>
<li>Agrupación</li>
<li>Sistemas de Recomendación</li>
</ol>
<h3>
<a id="user-content-python-para-análisis-de-datos" class="anchor" href="#python-para-an%C3%A1lisis-de-datos" aria-hidden="true"><span aria-hidden="true" class="octicon octicon-link"></span></a>Python para análisis de datos</h3>
<ol>
<li>Python para programadores</li>
<li>SciPy</li>
<li>Pandas</li>
<li>SciKit</li>
<li>TensorFlow</li>
</ol>
<h3>
<a id="user-content-para-generar-el-libro-en-formato-epub" class="anchor" href="#para-generar-el-libro-en-formato-epub" aria-hidden="true"><span aria-hidden="true" class="octicon octicon-link"></span></a>Para generar el libro en formato ePUB</h3>
<h4>
<a id="user-content-pre-requisitos" class="anchor" href="#pre-requisitos" aria-hidden="true"><span aria-hidden="true" class="octicon octicon-link"></span></a>Pre requisitos</h4>
<ol>
<li>Git <a href="https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git" rel="nofollow">Guía de Instalación</a>
</li>
<li>Pandoc <a href="https://pandoc.org/installing.html" rel="nofollow">Guía de Instalación</a>
</li>
</ol>
<h4>
<a id="user-content-generación" class="anchor" href="#generaci%C3%B3n" aria-hidden="true"><span aria-hidden="true" class="octicon octicon-link"></span></a>Generación</h4>
<pre><code>git clone https://github.com/mariosky/databook.git
</code></pre>
<pre><code>cd databook/txt 
</code></pre>
<pre><code>pandoc -o databook.epub title.txt \
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
</code></pre>
<h2>
<a id="user-content-licencia" class="anchor" href="#licencia" aria-hidden="true"><span aria-hidden="true" class="octicon octicon-link"></span></a>Licencia</h2>
<p>El contenido del libro tiene una licencia
<a href="https://creativecommons.org/licenses/by-sa/3.0/es/" rel="nofollow"><code>cc-by-sa</code></a> y el código incluido la licencia <a href="LICENSE">MIT</a>.</p>
<p><a href="https://camo.githubusercontent.com/2fe2da60e290c196786a2b2fea55035eaae397315b9bbb8de4eddc6f53a85a1e/68747470733a2f2f692e6372656174697665636f6d6d6f6e732e6f72672f6c2f62792d73612f332e302f65732f38387833312e706e67" target="_blank" rel="nofollow"><img src="https://camo.githubusercontent.com/2fe2da60e290c196786a2b2fea55035eaae397315b9bbb8de4eddc6f53a85a1e/68747470733a2f2f692e6372656174697665636f6d6d6f6e732e6f72672f6c2f62792d73612f332e302f65732f38387833312e706e67" alt="cc-by-sa" data-canonical-src="https://i.creativecommons.org/l/by-sa/3.0/es/88x31.png" style="max-width:100%;"></a></p>"""

soup = BeautifulSoup(html_doc, 'html.parser')

text = soup.get_text()
print(text)
print(type(text))

data = {'url':   'Alice',
    'title': 'Bob',
    'body':  text}

data = json.dumps(data)

print(data.encode('utf-8'))