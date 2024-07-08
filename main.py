#def cantidad_filmaciones_mes( Mes ):
# Se ingresa un mes en idioma Español. Debe devolver la cantidad
# de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.
# Ejemplo de retorno: X cantidad de películas fueron estrenadas en el mes de X

#levantar servidor uvicorn: uvicorn main:app --reload
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import pandas as pd
import numpy as np
import re
import json
import ast

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('popular')
## librerias para el Sistema de recomendacion

app = FastAPI()

df_movies = pd.read_parquet('data/df_movies_parquet.parquet',engine='pyarrow')
datos_crew = pd.read_parquet('data/df_crew_parquet.parquet',engine='pyarrow')
datos_cast = pd.read_parquet('data/df_cast_parquet.parquet',engine='pyarrow')
### debido a la transformacion de los datos anidados, debemos usar json.loads y json.dumps para
### serializarlo o deserializarlo
df_movies['genres'] = df_movies['genres'].apply(json.loads)

df_movies = df_movies.rename(columns={'id': 'id_credit'})

#ruta local: http://127.0.0.1:8000
@app.get("/")
async def root():
    return "Raiz de la API"

@app.get("/url")
async def url():
    return {"url_repo":"https://github.com/Pableren/Proyectos.git"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


#Funcion para cantidad de filmaciones por mes:
# pasar datos como: 127.0.0.1:8000/filmaciones_mes/enero
@app.get("/cantidad_filmaciones_mes/{mes}")
async def cantidad_filmaciones_mes(mes: str):
    df_unico = df_movies.drop_duplicates(subset=['id_credit', 'release_date'])
    cantidad_peliculas_mes = df_unico['release_date'].dt.month.value_counts()
    cantidad_peliculas_mes.sort_index(inplace=True)
    print(type(cantidad_peliculas_mes))
    if str(mes).lower() == "enero":
        #dic = dict({"la cantidad de peliculas estrenadas en enero fue de: ":str(cantidad_peliculas_mes[1])})
        retorno = {f"la cantidad de peliculas estrenas el mes {mes} fue de: ":str(cantidad_peliculas_mes[1])}
        return retorno
    elif str(mes).lower() == "febrero":
        retorno = {f"la cantidad de peliculas estrenas el mes {mes} fue de: ":str(cantidad_peliculas_mes[2])}
        return retorno
    elif str(mes).lower()== "marzo":
        retorno = {f"la cantidad de peliculas estrenas el mes {mes} fue de: ":str(cantidad_peliculas_mes[3])}
        return retorno
    elif str(mes).lower()== "abril":
        retorno = {f"la cantidad de peliculas estrenas el mes {mes} fue de: ":str(cantidad_peliculas_mes[4])}
        return retorno
    elif str(mes).lower()== "mayo":
        retorno = {f"la cantidad de peliculas estrenas el mes {mes} fue de: ":str(cantidad_peliculas_mes[5])}
        return retorno
    elif str(mes).lower()== "junio":
        retorno = {f"la cantidad de peliculas estrenas el mes {mes} fue de: ":str(cantidad_peliculas_mes[6])}
        return retorno
    elif str(mes).lower()== "julio":
        retorno = {f"la cantidad de peliculas estrenas el mes {mes} fue de: ":str(cantidad_peliculas_mes[7])}
        return retorno
    elif str(mes).lower()== "agosto":
        retorno = {f"la cantidad de peliculas estrenas el mes {mes} fue de: ":str(cantidad_peliculas_mes[8])}
        return retorno
    elif str(mes).lower()== "septiembre":
        retorno = {f"la cantidad de peliculas estrenas el mes {mes} fue de: ":str(cantidad_peliculas_mes[9])}
        return retorno
    elif str(mes).lower()== "octubre":
        retorno = {f"la cantidad de peliculas estrenas el mes {mes} fue de: ":str(cantidad_peliculas_mes[10])}
        return retorno
    elif str(mes).lower()== "noviembre":
        retorno = {f"la cantidad de peliculas estrenas el mes {mes} fue de: ":str(cantidad_peliculas_mes[11])}
        return retorno
    elif str(mes).lower()== "diciembre":
        retorno = {f"la cantidad de peliculas estrenas el mes {mes} fue de: ":str(cantidad_peliculas_mes[12])}
        return retorno
    else:
        print("valor no valido, use solo letras sin tildes")
        return {}

#def cantidad_filmaciones_dia( Dia ): Se ingresa un día en idioma Español.
# Funcion para cantidad de filmaciones por dia


# Aclaracion: a la funcion cantidad_filmaciones_dia, se le pasara como parametro un int representando el dia del mes
# A la funciones cantidad_filmaciones_diaDeSemana, se le pasara el dia de la semana como cadena de texto sin tildes
# lunes,martes,miercoles,jueves,viernes,sabado,domingo


@app.get("/cantidad_filmaciones_dia/{dia}")
async def cantidad_filmaciones_dia(dia: str):
    dia = str(dia).lower()
    df_unico = df_movies.drop_duplicates(subset=['id_credit', 'release_date'])
    peliculas_dia = df_unico['release_date'].dt.day_of_week.value_counts()
    peliculas_dia.sort_index(inplace=True)
    indice = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
    peliculas_dia.index = indice
    if (dia == 'lunes'):
        retorno = {f"la cantidad de peliculas estrenadas un {dia} fueron: ":str(peliculas_dia[dia])}
        return retorno
    elif (dia == 'martes'):
        retorno = {f"la cantidad de peliculas estrenadas un {dia} fueron: ":str(peliculas_dia[dia])}
        return retorno
    elif (dia == 'miercoles'):
        retorno = {f"la cantidad de peliculas estrenadas un {dia} fueron: ":str(peliculas_dia[dia])}
        return retorno
    elif (dia == 'jueves'):
        retorno = {f"la cantidad de peliculas estrenadas un {dia} fueron: ":str(peliculas_dia[dia])}
        return retorno
    elif (dia == 'viernes'):
        retorno = {f"la cantidad de peliculas estrenadas un {dia} fueron: ":str(peliculas_dia[dia])}
        return retorno
    elif (dia == 'sabado'):
        retorno = {f"la cantidad de peliculas estrenadas un {dia} fueron: ":str(peliculas_dia[dia])}
        return retorno
    elif (dia == 'domingo'):
        retorno = {f"la cantidad de peliculas estrenadas un {dia} fueron: ":str(peliculas_dia[dia])}
        return retorno
    else:
        print("valor no valido")
        return {}


@app.get("/cantidad_filmaciones_diaDelMes/{dia}")
async def cantidad_filmaciones_diaDelMes(dia: int):
    df_unico = df_movies.drop_duplicates(subset=['id_credit', 'release_date'])
    peliculas_dia = df_unico['release_date'].dt.day.value_counts()
    peliculas_dia.sort_index(inplace=True)
    if type(dia) == int:
        retorno = peliculas_dia[dia]
        return {f"la cantidad de peliculas estrenadas el dia {dia} es:":str(retorno)}
    else:
        return {}

#def score_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando
# como respuesta el título, el año de estreno y el score.
# Ejemplo de retorno: La película X fue estrenada en el año X con un score/popularidad de X


#@app.get("/score_titulo/{dia}")
#async def score_titulo(titulo: str):
 #   return None

@app.get("/score_titulo/{titulo}")
async def score_titulo(titulo: str):
    titulo = str(titulo).strip().lower()
    df_movies['title'] = df_movies['title'].str.lower() 
    df_unico = df_movies.drop_duplicates(subset=['title','id_credit'])
    filtrado = df_unico[df_unico['title'] == titulo]
    if filtrado.empty:
        return {f"No se encontró información sobre la filmación:'":{titulo}}
    titulo = filtrado['title'].values[0]
    año = filtrado['release_year'].values[0]
    score = filtrado['popularity'].values[0]
    return {titulo:f"La película {titulo} fue estrenada en el año {año} con un score/popularidad de {score}."}

#def votos_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando
# como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.
# Ejemplo de retorno:
# La película X fue estrenada en el año X. La misma cuenta con un total de X valoraciones, con un promedio de X

@app.get("/votos_titulo/{titulo}")
async def votos_titulo(titulo: str):
    titulo = str(titulo).strip().lower()
    df_movies['title'] = df_movies['title'].str.lower()
    df_unico = df_movies.drop_duplicates(subset=['title','id_credit'])
    filmacion = df_unico[df_unico['title'] == titulo]
    try:
        if filmacion['vote_count'].values[0] < 2000:
            return {f"la pelicula {titulo} no supera las 2000 votaciones necesarias para entrar en este ranking":titulo}
        if filmacion.empty:
            return {f"No se encontró información sobre la filmación:'":titulo}
        title = filmacion['title'].values[0]
        año = filmacion['release_year'].values[0]
        votos = filmacion['vote_count'].values[0]
        promedio = filmacion['vote_average'].values[0]
        return {f"la pelicula {title} fue estrenada en el año {año}. La misma cuenta con un total de {votos} valoraciones, con un promedio de {promedio}":title}
    except:
        return {"No se encontró información sobre la filmación:":titulo}

#def get_actor( nombre_actor ): Se ingresa el nombre de un actor que se encuentre dentro
# de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y el promedio de retorno. La definición no deberá considerar directores.
# Ejemplo de retorno: El actor X ha participado de X cantidad de filmaciones,
#                      el mismo ha conseguido un retorno de X con un promedio de X por filmación
#uvicorn main:app --reload

@app.get("/get_actor/{actor}")
async def get_actor(actor: str):
    datos_cast['name'] = datos_cast['name'].str.lower()
    actor = actor.strip().lower()
    df_cast_filtrado = datos_cast[datos_cast['name']== actor]
    if not df_cast_filtrado.empty:
        df_movies_filtrado = df_movies.merge(df_cast_filtrado[['id_credit','name']],how='inner',on='id_credit')
        cantidad_peliculas = df_movies_filtrado.shape[0]
        retorno_total = df_movies_filtrado['return'].sum()
        promedio_retorno = retorno_total/cantidad_peliculas
        return {f"El actor {actor} ha participado de {cantidad_peliculas} filmaciones, el mismo ha conseguido un retorno de {retorno_total} con un promedio de {promedio_retorno:.2f} por filmación.": actor}
    else:
        return {f"El actor no se encuentra en el sistema ":actor}

#def get_director( nombre_director ): Se ingresa el nombre de un director que se
# encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través
# del retorno. Además, deberá devolver el nombre de cada película con la
# fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

#uvicorn main:app --reload

@app.get("/get_director/{director}")
async def get_director(director: str):
    datos_crew['job'] = datos_crew['job'].str.lower()
    datos_crew['name'] = datos_crew['name'].str.lower()
    director = director.strip().lower()
    director_movies = datos_crew[(datos_crew['job'] == 'director') & (datos_crew['name'] == director)]
    if director_movies.empty:
        return {"El director no se encuentra en el sistema": director}
    movie_ids = director_movies['id_credit'].unique()
    director_movies_info = df_movies[df_movies['id_credit'].isin(movie_ids)]
    total_return = director_movies_info['return'].sum()
    #average_return = director_movies_info['return'].mean()
    #peliculas_director = director_movies_info[['title', 'release_date', 'return', 'budget', 'revenue']]
    director_dic = {'director': director,'total_return': total_return,'peliculas': []}
    for _,row in director_movies_info.iterrows():
        pelicula_dic = {'title': row['title'],
            'release_date': row['release_date'],
            'return': row['return'],
            'budget': row['budget'],
            'revenue': row['revenue']}
        director_dic['peliculas'].append(pelicula_dic)
    return director_dic
    #return {"exito": total_return,
     #       "peliculas": peliculas_director}

nltk.download('stopwords')


stopwords = nltk.corpus.stopwords.words('english')
lemmatizer = WordNetLemmatizer()
### Funcion para convertir los generos de lista de listas a strings separados por ","
def juntar_listas(lista):
  if isinstance(lista, (list)):
    return ','.join([str(elemento[1]) for elemento in lista])

### funcion preprocesamiento para tokenizar(lematizar) el texto
def preprocesamiento(texto):
    tokens = word_tokenize(texto.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in stopwords]
    return ' '.join(tokens)

### funcion contiene_genero para verificar si contiene un genero o no
def contiene_genero(genres, genres_to_filter):
    genres_list = [genre.strip() for genre in genres.split(',')]
    return any(genre in genres_list for genre in genres_to_filter)


df_movies['generos'] = df_movies['genres'].apply(juntar_listas)
df_movies['title'] = df_movies['title'].str.lower()
df_movies = df_movies.dropna(axis=0,subset=['overview'])
### Funcion recomendacion(titulo): Se ingresa el nombre de una película y te recomienda
### las similares en una lista de 5 valores.
#uvicorn main:app --reload
@app.get("/recomendacion/{titulo}")
async def recomendacion(titulo: str):
    titulo =str(titulo).strip().lower()
    try:
        linea = df_movies[df_movies['title']== titulo]
        generos = linea['generos']
        generos_list = generos.str.split(',')
        generos_list = list(generos_list.values)
        df_filtrado = df_movies[df_movies['generos'].apply(lambda x: contiene_genero(x, generos_list[0]))]
        df_filtrado.drop_duplicates(subset=['title'],inplace=True)
        #se resetea el indice porque creamos el dataframe filtrado por los generos
        df_filtrado = df_filtrado.reset_index()
        df_filtrado.drop(columns=['index'],inplace=True)
        # se resetea el indice porque creamos el dataframe filtrado por los generos
        indices = pd.Series(df_filtrado.index,index=df_filtrado['title']) #Crear los indices del dataframe
        df_filtrado['processed_overview'] = df_filtrado['overview'].apply(preprocesamiento) #se tokeniza el texto
        # creación de matriz TF-IDF
        # max_df = 0.5 equivale a eliminar del modelo los términos que aparecen en más del 50% de los documentos o peliculas.
        # es decir, mientras mas reduzca el parametro "max_df" mayor sera la
        # importancia relativa de las palabras menos frecuentes
        tfidf = TfidfVectorizer(max_df=0.5, max_features=25, sublinear_tf=True)
        # por el hecho del costo computacional que genera esta vectorizacion de palabras se usara max_features=50
        tfidf_matrix = tfidf.fit_transform(df_filtrado['processed_overview'])
        # Calcular la similitud del coseno
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        idx = indices[titulo]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        movie_indices = [i[0] for i in sim_scores]
        lista_top = df_movies['title'].iloc[movie_indices].tolist()
        return {f'Las recomendaciones para {titulo} son: ':lista_top}
    except:
        return{"la pelicula no se encuentra en el sistema:":titulo}

