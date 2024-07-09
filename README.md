# Proyecto Individual: 

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

La data presenta en varias variables valores atipicos, 

