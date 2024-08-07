# Proyecto Individual: Plataforma de Streaming: Movies
### Tabla de contenidos

1. [Contexto](#contexto)
2. [Instalacion y requisitos](#instalacion-y-requisitos)
3. [Pasos de instalacion](#pasos-de-instalacion)
4. [Etl](#etl)
5. [Api](#api)
6. [Eda](#eda)
7. [Documentos del proyecto](#documentos-del-proyecto)
8. [Datos y Fuentes](#datos-y-fuentes)
9. [Metodologia](#metodologia)
10. [Autor](#autor)

### Contexto
Te encuentras trabajando como Data Scientist en una startup que ofrece servicios de agregación de plataformas de streaming. Te han asignado la tarea de desarrollar un sistema de recomendación de películas para los usuarios de la plataforma. Para ello, deberás realizar un proceso de Extracción, Transformación y Carga (ETL) de los datos, un Análisis Exploratorio de Datos (EDA) y finalmente, implementar una API para que el sistema pueda ser utilizado por la aplicación.

### Instalacion y requisitos

- python 3.11 o superior
- pandas
- numpy
- scikit-learn 1.5.1
- fastAPI 0.111.0
- pyarrow y pydantic 16.1.0 y 2.8.2 respectivamente
- nltk 3.8.2
- matplotlib
- seaborn

Para una mayor especificación revisar el archivo requirements.txt

### Pasos de instalacion:
1. Clonar el repositorio: "[url del repo](https://github.com/Pableren/Henry_proyectos.git)"
2. Crear el entorno virtual: "python -m venv venv
3. Activar el entorno virtual:
- Navegar hacia la carpeta
- Windows: venv\Scripts\activate
- Instalar las dependencias: pip install -r requirements.txt
5. En caso de estar en un entorno local ejecutar "uvicorn main:app --reload" e ir al puerto por defecto 127.0.0.1:8000 y realizar las consultas.

### ETL

Se realizo un proceso ETL donde se extrajo la informacion de los datos, contenida en 2 archivos. Separados en peliculas y creditos.
Para la data de peliculas, se realizo la desanidacion de algunas columnas con datos anidados y se guardo en un formato mas familiar a python(lista de listas).
Se eliminaron algunas columnas que no fueron necesarias para el analisis y se eliminaron valores nulos de la data.

Respecto a la data de creditos, que tambien se encontraba anidada, se dividio en 2 dataframes de pandas.
Cada fila del dataframe representa un "valor" de la data anidada y sus columnas son las "claves" de la data y se reservaron 1 dataframe para el casting(reparto) y otro para la crew(equipo). Se habla de clave-valor debido a que interpretamos los datos como diccionarios de python.

### Api

La api se desarrollo con FastApi dentro de python, la cual cuenta con las siguientes funciones:
- def cantidad_filmaciones_mes( Mes ): Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.
- def cantidad_filmaciones_dia( Dia ): Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.
- def score_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.
- def votos_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones.
- def get_actor( nombre_actor ): Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno.
- def get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno.
- def recomendacion( titulo ): Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.

### EDA

La data presenta en varias variables valores atipicos, y en variables como vote_average poseen una distribucion normal. Se observo una tendencia de la popularidad de las peliculas al alza a lo largo de los años. Tambien se observo la distribucion de las peliculas para cada uno de los generos y se realizo un analisis temporal de la popularidad de las peliculas.


### Documentos del proyecto
- data/: Contiene los datasets del proyecto.
- notebooks/: Notebooks(eda y etl) del proyecto
- README.md: Documentacion del proyecto
- requirements.txt: Archivo con las librerias y dependencias del proyecto
- main.py: Archivo principal de la api.
- Funciones.py: Archivo que almacena las funciones creadas durante el proyecto y que serviran para procesar y visualizar los datos.

### Datos y fuentes

La empresa start-up que provee servicios de agregación de plataformas de streaming nos consiguio una muestra de su base de datos para analizar con informacion respecto de las peliculas, reparto y equipo.

### Metodologia

Se aplicaron metodos de procesamiento de los datos para aumentar la eficiencia de la lectura de los datos y mejorar la eficiencia de las funciones.
Se realizo un analisis exploratorio de los datos para encontrar patrones y tendencia en los datos de las peliculas. Tambien se aplico un sistema de recomendacion con un CountVectorizer para evaluar la similitud de las peliculas.

### Autor:

Este proyecto fue realizado por Pablo Chamena. Dataft23 grupo 03

- Linkedin: (www.linkedin.com/in/pablo-chamena-8814bb211)

