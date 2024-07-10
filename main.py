
#levantar servidor uvicorn: uvicorn main:app --reload
### Librerias necesarias
from fastapi import FastAPI
import pandas as pd
import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = FastAPI()
#lectura de los datos
df_movies = pd.read_parquet('data/df_movies_parquet.parquet',engine='pyarrow',columns=['title', 'release_year', 'popularity', 'id','release_date','overview_tokenizado','genres','vote_count','vote_average','return','budget','revenue','generos'])
datos_crew = pd.read_parquet('data/df_crew_parquet.parquet',engine='pyarrow',columns=['job', 'name','id_credit'])
datos_cast = pd.read_parquet('data/df_cast_parquet.parquet',engine='pyarrow',columns=['name','id_credit'])
#transformacion de los datos
df_movies['title'] = df_movies['title'].str.lower()
df_movies = df_movies.dropna(axis=0,subset=['overview_tokenizado'])
df_movies = df_movies.drop_duplicates(subset=['title'])
#df_movies['genres'] = df_movies['genres'].apply(json.loads)

df_movies = df_movies.rename(columns={'id': 'id_credit'})

#ruta local: http://127.0.0.1:8000
@app.get("/")
async def root():
    return "Raiz de la API"

@app.get("/cantidad_filmaciones_mes/{mes}")
async def cantidad_filmaciones_mes(mes: str):
    """
    Se ingresa un mes en idioma Español. Debe devolver la cantidad
    de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.
    Basado en las primeras 6000 lineas de la data general
    ej: agosto
    """
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


@app.get("/cantidad_filmaciones_dia/{dia}")
async def cantidad_filmaciones_dia(dia: str):
    """_summary_
    Se ingresa un día en idioma Español. Funcion para cantidad de filmaciones por dia
    ej: Lunes o lunes
    Basado en las primeras 6000 lineas de la data general
    """
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


@app.get("/score_titulo/{titulo}")
async def score_titulo(titulo: str):
    """_summary_
    def score_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando
    como respuesta el título, el año de estreno y el score.
    Basado en las primeras 6000 lineas de la data general
    ej: Toy Story
    """
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


@app.get("/votos_titulo/{titulo}")
async def votos_titulo(titulo: str):
    """
    def votos_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando
    como respuesta el título, la cantidad de votos y el valor promedio de las votaciones.
    Basado en las primeras 6000 lineas de la data general
    ej: Toy Story
    """
    titulo = str(titulo).strip().lower()
    filmacion = df_movies[df_movies['title'] == titulo]
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


@app.get("/get_actor/{actor}")
async def get_actor(actor: str):
    """
    def get_actor( nombre_actor ): Se ingresa el nombre de un actor que se encuentre dentro
    de un dataset debiendo devolver el éxito del mismo medido a través del retorno.
    Basado en las primeras 6000 lineas de la data general
    ej: Tom Hanks
    """
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
    
    
@app.get("/get_director/{director}")
async def get_director(director: str):
    """
    def get_director( nombre_director ): Se ingresa el nombre de un director que se
    encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través
    del retorno.
    Basado en las primeras 6000 lineas de la data general
    ej: John Lasseter - Tom Hanks
    """ 
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



from Funciones import contiene_genero

df_movies_recortado = df_movies[:6000]
#df_movies = df_movies[:6000]
@app.get("/recomendacion/{titulo}")
async def recomendacion(titulo: str):
    """
    Funcion recomendacion(titulo): Se ingresa el nombre de una película y te recomienda
    las similares en una lista de 5 valores.
    Esta funcion debido al limitante de render, se limita solo a recomendar en base a una octava parte
    de los datos(primeras 6000 instancias)
    Ejemplos: Toy Story - Tom and Huck - Sudden Death
    """
    
    titulo = str(titulo).strip().lower()
    try:
        linea = df_movies_recortado[df_movies_recortado['title'] == titulo] # Obtener la instancia del titulo
        generos = linea['generos'] # variable con los generos de la pelicula
        generos_list = generos.str.split(',') # usamos .split() para poder convertir a lista
        generos_list = list(generos_list.values)
        print(generos_list)
        # filtramos las peliculas que compartan al menos 1 genero con la pelicula pasada como parametro
        df_filtrado = df_movies_recortado[df_movies_recortado['generos'].apply(lambda x: contiene_genero(x, generos_list[0]))]
        df_filtrado.drop_duplicates(subset=['title'], inplace=True) #drop de duplicados
        # se resetea el indice porque creamos el dataframe filtrado por los generos
        df_filtrado = df_filtrado.reset_index()
        df_filtrado.drop(columns=['index'], inplace=True)
        indices = pd.Series(df_filtrado.index, index=df_filtrado['title'])
        # CountVectorizer
        count = CountVectorizer(max_df=0.1, max_features=35) # instanciamos el CountVectorizer
        # max_df= 0.1 y 35 palabras
        # transformamos la data ya lematizada.
        count_matrix = count.fit_transform(df_filtrado['overview_tokenizado']) 
        # Calcular la similitud del coseno
        cosine_sim = linear_kernel(count_matrix, count_matrix)
        idx = indices[titulo]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True) #reordenar el array
        sim_scores = sim_scores[1:6] # obtengo los 5 mejores
        movie_indices = [i[0] for i in sim_scores]
        lista_top = df_movies_recortado['title'].iloc[movie_indices].tolist()
        return {f'Las recomendaciones para {titulo} son: ': lista_top}
    except:
        return {"la pelicula no se encuentra en el sistema:": titulo}
