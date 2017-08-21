## Introducción
Cuando visitamos al médico, confiamos que el ha adquirido un amplio **conocimiento** por medio de interactuar con su entorno y su capacidad de procesar la información que lo rodea. Utilizando este conocimiento él es capaz de darnos un diagnóstico acertado. Si en lugar de asistir con un humano eligiéramos visitar a un robot-médico, más vale que cuente con una buena inteligencia artificial. Según Rusell y Norvig el término inteligencia artificial se aplica cuando una máquina imita las funciones cognitivas que los humanos asocian con otras mentes humanas, como por ejemplo: *aprender* y *resolver problemas* [ref]. Precisamente, una de las primeras aplicaciones de la inteligencia artificial han sido los Sistemas Expertos, los cuales pueden emular la toma de decisiones de un humano experto, por ejemplo a un médico. Un exponente importante de este tipo de sistemas fue  [Mycin](https://es.wikipedia.org/wiki/Mycin) el cual se basaba principalmente en un sencillo motor de inferencia, que manejaba una base de conocimiento de aproximadamente unas 500 reglas. Estas reglas [representaban el conocimiento](https://es.wikipedia.org/wiki/Representaci%C3%B3n_del_conocimiento) de los médicos. Una desventaja de este tipo de sistemas era que se requería de mucho esfuerzo y recursos para extraer el conocimiento de los expertos. Se debía entrevistarlos utilizando técnicas de *elicitación del conocimiento* para después representar dicho conocimiento de alguna manera para después   almacenarlo en una *base de conocimiento*. Digamos que se realizaba una extracción manual del conocimiento a partir de las ideas de los expertos. Cualquier desarrollador que ha tenido que extraer los requerimientos de un usuario te dirá que fue una tarea cercana a lo imposible. No es descabellado preguntarnos entonces: ¿el conocimiento "humano" podrá ser extraído  de otras fuentes?, ¿y si contamos con una base de datos de miles de diagnósticos realizados anteriormente?, ¿podremos extraer de esta base de datos un nuevo conocimiento?. Este es el tipo de preguntas son las que se trata de contestar el área de investigación en inteligencia artificial, pero como veremos más adelante, en la búsqueda de respuestas se involucran muchas otras áreas de investigación.

### Descubrimiento de conocimiento en bases de datos (KDD)
Al proceso de extraer conocimiento útil a partir de datos se le denomina *Descubrimiento de Conocimiento en Bases de Datos* o *KDD* ya que es muy común utilizar las siglas del inglés de "Knowledge Discovery from Databases". Este proceso puede hacerse manualmente, expertos en algún dominio pueden consultar y analizar bases de datos para descubrir patrones que les ayuden a tomar decisiones. Por ejemplo, en la película "The BigShort" podemos ver al inversionista Michael Burry analizando grandes cantidades de datos, para después predecir el eminente desplome de la burbuja inmobiliaria. Como podemos imaginar, este proceso no es trivial, no es simplemente hacer una consulta en una base de datos o en una motor de búsqueda. El KDD sigue evolucionando involucrando cada vez más áreas de investigación: aprendizaje automático, reconocimiento de patrones, computación inteligente, estadística, procesamiento de lenguaje natural, visualización, ingeniería de software entre otras.

La Minería de Datos de hecho es uno de los componentes del proceso KDD.
Veamos el proceso del KDD, según el esquema de Brachman y Anand:

![El procesos del KDD según Brachman y Anand](../img/Proceso-KDD.png)

1. Como primer paso debemos *identificar el objetivo* del proceso de KDD. Por ejemplo, un proveedor de telefonía móvil podría estar interesado en identificar a aquellos clientes que ya no renovarán su contrato y se irán con la competencia. A esto se le llama la tasa de cancelación de clientes (en inglés [churn rate](https://en.wikipedia.org/wiki/Churn_rate) o attrition rate) y es crucial para estimar el desempeño de la empresa.

2. El siguiente paso es *seleccionar y recolectar* aquellos datos necesarios para el proceso. Para nuestro ejemplo, podríamos requerir el historial de pago de los clientes, datos sobre quejas y llamadas que han hecho a soporte, servicios adicionales que se han contratado o cancelado, etc. Esta información puede estar distribuida en diferentes bases de datos. También se puede incluir información que se colecte por medio de sensores o sistemas externos, por ejemplo lecturas del GPS, caídas de la conexión o el número de aplicaciones que el cliente se ha instalado.

3. Es necesario *preprocesar* los datos para limpiarlos de datos erróneos, datos faltantes, cambios de formato, inconsistencias, etc. Esto proceso complicado y depende bastante de los requerimientos de la empresa.

4. Dependiendo de los objetivos se deben *transformar* los datos para simplificar su procesamiento. Por ejemplo un documento de texto es necesario transformarlo en vector representativo. Una imagen puede ser transformada en una representación simplificada pero conservando sus características esenciales. Muchas veces también es necesario eliminar campos que no aportan mucho a la tarea de KDD. Siguiendo nuestro ejemplo, después de un análisis podríamos darnos cuenta que el número de teléfono en sí no es un dato importante para distinguir el comportamiento de los clientes, y que al contrario la marca y modelo de sus móviles son muy importantes.

5. Este paso consiste en *seleccionar la tarea de minería de datos* adecuado de acuerdo con la meta establecida para el proceso de KDD. Por ejemplo, clasificación, regresión, agrupamiento, etc.

6. Se hace un *análisis exploratorio*, podemos experimentar con diferentes  algoritmos de minería de datos o de aprendizaje automático. Al seleccionar los algoritmos debemos considerar los tipos de datos que tenemos. Por ejemplo algunos algoritmos no son apropiados para datos categóricos (modelo de celular). También debemos ajustar los parámetros para mejorar el desempeño y comparar el rendimiento entre los algoritmos.

7. En este paso se realiza la *minería de datos* a partir de el o los algoritmos seleccionados en el paso anterior.

Este paso nos arroja los *patrones ocultos* que describen a los datos. Siguiendo nuestro ejemplo, el resultado podría ser un conjunto de reglas nos que pueden servir para decidir si un cliente cancelará su subscripción. Una de las regla podría ser:
```
    SI el cliente tiene un promedio mayor a 7 días de retraso
      AND su promedio de llamadas al mes es menor que 10
    ENTONCES:
         el cliente cancelara el servicio
```
Los patrones son entonces son entonces Modelos que se ajustan a los datos. Los modelos no siempre están expresados en un lenguaje que los humanos podamos entender. Por ejemplo el resultado de un algoritmo de agrupamiento podrían ser simplemente grupos de clientes, que después deberíamos de interpretar.

En el texto utilizaremos el término modelo en lugar de patrones, ya que es más usual actualmente. Algo muy importante es que los modelos deben de representar también a datos nuevos. Digamos nuevos clientes que se subscriban el mes siguiente.       

8. En este paso nos toca *interpretar y evaluar* los patrones que encontramos en el paso anterior. Visualizar los patones y modelos extraídos. Decidir si se ha encontrado algún conocimiento útil.

9. El último paso es hacer algo con el conocimiento adquirido. Se puede utilizar directamente para tomar decisiones, incorporarlo como parte de un sistema o simplemente reportar los resultados a los interesados.

## Ejercicio Práctico: Iris, ¿Setosa, Virginica o Versicolor?

#### Nota:
Para realizar los ejercicios debes tener previamente instalada la distribución [Anaconda](https://www.continuum.io/downloads) con python 2.7.

Como primer ejercicio vamos a seguir el proceso de KDD para extraer conocimiento a partir del famoso [conjunto de datos de flores Iris](). El conjunto de datos incluso cuenta con su propia entrada en [wikipedia](https://es.wikipedia.org/wiki/Iris_flor_conjunto_de_datos). El conjunto de datos fue introducido por Ronald Fisher en un para un articulo en 1936. Contiene 50 muestras de tres especies de la flor Iris (Iris setosa, Iris virginica e Iris versicolor). Fisher midió cuatro características de cada muestra: el largo y ancho del sépalo y el largo y ancho del pétalo, en centímetros. Basado en la combinación de estos cuatro rasgos, Fisher se desarrolló un modelo discriminante lineal para distinguir entre una especie y otra. Como ejemplo veamos un fragmento que incluye varios registros de cada flor:

#### iris.csv

```
sepal_length,sepal_width,petal_length,petal_width,species
5.1,3.5,1.4,0.2,setosa
4.9,3.0,1.4,0.2,setosa
4.7,3.2,1.3,0.2,setosa
4.6,3.1,1.5,0.2,setosa
7.0,3.2,4.7,1.4,versicolor
6.4,3.2,4.5,1.5,versicolor
6.9,3.1,4.9,1.5,versicolor
5.5,2.3,4.0,1.3,versicolor
6.5,2.8,4.6,1.5,versicolor
6.3,3.3,6.0,2.5,virginica
5.8,2.7,5.1,1.9,virginica
7.1,3.0,5.9,2.1,virginica
6.3,2.9,5.6,1.8,virginica
6.5,3.0,5.8,2.2,virginica
```
Para compartir los conjuntos de datos normalmente se utilizan archivos en formato texto. En este caso el *dataset* se encuentra en formato CSV ( comma-separated values) con el cual es muy fácil representar datos tabulares. Los archivos CSV se pueden abrir e importar sin ningún problema a hojas de calculo y sistemas de bases de datos. Como podemos ver en el ejemplo los registros están separados por saltos de línea, y en la primera se indica el nombre de la columna. En este caso cada registro cuenta con cinco campos. Los primeros cuatro son las lecturas correspondientes en centímetros y el último es muy importante ya que es la etiqueta o clase. En este caso en particular la etiqueta indica el tipo de flor.

### Paso 1: identificar el objetivo

El objetivo del proceso de KDD será encontrar algunos patrones que nos permitan clasificar las flores, o algún otro conocimiento nuevo.

### Paso 2: seleccionar y recolectar

En este caso lo que debemos hacer es simplemente bajarnos el archivo *iris.csv* de alguna parte. Esto lo podemos hacer manualmente o directamente con Python.

#### Recolectar archivo iris.data

Esto lo vamos a hacer de manera interactiva desde el interprete. Para ejecutar el interprete simplemente escribimos python en la línea de comandos.

El interprete nos da la bienvenida:

```
Python 2.7.13 |Anaconda custom (x86_64)| (default, Dec 20 2016, 23:05:08)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>>
```
El archivo lo podemos bajar del Machine Learning Repository de la UCI (University of California Irvine). La URL directa es la siguiente:
https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data. Me ha tocado algunas veces que no esta disponible el servidor, si esto sucede descárgalo de algún otro lado.

Para bajarlo utilizaremos la biblioteca de python [requests](http://docs.python-requests.org/en/master/). Esta biblioteca ya viene instalada en Anaconda. Solamente tenemos que importarla:

``` python
>>> import requests
```   
Hacemos la petición *get* al archivo (esto puede tardar unos segundos):

``` python
>>> r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
```
Imprimimos el texto para ver que se haya bajado bien. Se debería ver esto:

``` python
>>> r.text
u'5.1,3.5,1.4,0.2,Iris-setosa\n4.9,3.0,1.4,0.2,Iris-setosa\n4.7,3.2,1.3,0.2,Iris-setosa\n4.6,3.1,1.5,0.2,Iris-setosa\n5.0,3.6,1.4,0.2,Iris-setosa\n5.4,3.9,1.7,0.4,Iris-setosa\n4.6,3.4,1.4,0.3,Iris-setosa\n5.0,3.4,1.5,0.2,Iris-setosa\n4.4,2.9,1.4,0.2,Iris-setosa\n4.9,3.1,1.5,0.1,Iris-setosa\n5.4,3.7,1.5,0.2,Iris-setosa\n4.8,3.4,1.6,0.2,Iris-setosa\n4.8,3.0,1.4,0.1,Iris-setosa\n4.3,3.0,1.1,0.1,Iris-setosa\n5.8,4.0,1.2,0.2,Iris-setosa\n5.7,4.4,1.5,0.4,Iris-setosa\n5.4,3.9,1.3,0.4,Iris-setosa\n5.1,3.5,1.4,0.3,Iris-setosa\n5.7,3.8,1.7,0.3,Iris-setosa\n5.1,3.8,1.5,0.3,Iris-setosa\n5.4,3.4,1.7,0.2,Iris-setosa\n5.1,3.7,1.5,0.4,Iris-setosa\n4.6,3.6,1.0,0.2,Iris-setosa\n5.1,3.3,1.7,0.5,Iris-setosa\n4.8,3.4,1.9,0.2,Iris-setosa\n5.0,3.0,1.6,0.2,Iris-setosa\n5.0,3.4,1.6,0.4,Iris-setosa\n5.2,3.5,1.5,0.2,Iris-setosa\n5.2,3.4,1.4,0.2,Iris-setosa\n4.7,3.2,1.6,0.2,Iris-setosa\n4.8,3.1,1.6,0.2,Iris-setosa\n5.4,3.4,1.5,0.4,Iris-setosa\n5.2,4.1,1.5,0.1,Iris-setosa\n5.5,4.2,1.4,0.2,Iris-setosa\n4.9,3.1,1.5,0.1,Iris-setosa\n5.0,3.2,1.2,0.2,Iris-setosa\n5.5,3.5,1.3,0.2,Iris-setosa\n4.9,3.1,1.5,0.1,Iris-setosa\n4.4,3.0,1.3,0.2,Iris-setosa\n5.1,3.4,1.5,0.2,Iris-setosa\n5.0,3.5,1.3,0.3,Iris-setosa\n4.5,2.3,1.3,0.3,Iris-setosa\n4.4,3.2,1.3,0.2,Iris-setosa\n5.0,3.5,1.6,0.6,Iris-setosa\n5.1,3.8,1.9,0.4,Iris-setosa\n4.8,3.0,1.4,0.3,Iris-setosa\n5.1,3.8,1.6,0.2,Iris-setosa\n4.6,3.2,1.4,0.2,Iris-setosa\n5.3,3.7,1.5,0.2,Iris-setosa\n5.0,3.3,1.4,0.2,Iris-setosa\n7.0,3.2,4.7,1.4,Iris-versicolor\n6.4,3.2,4.5,1.5,Iris-versicolor\n6.9,3.1,4.9,1.5,Iris-versicolor\n5.5,2.3,4.0,1.3,Iris-versicolor\n6.5,2.8,4.6,1.5,Iris-versicolor\n5.7,2.8,4.5,1.3,Iris-versicolor\n6.3,3.3,4.7,1.6,Iris-versicolor\n4.9,2.4,3.3,1.0,Iris-versicolor\n6.6,2.9,4.6,1.3,Iris-versicolor\n5.2,2.7,3.9,1.4,Iris-versicolor\n5.0,2.0,3.5,1.0,Iris-versicolor\n5.9,3.0,4.2,1.5,Iris-versicolor\n6.0,2.2,4.0,1.0,Iris-versicolor\n6.1,2.9,4.7,1.4,Iris-versicolor\n5.6,2.9,3.6,1.3,Iris-versicolor\n6.7,3.1,4.4,1.4,Iris-versicolor\n5.6,3.0,4.5,1.5,Iris-versicolor\n5.8,2.7,4.1,1.0,Iris-versicolor\n6.2,2.2,4.5,1.5,Iris-versicolor\n5.6,2.5,3.9,1.1,Iris-versicolor\n5.9,3.2,4.8,1.8,Iris-versicolor\n6.1,2.8,4.0,1.3,Iris-versicolor\n6.3,2.5,4.9,1.5,Iris-versicolor\n6.1,2.8,4.7,1.2,Iris-versicolor\n6.4,2.9,4.3,1.3,Iris-versicolor\n6.6,3.0,4.4,1.4,Iris-versicolor\n6.8,2.8,4.8,1.4,Iris-versicolor\n6.7,3.0,5.0,1.7,Iris-versicolor\n6.0,2.9,4.5,1.5,Iris-versicolor\n5.7,2.6,3.5,1.0,Iris-versicolor\n5.5,2.4,3.8,1.1,Iris-versicolor\n5.5,2.4,3.7,1.0,Iris-versicolor\n5.8,2.7,3.9,1.2,Iris-versicolor\n6.0,2.7,5.1,1.6,Iris-versicolor\n5.4,3.0,4.5,1.5,Iris-versicolor\n6.0,3.4,4.5,1.6,Iris-versicolor\n6.7,3.1,4.7,1.5,Iris-versicolor\n6.3,2.3,4.4,1.3,Iris-versicolor\n5.6,3.0,4.1,1.3,Iris-versicolor\n5.5,2.5,4.0,1.3,Iris-versicolor\n5.5,2.6,4.4,1.2,Iris-versicolor\n6.1,3.0,4.6,1.4,Iris-versicolor\n5.8,2.6,4.0,1.2,Iris-versicolor\n5.0,2.3,3.3,1.0,Iris-versicolor\n5.6,2.7,4.2,1.3,Iris-versicolor\n5.7,3.0,4.2,1.2,Iris-versicolor\n5.7,2.9,4.2,1.3,Iris-versicolor\n6.2,2.9,4.3,1.3,Iris-versicolor\n5.1,2.5,3.0,1.1,Iris-versicolor\n5.7,2.8,4.1,1.3,Iris-versicolor\n6.3,3.3,6.0,2.5,Iris-virginica\n5.8,2.7,5.1,1.9,Iris-virginica\n7.1,3.0,5.9,2.1,Iris-virginica\n6.3,2.9,5.6,1.8,Iris-virginica\n6.5,3.0,5.8,2.2,Iris-virginica\n7.6,3.0,6.6,2.1,Iris-virginica\n4.9,2.5,4.5,1.7,Iris-virginica\n7.3,2.9,6.3,1.8,Iris-virginica\n6.7,2.5,5.8,1.8,Iris-virginica\n7.2,3.6,6.1,2.5,Iris-virginica\n6.5,3.2,5.1,2.0,Iris-virginica\n6.4,2.7,5.3,1.9,Iris-virginica\n6.8,3.0,5.5,2.1,Iris-virginica\n5.7,2.5,5.0,2.0,Iris-virginica\n5.8,2.8,5.1,2.4,Iris-virginica\n6.4,3.2,5.3,2.3,Iris-virginica\n6.5,3.0,5.5,1.8,Iris-virginica\n7.7,3.8,6.7,2.2,Iris-virginica\n7.7,2.6,6.9,2.3,Iris-virginica\n6.0,2.2,5.0,1.5,Iris-virginica\n6.9,3.2,5.7,2.3,Iris-virginica\n5.6,2.8,4.9,2.0,Iris-virginica\n7.7,2.8,6.7,2.0,Iris-virginica\n6.3,2.7,4.9,1.8,Iris-virginica\n6.7,3.3,5.7,2.1,Iris-virginica\n7.2,3.2,6.0,1.8,Iris-virginica\n6.2,2.8,4.8,1.8,Iris-virginica\n6.1,3.0,4.9,1.8,Iris-virginica\n6.4,2.8,5.6,2.1,Iris-virginica\n7.2,3.0,5.8,1.6,Iris-virginica\n7.4,2.8,6.1,1.9,Iris-virginica\n7.9,3.8,6.4,2.0,Iris-virginica\n6.4,2.8,5.6,2.2,Iris-virginica\n6.3,2.8,5.1,1.5,Iris-virginica\n6.1,2.6,5.6,1.4,Iris-virginica\n7.7,3.0,6.1,2.3,Iris-virginica\n6.3,3.4,5.6,2.4,Iris-virginica\n6.4,3.1,5.5,1.8,Iris-virginica\n6.0,3.0,4.8,1.8,Iris-virginica\n6.9,3.1,5.4,2.1,Iris-virginica\n6.7,3.1,5.6,2.4,Iris-virginica\n6.9,3.1,5.1,2.3,Iris-virginica\n5.8,2.7,5.1,1.9,Iris-virginica\n6.8,3.2,5.9,2.3,Iris-virginica\n6.7,3.3,5.7,2.5,Iris-virginica\n6.7,3.0,5.2,2.3,Iris-virginica\n6.3,2.5,5.0,1.9,Iris-virginica\n6.5,3.0,5.2,2.0,Iris-virginica\n6.2,3.4,5.4,2.3,Iris-virginica\n5.9,3.0,5.1,1.8,Iris-virginica\n\n'
```
¡Muy bien!, a lo que sigue.

### Paso 3: Preprocesar los datos.

Una cadena enorme contiene todos los datos. Esto no nos sirven de mucho. El objetivo de este paso será procesar la cadena para tener como resultado un arreglo multidimensional de NumPy [QuickStart] (https://docs.scipy.org/doc/numpy-dev/user/quickstart.html). Este tipo de arreglos nos permite leer secciones a lo largo y ancho lo cual será muy útil en nuestro análisis. Más adelante veremos otras bibliotecas que simplificarán aun más este proceso como la biblioteca de análisis de datos [Pandas](http://pandas.pydata.org/).

Empezaremos por crear una lista a partir de una separación de la cadena. Esto lo hacemos con el método split() separando la cadena por los saltos de línea ('\n'):

``` python
>>> renglones_iris = r.text.split('\n')
```

Revisemos un poco el contenido de la lista:

``` python
>>> renglones_iris[:5]
[u'5.1,3.5,1.4,0.2,Iris-setosa', u'4.9,3.0,1.4,0.2,Iris-setosa', u'4.7,3.2,1.3,0.2,Iris-setosa', u'4.6,3.1,1.5,0.2,Iris-setosa', u'5.0,3.6,1.4,0.2,Iris-setosa']
```
Podemos ver un detalle importante al final de la lista: los últimos dos renglones están vacíos:
``` python
>>> renglones_iris[-4:]
[u'6.2,3.4,5.4,2.3,Iris-virginica', u'5.9,3.0,5.1,1.8,Iris-virginica', u'', u'']
```
Observamos también que cada uno de los elementos de la lista a su vez está separado por comas y no necesitamos el último dato ya que queremos solo las medidas en centímetros. Lo que queremos entonces es crear una nueva lista a partir de renglones_iris que tenga como elementos a su vez listas con las medidas. Para esto utilizaremos [comprensión de listas](). Primero vamos a hacer algunas pruebas:
```python
>>> [ renglon.split(',')[:-1] for renglon in renglones_iris[:-2]]
[[u'5.1', u'3.5', u'1.4', u'0.2'], [u'4.9', u'3.0', u'1.4', u'0.2'], [u'4.7', u'3.2', u'1.3', u'0.2'], [u'4.6', u'3.1', u'1.5', u'0.2'], [u'5.0', u'3.6', u'1.4', u'0.2'], [u'5.4', u'3.9', u'1.7', u'0.4'], [u'4.6', u'3.4', u'1.4', u'0.3'], [u'5.0', u'3.4', u'1.5', u'0.2'], [u'4.4', u'2.9', u'1.4', u'0.2'], [u'4.9', u'3.1', u'1.5', u'0.1'], [u'5.4', u'3.7', u'1.5', u'0.2'], [u'4.8', u'3.4', u'1.6', u'0.2'], [u'4.8', u'3.0', u'1.4', u'0.1'], [u'4.3', u'3.0', u'1.1', u'0.1'], [u'5.8', u'4.0', u'1.2', u'0.2'], [u'5.7', u'4.4', u'1.5', u'0.4'], [u'5.4', u'3.9', u'1.3', u'0.4'], [u'5.1', u'3.5', u'1.4', u'0.3'], [u'5.7', u'3.8', u'1.7', u'0.3'], [u'5.1', u'3.8', u'1.5', u'0.3'], [u'5.4', u'3.4', u'1.7', u'0.2'], [u'5.1', u'3.7', u'1.5', u'0.4'], [u'4.6', u'3.6', u'1.0', u'0.2'], [u'5.1', u'3.3', u'1.7', u'0.5'], [u'4.8', u'3.4', u'1.9', u'0.2'], [u'5.0', u'3.0', u'1.6', u'0.2'], [u'5.0', u'3.4', u'1.6', u'0.4'], [u'5.2', u'3.5', u'1.5', u'0.2'], [u'5.2', u'3.4', u'1.4', u'0.2'], [u'4.7', u'3.2', u'1.6', u'0.2'], [u'4.8', u'3.1', u'1.6', u'0.2'], [u'5.4', u'3.4', u'1.5', u'0.4'], [u'5.2', u'4.1', u'1.5', u'0.1'], [u'5.5', u'4.2', u'1.4', u'0.2'], [u'4.9', u'3.1', u'1.5', u'0.1'], [u'5.0', u'3.2', u'1.2', u'0.2'], [u'5.5', u'3.5', u'1.3', u'0.2'], [u'4.9', u'3.1', u'1.5', u'0.1'], [u'4.4', u'3.0', u'1.3', u'0.2'], [u'5.1', u'3.4', u'1.5', u'0.2'], [u'5.0', u'3.5', u'1.3', u'0.3'], [u'4.5', u'2.3', u'1.3', u'0.3'], [u'4.4', u'3.2', u'1.3', u'0.2'], [u'5.0', u'3.5', u'1.6', u'0.6'], [u'5.1', u'3.8', u'1.9', u'0.4'], [u'4.8', u'3.0', u'1.4', u'0.3'], [u'5.1', u'3.8', u'1.6', u'0.2'], [u'4.6', u'3.2', u'1.4', u'0.2'], [u'5.3', u'3.7', u'1.5', u'0.2'], [u'5.0', u'3.3', u'1.4', u'0.2'], [u'7.0', u'3.2', u'4.7', u'1.4'], [u'6.4', u'3.2', u'4.5', u'1.5'], [u'6.9', u'3.1', u'4.9', u'1.5'], [u'5.5', u'2.3', u'4.0', u'1.3'], [u'6.5', u'2.8', u'4.6', u'1.5'], [u'5.7', u'2.8', u'4.5', u'1.3'], [u'6.3', u'3.3', u'4.7', u'1.6'], [u'4.9', u'2.4', u'3.3', u'1.0'], [u'6.6', u'2.9', u'4.6', u'1.3'], [u'5.2', u'2.7', u'3.9', u'1.4'], [u'5.0', u'2.0', u'3.5', u'1.0'], [u'5.9', u'3.0', u'4.2', u'1.5'], [u'6.0', u'2.2', u'4.0', u'1.0'], [u'6.1', u'2.9', u'4.7', u'1.4'], [u'5.6', u'2.9', u'3.6', u'1.3'], [u'6.7', u'3.1', u'4.4', u'1.4'], [u'5.6', u'3.0', u'4.5', u'1.5'], [u'5.8', u'2.7', u'4.1', u'1.0'], [u'6.2', u'2.2', u'4.5', u'1.5'], [u'5.6', u'2.5', u'3.9', u'1.1'], [u'5.9', u'3.2', u'4.8', u'1.8'], [u'6.1', u'2.8', u'4.0', u'1.3'], [u'6.3', u'2.5', u'4.9', u'1.5'], [u'6.1', u'2.8', u'4.7', u'1.2'], [u'6.4', u'2.9', u'4.3', u'1.3'], [u'6.6', u'3.0', u'4.4', u'1.4'], [u'6.8', u'2.8', u'4.8', u'1.4'], [u'6.7', u'3.0', u'5.0', u'1.7'], [u'6.0', u'2.9', u'4.5', u'1.5'], [u'5.7', u'2.6', u'3.5', u'1.0'], [u'5.5', u'2.4', u'3.8', u'1.1'], [u'5.5', u'2.4', u'3.7', u'1.0'], [u'5.8', u'2.7', u'3.9', u'1.2'], [u'6.0', u'2.7', u'5.1', u'1.6'], [u'5.4', u'3.0', u'4.5', u'1.5'], [u'6.0', u'3.4', u'4.5', u'1.6'], [u'6.7', u'3.1', u'4.7', u'1.5'], [u'6.3', u'2.3', u'4.4', u'1.3'], [u'5.6', u'3.0', u'4.1', u'1.3'], [u'5.5', u'2.5', u'4.0', u'1.3'], [u'5.5', u'2.6', u'4.4', u'1.2'], [u'6.1', u'3.0', u'4.6', u'1.4'], [u'5.8', u'2.6', u'4.0', u'1.2'], [u'5.0', u'2.3', u'3.3', u'1.0'], [u'5.6', u'2.7', u'4.2', u'1.3'], [u'5.7', u'3.0', u'4.2', u'1.2'], [u'5.7', u'2.9', u'4.2', u'1.3'], [u'6.2', u'2.9', u'4.3', u'1.3'], [u'5.1', u'2.5', u'3.0', u'1.1'], [u'5.7', u'2.8', u'4.1', u'1.3'], [u'6.3', u'3.3', u'6.0', u'2.5'], [u'5.8', u'2.7', u'5.1', u'1.9'], [u'7.1', u'3.0', u'5.9', u'2.1'], [u'6.3', u'2.9', u'5.6', u'1.8'], [u'6.5', u'3.0', u'5.8', u'2.2'], [u'7.6', u'3.0', u'6.6', u'2.1'], [u'4.9', u'2.5', u'4.5', u'1.7'], [u'7.3', u'2.9', u'6.3', u'1.8'], [u'6.7', u'2.5', u'5.8', u'1.8'], [u'7.2', u'3.6', u'6.1', u'2.5'], [u'6.5', u'3.2', u'5.1', u'2.0'], [u'6.4', u'2.7', u'5.3', u'1.9'], [u'6.8', u'3.0', u'5.5', u'2.1'], [u'5.7', u'2.5', u'5.0', u'2.0'], [u'5.8', u'2.8', u'5.1', u'2.4'], [u'6.4', u'3.2', u'5.3', u'2.3'], [u'6.5', u'3.0', u'5.5', u'1.8'], [u'7.7', u'3.8', u'6.7', u'2.2'], [u'7.7', u'2.6', u'6.9', u'2.3'], [u'6.0', u'2.2', u'5.0', u'1.5'], [u'6.9', u'3.2', u'5.7', u'2.3'], [u'5.6', u'2.8', u'4.9', u'2.0'], [u'7.7', u'2.8', u'6.7', u'2.0'], [u'6.3', u'2.7', u'4.9', u'1.8'], [u'6.7', u'3.3', u'5.7', u'2.1'], [u'7.2', u'3.2', u'6.0', u'1.8'], [u'6.2', u'2.8', u'4.8', u'1.8'], [u'6.1', u'3.0', u'4.9', u'1.8'], [u'6.4', u'2.8', u'5.6', u'2.1'], [u'7.2', u'3.0', u'5.8', u'1.6'], [u'7.4', u'2.8', u'6.1', u'1.9'], [u'7.9', u'3.8', u'6.4', u'2.0'], [u'6.4', u'2.8', u'5.6', u'2.2'], [u'6.3', u'2.8', u'5.1', u'1.5'], [u'6.1', u'2.6', u'5.6', u'1.4'], [u'7.7', u'3.0', u'6.1', u'2.3'], [u'6.3', u'3.4', u'5.6', u'2.4'], [u'6.4', u'3.1', u'5.5', u'1.8'], [u'6.0', u'3.0', u'4.8', u'1.8'], [u'6.9', u'3.1', u'5.4', u'2.1'], [u'6.7', u'3.1', u'5.6', u'2.4'], [u'6.9', u'3.1', u'5.1', u'2.3'], [u'5.8', u'2.7', u'5.1', u'1.9'], [u'6.8', u'3.2', u'5.9', u'2.3'], [u'6.7', u'3.3', u'5.7', u'2.5'], [u'6.7', u'3.0', u'5.2', u'2.3'], [u'6.3', u'2.5', u'5.0', u'1.9'], [u'6.5', u'3.0', u'5.2', u'2.0'], [u'6.2', u'3.4', u'5.4', u'2.3'], [u'5.9', u'3.0', u'5.1', u'1.8']]
```

Lo que estamos haciendo es lo siguiente: a partir de la lista renglones_iris menos sus últimos dos elementos (renglones_iris[:-2]) vamos a generar una lista nueva procesando cada uno de sus elementos. Cada una de las cadenas en renglones_iris la vamos a separar por las comas y nos quedaremos con los primeros cuatro elementos (renglon.split(',')[:-1]).  Ya casi tenemos lo que necesitamos. Solamente faltaría convertir cada elemento a tipo flotante ya que como vemos son todas cadenas. Esto lo podemos hacer utilizando la función map() la cual aplica una función a cada elemento de la lista regresando una nueva. En este caso queremos utilizar la función float(). Veamos:

```python
>>> [map(float, renglon.split(',')[:-1]) for renglon in   renglones_iris[:-2]]
[[5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2], [4.6, 3.1, 1.5, 0.2], [5.0, 3.6, 1.4, 0.2], [5.4, 3.9, 1.7, 0.4], [4.6, 3.4, 1.4, 0.3], [5.0, 3.4, 1.5, 0.2], [4.4, 2.9, 1.4, 0.2], [4.9, 3.1, 1.5, 0.1], [5.4, 3.7, 1.5, 0.2], [4.8, 3.4, 1.6, 0.2], [4.8, 3.0, 1.4, 0.1], [4.3, 3.0, 1.1, 0.1], [5.8, 4.0, 1.2, 0.2], [5.7, 4.4, 1.5, 0.4], [5.4, 3.9, 1.3, 0.4], [5.1, 3.5, 1.4, 0.3], [5.7, 3.8, 1.7, 0.3], [5.1, 3.8, 1.5, 0.3], [5.4, 3.4, 1.7, 0.2], [5.1, 3.7, 1.5, 0.4], [4.6, 3.6, 1.0, 0.2], [5.1, 3.3, 1.7, 0.5], [4.8, 3.4, 1.9, 0.2], [5.0, 3.0, 1.6, 0.2], [5.0, 3.4, 1.6, 0.4], [5.2, 3.5, 1.5, 0.2], [5.2, 3.4, 1.4, 0.2], [4.7, 3.2, 1.6, 0.2], [4.8, 3.1, 1.6, 0.2], [5.4, 3.4, 1.5, 0.4], [5.2, 4.1, 1.5, 0.1], [5.5, 4.2, 1.4, 0.2], [4.9, 3.1, 1.5, 0.1], [5.0, 3.2, 1.2, 0.2], [5.5, 3.5, 1.3, 0.2], [4.9, 3.1, 1.5, 0.1], [4.4, 3.0, 1.3, 0.2], [5.1, 3.4, 1.5, 0.2], [5.0, 3.5, 1.3, 0.3], [4.5, 2.3, 1.3, 0.3], [4.4, 3.2, 1.3, 0.2], [5.0, 3.5, 1.6, 0.6], [5.1, 3.8, 1.9, 0.4], [4.8, 3.0, 1.4, 0.3], [5.1, 3.8, 1.6, 0.2], [4.6, 3.2, 1.4, 0.2], [5.3, 3.7, 1.5, 0.2], [5.0, 3.3, 1.4, 0.2], [7.0, 3.2, 4.7, 1.4], [6.4, 3.2, 4.5, 1.5], [6.9, 3.1, 4.9, 1.5], [5.5, 2.3, 4.0, 1.3], [6.5, 2.8, 4.6, 1.5], [5.7, 2.8, 4.5, 1.3], [6.3, 3.3, 4.7, 1.6], [4.9, 2.4, 3.3, 1.0], [6.6, 2.9, 4.6, 1.3], [5.2, 2.7, 3.9, 1.4], [5.0, 2.0, 3.5, 1.0], [5.9, 3.0, 4.2, 1.5], [6.0, 2.2, 4.0, 1.0], [6.1, 2.9, 4.7, 1.4], [5.6, 2.9, 3.6, 1.3], [6.7, 3.1, 4.4, 1.4], [5.6, 3.0, 4.5, 1.5], [5.8, 2.7, 4.1, 1.0], [6.2, 2.2, 4.5, 1.5], [5.6, 2.5, 3.9, 1.1], [5.9, 3.2, 4.8, 1.8], [6.1, 2.8, 4.0, 1.3], [6.3, 2.5, 4.9, 1.5], [6.1, 2.8, 4.7, 1.2], [6.4, 2.9, 4.3, 1.3], [6.6, 3.0, 4.4, 1.4], [6.8, 2.8, 4.8, 1.4], [6.7, 3.0, 5.0, 1.7], [6.0, 2.9, 4.5, 1.5], [5.7, 2.6, 3.5, 1.0], [5.5, 2.4, 3.8, 1.1], [5.5, 2.4, 3.7, 1.0], [5.8, 2.7, 3.9, 1.2], [6.0, 2.7, 5.1, 1.6], [5.4, 3.0, 4.5, 1.5], [6.0, 3.4, 4.5, 1.6], [6.7, 3.1, 4.7, 1.5], [6.3, 2.3, 4.4, 1.3], [5.6, 3.0, 4.1, 1.3], [5.5, 2.5, 4.0, 1.3], [5.5, 2.6, 4.4, 1.2], [6.1, 3.0, 4.6, 1.4], [5.8, 2.6, 4.0, 1.2], [5.0, 2.3, 3.3, 1.0], [5.6, 2.7, 4.2, 1.3], [5.7, 3.0, 4.2, 1.2], [5.7, 2.9, 4.2, 1.3], [6.2, 2.9, 4.3, 1.3], [5.1, 2.5, 3.0, 1.1], [5.7, 2.8, 4.1, 1.3], [6.3, 3.3, 6.0, 2.5], [5.8, 2.7, 5.1, 1.9], [7.1, 3.0, 5.9, 2.1], [6.3, 2.9, 5.6, 1.8], [6.5, 3.0, 5.8, 2.2], [7.6, 3.0, 6.6, 2.1], [4.9, 2.5, 4.5, 1.7], [7.3, 2.9, 6.3, 1.8], [6.7, 2.5, 5.8, 1.8], [7.2, 3.6, 6.1, 2.5], [6.5, 3.2, 5.1, 2.0], [6.4, 2.7, 5.3, 1.9], [6.8, 3.0, 5.5, 2.1], [5.7, 2.5, 5.0, 2.0], [5.8, 2.8, 5.1, 2.4], [6.4, 3.2, 5.3, 2.3], [6.5, 3.0, 5.5, 1.8], [7.7, 3.8, 6.7, 2.2], [7.7, 2.6, 6.9, 2.3], [6.0, 2.2, 5.0, 1.5], [6.9, 3.2, 5.7, 2.3], [5.6, 2.8, 4.9, 2.0], [7.7, 2.8, 6.7, 2.0], [6.3, 2.7, 4.9, 1.8], [6.7, 3.3, 5.7, 2.1], [7.2, 3.2, 6.0, 1.8], [6.2, 2.8, 4.8, 1.8], [6.1, 3.0, 4.9, 1.8], [6.4, 2.8, 5.6, 2.1], [7.2, 3.0, 5.8, 1.6], [7.4, 2.8, 6.1, 1.9], [7.9, 3.8, 6.4, 2.0], [6.4, 2.8, 5.6, 2.2], [6.3, 2.8, 5.1, 1.5], [6.1, 2.6, 5.6, 1.4], [7.7, 3.0, 6.1, 2.3], [6.3, 3.4, 5.6, 2.4], [6.4, 3.1, 5.5, 1.8], [6.0, 3.0, 4.8, 1.8], [6.9, 3.1, 5.4, 2.1], [6.7, 3.1, 5.6, 2.4], [6.9, 3.1, 5.1, 2.3], [5.8, 2.7, 5.1, 1.9], [6.8, 3.2, 5.9, 2.3], [6.7, 3.3, 5.7, 2.5], [6.7, 3.0, 5.2, 2.3], [6.3, 2.5, 5.0, 1.9], [6.5, 3.0, 5.2, 2.0], [6.2, 3.4, 5.4, 2.3], [5.9, 3.0, 5.1, 1.8]]
```

Ya que obtuvimos el código paso a paso, vamos a utilizarlo para crear el nuevo arreglo:

```python
>>> import numpy
>>> iris_data = [map(float, renglon.split(',')[:-1]) for renglon in   renglones_iris[:-2]]
>>> iris = numpy.array(iris_data)
```
Listo ya tenemos nuestros datos en una estructura adecuada:
```python
>>> iris[:10]
array([[ 5.1,  3.5,  1.4,  0.2],
       [ 4.9,  3. ,  1.4,  0.2],
       [ 4.7,  3.2,  1.3,  0.2],
       [ 4.6,  3.1,  1.5,  0.2],
       [ 5. ,  3.6,  1.4,  0.2],
       [ 5.4,  3.9,  1.7,  0.4],
       [ 4.6,  3.4,  1.4,  0.3],
       [ 5. ,  3.4,  1.5,  0.2],
       [ 4.4,  2.9,  1.4,  0.2],
       [ 4.9,  3.1,  1.5,  0.1]])
```
### Paso 4: Transformar los datos
En este caso sencillo no será necesario transformar los datos.

### Paso 5:  Seleccionar la tarea de minería de datos
La tarea que vamos a realizar será *Clasificación*.

### Paso 6:  Análisis exploratorio
La minería de datos en este primer ejercicio la vamos a realizar manualmente, para esto vamos a explorar los datos visualmente. Para ello utilizaremos la popular biblioteca [matplotlib](https://matplotlib.org/). Primero vamos a seleccionar las dos primeras características: ancho y largo del sépalo para ver si hay algún patrón útil. Importamos matplotlib y hacemos el plot de la primera flor. Los primeros cincuenta datos son de Iris Setosa:   

```python
>>> import matplotlib.pyplot as plt
>>> x = iris[:50,0]
>>> y = iris[:50,1]
>>> plt.plot(x, y, 'r.')
>>> plt.show()
```

Al ejecutar la instrucción plt.show() se debería mostrar lo siguiente:
![Setosa](../img/plot1.png)


En el eje **x** tenemos el ancho del sépalo Y en el eje **y** el largo, ambos en cm. El parámetro 'r.' indica que las flores Setosa se representarán por puntos rojos ('r.' red dots).

Ahora graficaremos al mismo tiempo las flores Setosa y Versicolor:

```python
>>> plt.plot( iris[:50,0], iris[:50,1], 'r.') # Setosa
[<matplotlib.lines.Line2D object at 0x1066ed610>]
>>> plt.plot( iris[51:100,0], iris[51:100,1], 'b.')
[<matplotlib.lines.Line2D object at 0x113731710>] # Virginica
>>> plt.show()
```
Descubrimos algo, es posible separar linealmente o clasificar ambas flores utilizando estas dos características:
![Setosa y Virginica](../img/plot2.png)

```python
>>> plt.plot( iris[51:100,0], iris[51:100,1], 'b.')
[<matplotlib.lines.Line2D object at 0x114cae950>]
>>> plt.plot( iris[101:,0], iris[101:,1], 'g.')
[<matplotlib.lines.Line2D object at 0x114cbc110>]
>>> plt.show()
```
Veremos si corremos con igual suerte al agregar la Versicolor:

```python
[<matplotlib.lines.Line2D object at 0x114cae850>]
>>> plt.plot( iris[51:100,0], iris[51:100,1], 'b.')
[<matplotlib.lines.Line2D object at 0x114cae950>]
>>> plt.plot( iris[101:,0], iris[101:,1], 'g.')
[<matplotlib.lines.Line2D object at 0x114cbc110>]
>>> plt.show()
```

![Setosa, Virginica, Versicolor](../img/plot3.png)

Por lo menos al considerar estas dos características vemos que es difícil distinguir entre las flores Virginica y Versicorlor.

### Paso 7:  Minería de Datos

Este paso lo vamos a hacer manualmente por lo pronto. ¿Como podríamos especificar el modelo?. Una manera muy sencilla sería la siguiente:

![Setosa, Virginica, Versicolor](../img/plot4.png)

Utilizando una recta para separar a las flores Setosa del resto. Podríamos además utilizar varias rectas o incluso funciones no lineales. Estas ideas las podremos llevar acabo "manualmente" ya que solo estamos considerando dos características. Esto se puede tornar más difícil al considerar las otras dos medidas pues estaríamos trabajando en dimensión cuatro.

Otra modelo podría ser expresado en forma de reglas:
```
R1:
    SI sepal_length < 5.9 AND sepal_width > 2.9
    ENTONCES:
         Setosa

R2:
    SI sepal_length < 4.7 AND sepal_width <= 2.9
    ENTONCES:
         Setosa
```

Gráficamente sería algo como:

![Setosa, Virginica, Versicolor](../img/plot5.png)

Ya que estamos en esto podemos proponer un nuevo modelo simplemente agregando otra regla:
![Setosa, Virginica, Versicolor](../img/plot6.png)

Podríamos segur buscando, por ejemplo cambiando un poco los antecedentes de las reglas, por ejemplo de sepal_length < 5.9 a sepal_length < 6.0. Nos empezamos a dar cuenta que no es fácil hacer esto manualmente. Mejor hagamos programas que hagan este trabajo de generar modelos automáticamente. Es decir, algoritmos de aprendizaje automático.

### Paso 8. Interpretar y evaluar

Esto lo haremos más adelante, pero vale la pena pensar un poco al respecto. ¿Cual es mejor modelo?, ¿El mejor es suficientemente bueno?, ¿Existe un modelo óptimo?. ¿Que pasará cuando agreguemos nuevas flores al conjunto de datos?.
También debemos pensar si pudimos extraer algún conocimiento nuevo. ¿Es útil?.

### Paso 9. Aplicar el conocimiento adquirido

De este pequeño ejercicio podríamos reportar que las flores Setosa son fáciles de identificar.  

Este ejercicio es básico y además no hicimos todas las consideraciones. Más adelante veremos otros detalles que no hemos considerado y por supuesto ya no haremos la minería de datos manualmente. El ejercicio también ha servido para darnos idea de como trabajaremos con Python y sus bibliotecas para este tipo de tareas. Seguro te diste cuenta que no hemos utilizado ciclos, enviamos funciones como parámetros y trabajamos de forma interactiva para llegar a la solución.

#### Atención estudiantes:
Si te fijas el proceso de KDD también puede ser utilizado como guía para hacer  proyectos de investigación en el área. El proceso es el mismo pero cambian los algoritmos, aplicaciones y tipos de datos.

## Algunas definiciones y Tecnologías Complementarias

### Minería de datos
El libro se enfocará principalmente en el componente de Minería de Datos, que como vimos es un paso importante en el proceso de KDD. Pero también te haz dado cuenta que es muy importante hacer bien los pasos anteriores. De hecho en la mayoría de los proyectos los otros pasos requieren de mayor trabajo. La minería de datos entonces podemos definirla como: El proceso de búsqueda de patrones aplicando distintos algoritmos a grandes cantidades de datos. Algunas veces se utiliza el término Minería de Datos para referirse a todo el proceso de KDD.

### Aprendizaje automático (Machine Learning)
El aprendizaje automático es el área de las ciencias computacionales encargada de estudiar y desarrollar los algoritmos capaces de aprender y hacer predicciones a partir de los datos. Podríamos decir que en el proceso de vamos a aplicar algoritmos de aprendizaje automático, por lo que debemos conocer muy bien sus fundamentos y limitaciones.

### Ciencia de datos
Como hemos visto el proceso de KDD busca extraer conocimiento partir de los datos. ¿Y si vamos más allá?. La ciencia de datos es similar al KDD pero el conocimiento que se busca es el conocimiento científico. Es hacer ciencia a partir de los datos. La ciencia apoyada en datos (en inglés data-driven science) al igual que el KDD es una campo interdisciplinario que incluye métodos científicos, procesos, y sistemas para extraer conocimiento o entendimiento a partir de los datos.

### Computación inteligente
La expresión computación inteligente (CI de computational intelligence) se asocia a la habilidad de un sistema de computo de aprender a realizar una tarea a partir de datos o la observación. Una distinción importante es que los métodos empleados se son inspirados en la naturaleza. La CI busca resolver problemas complejos del mundo-real para los cuales el modelado tradicional o matemático son insuficientes. Los métodos más representativos son: redes neuronales artificiales, lógica difusa y computación evolutiva.

### Big Data
Big Data se refiere al caso de sistemas que cuentan con cantidades enormes de datos. Normalmente los datos se almacenan en un servidor central. En el caso de Big Data los datos son tantos que deben almacenarse en muchos servidores. También el tipo de dato podría ser muy grande, por ejemplo un registro de un experimento determinado podría medir un TeraByte. En estos casos las técnicas o algoritmos tradicionales resultan inadecuados. El usar Big Data no implica Minería de Datos, muchos sistemas solamente requieren procesar los datos, por ejemplo para realizar una consulta o algún calculo. Claro que también hay procesos de Minería de Datos que se realizan utilizando Big Data, esto requiere de tecnología y algoritmos especializados.


## Algunas Aplicaciones

### Modelado de sistemas no lineales
En general se utiliza la Minería de Datos para modelar sistemas no lineales. En caso de que no estés familiarizado veamos un ejemplo. Ana entra a trabajar a las 7:00 am. El trabajo de Ana está a 10 km de su casa. Ella normalmente sale de su casa a las 6:20 y llega a las 6:40, hace 20 minutos. En ocasiones sale a las 6:10 y  claro llega a las 6:30. Hasta aquí todo va bien, los tiempos siguen un comportamiento lineal y constante. Incluso podemos calcular que si antes deja a sus hijos en la escuela que está a 5 km, llegará en 10 minutos. El problema viene cuando Ana sale de casa a las 6:25 en ese caso hace 25 minutos y si sale a las 6:30 hace 40 minutos y llega tarde a su trabajo. ¿Por que el sistema no sigue un comportamiento lineal?. El problema es que el tiempo que hace a su trabajo no solo depende de la velocidad promedio y la distancia. El tiempo depende del tráfico, la ruta que tome, si se pone un policía a dirigir el tráfico, si hay alguna manifestación, si las primarias están de vacaciones, etc. El problema se vuelve no lineal por que está ubicado en el mundo real, y si queremos hacer un calculo más exacto tendríamos que considerar muchas variables, incluso podríamos hacer un simulador. Cuando salimos a nuestro trabajo muchos hacemos un cálculo mental del tiempo que haremos por eso los optimistas llegamos tarde. Pero, ¿en que basamos nuestro cálculo si el sistema es no lineal y por lo tanto muy complejo?. Así es, en nuestra experiencia, es decir en extraer de nuestra mente el tiempo que hemos hecho los días anteriores, de nuestro sentido común "hoy es viernes, habrá mucho tráfico". La minería de datos puede ayudarnos a modelar este tipo de sistemas, sin que tengamos nosotros que establecer las relaciones no lineales entre muchas variables.

### Ruido
El ruido es una complicación común en sistemas del mundo-real. Por ejemplo, cuando se le pone un sensor a un paciente, en ocasiones las lecturas se ven afectadas por los movimientos del paciente y registran valores erróneos o muy altos o bajos en comparación con el valor real. Descubrir patrones en presencia de ruido es bastante difícil, por lo que se deben elegir técnicas de modelado que toleren el ruido.     

### Internet de las Cosas
El concepto de Internet de las Cosas (IoT) se refiere básicamente a que todas las cosas están conectadas al Internet y pueden recopilar e intercambiar datos. Crear modelos de sistemas no lineales con muchísimas variables es muy complicado. La tecnología de IoT se puede aplicar en sistemas de ciudades inteligentes, para agilizar el tráfico en tiempo real o abrir el paso a los bomberos cuando se dirigen a atender una emergencia. Estos sistemas deben considerar las lecturas en tiempo real de muchísimos sensores y determinar como se afectan entre sí, para determinar si hay alguna emergencia grave, predecir el tráfico. Utilizando técnicas de aprendizaje automático es posible modelar este tipo de sistemas.    

### Reconocimiento de patrones en multimedia
Al momento de subir a Facebook la tradicional *selfie* con los amigos, el sistema nos sugiere etiquetar las caras de ellos con su nombre de usuario correcto. Es decir, el sistema reconoció al usuario a partir de la imagen una imagen de rostro. Esto es parecido a lo que hicimos anteriormente con las flores Iris. Pero en lugar de 4 variables de entrada tenemos un arreglo de los cientos de pixeles que hacen la imagen y en lugar de tres flores, tenemos cientos de amigos. En el caso de las flores recordamos que ya estaban etiquetadas. En el caso de Facebook, la extracción del modelo requiere que ya haya ejemplos de los rostros asociados a los usuarios. Nosotros mismos agregamos ejemplos clasificados cada que manualmente etiquetamos un rostro. Las mismas técnicas pueden utilizarse para reconocer gestos, la voz, huellas digitales, firmas, letra escrita, copias de videos y muchos otros patrones.  

### Negocios
Se utiliza el KDD principalmente para el mercadeo dirigido, para calcular el riesgo de alguna operación, predecir cambios en los mercados, identificar tendencias a partir de las publicaciones en redes sociales, recomendar productos o personalizar servicios.   

### Ciencia
POR HACER

## Técnicas de la minería de datos
### Clasificación
### Agrupamiento
### Regresión
### Optimización

### Reglas de asociación
### Detección de anomalías


## Los Retos
### Escalabilidad
### Tipos de Datos



[Lectura adicional](http://www.kdnuggets.com/gpspubs/aimag-kdd-overview-1996-Fayyad.pdf)
