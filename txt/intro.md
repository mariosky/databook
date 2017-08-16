## Introducción
Cuando visitamos al médico, confiamos que el ha adquirido un amplio conocimiento por medio de interactuar con su entorno y su capacidad de procesar la información que lo rodea. El médico es capaz de dar un diagnóstico evaluando la información que le damos y lo que el puede observar. Si en lugar de asistir con un humano eligiéramos a un robot-médico, más vale que cuente con una buena inteligencia artificial. Según Rusell y Norvig el término inteligencia artificial se aplica cuando una máquina imita las funciones cognitivas que los humanos asocian con otras mentes humanas, como por ejemplo: *aprender* y *resolver problemas* [ref]. Precisamente, una de las primeras aplicaciones de la inteligencia artificial ha sido desarrollo de Sistemas Expertos, los cuales pueden emular la toma de decisiones de un humano experto, por ejemplo a un médico. Un ejemplo de este tipo de sistemas fue [Mycin](https://es.wikipedia.org/wiki/Mycin) el cual se basaba principalmente en un sencillo motor de inferencia, que manejaba una base de conocimiento de aproximadamente unas 500 reglas. Estas reglas [representaban el conocimiento](https://es.wikipedia.org/wiki/Representaci%C3%B3n_del_conocimiento) de los médicos. Una desventaja de este tipo de sistemas era que se requiere de mucho esfuerzo y recursos para extraer el conocimiento de los expertos. Se debía entrevistar a los expertos utilizando técnicas de *elicitación del conocimiento* para después representar dicho conocimiento de alguna manera y almacenarlo en una *base de conocimiento*. ¿El conocimiento "humano" podrá ser extraído  de otras fuentes?. ¿Y si contamos con una base de datos de miles de diagnósticos realizados anteriormente?. ¿Y si pudiéramos extraer de esta base de datos nuevo conocimiento?. ¿Se podría sin intervención humana?. Este es el tipo de preguntas que trata de contestar el área de investigación de la  inteligencia artificial, pero como veremos más adelante, en esto se involucran muchas otras áreas de investigación.

### Descubrimiento de conocimiento en bases de datos (KDD)
Al proceso de extraer conocimiento útil a partir de datos se le denomina Descubrimiento de Conocimiento en Bases de Datos o KDD ya que es muy común utilizar estas siglas del inglés "Knowledge Discovery from Databases". Este proceso puede hacerse manualmente, expertos en algún dominio pueden consultar y analizar bases de datos para descubrir patrones que les ayuden a tomar decisiones. Por ejemplo, en la película "The BigShort" podemos ver al inversionista Michael Burry analizar grandes cantidades de datos para después predecir el eminente  desplome de la burbuja de bienes y raíces en los Estados Unidos. Como podemos imaginar, este proceso no es trivial, no es simplemente hacer una consulta en una base de datos o en una motor de búsqueda. El KDD sigue evolucionando involucrando áreas de investigación como: aprendizaje automático, reconocimiento de patrones, computación inteligente, estadística, procesamiento de lenguaje natural, visualización entre otros. La Minería de Datos de hecho es uno de los componentes del KDD.

Antes de hablar de Minería de datos veamos el proceso del KDD, según el esquema de Brachman y Anand:

![El procesos del KDD según Brachman y Anand](../img/Proceso-KDD.png)

1. El proceso inicia con identificar el objetivo del proceso de KDD. Por ejemplo, un proveedor de telefonía móvil está interesado en identificar a aquellos clientes que ya no renovarán su contrato y se irán con la competencia.

2. El siguiente paso es seleccionar y recolectar aquellos datos necesarios para el proceso. Para nuestro ejemplo, podríamos requerir el historial de pago de los clientes, datos sobre quejas y llamadas que ha hecho a soporte, servicios adicionales que ha contratado o cancelado, etc. Esta información puede estar distribuida en diferentes bases de datos. También podría ser información que se colecte desde sensores o sistemas externos, por ejemplo lecturas del GPS, caídas en de la conexión o el número de aplicaciones que ha instalado.

3. Es necesario preprocesar los datos para limpiarlos de datos erróneos, datos faltantes, cambios de formato, inconsistencias, etc.

4. Dependiendo de los objetivos se deben transformar los datos para simplificar su procesamiento. Por ejemplo un documento de texto es necesario transformarlo en vector representativo. Una imagen puede ser transformada en una representación simplificada pero conservando sus características esenciales. Muchas veces también es necesario eliminar campos que no aportan mucho a la tarea de KDD. Siguiendo nuestro ejemplo, después de un análisis podríamos darnos cuenta que el número de teléfono en sí no es un dato importante para distinguir el comportamiento de los clientes, y que al contrario la marca y modelo de sus móviles son muy importantes.

5. 


### Minería de datos

### Aprendizaje automático

### Ciencia de datos

## Aplicaciones

## Técnicas de la minería de datos
### Clasificación
### Agrupamiento
### Reglas de asociación
### Detección de anomalías

## Los Retos


[Lectura adicional](http://www.kdnuggets.com/gpspubs/aimag-kdd-overview-1996-Fayyad.pdf)


## Un problema de clasificación

### ¿Iris, Setosa o Versicolor?

### Python al rescate
