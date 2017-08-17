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

### ¿Iris, Setosa o Versicolor?

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

## Paso 1: identificar el objetivo

El objetivo del proceso de KDD será encontrar algunos patrones que nos permitan clasificar las flores, o algún otro conocimiento nuevo.

## Paso 2: seleccionar y recolectar

En este caso lo que debemos hacer es simplemente bajarnos el archivo *iris.csv* de alguna parte. Esto lo podemos hacer manualmente o directamente con Python.

  

### Minería de datos
Como hemos visto la Minería de Datos es un paso importante en el proceso de KDD, ya que a su vez es el proceso iterativo de búsqueda de patrones aplicando distintos algoritmos.

### Aprendizaje automático

### Ciencia de datos

## Aplicaciones

## Técnicas de la minería de datos
### Clasificación
### Agrupamiento
### Reglas de asociación
### Detección de anomalías

## Los Retos







### Python al rescate


[Lectura adicional](http://www.kdnuggets.com/gpspubs/aimag-kdd-overview-1996-Fayyad.pdf)
