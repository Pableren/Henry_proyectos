#libreria de funciones:
import pandas as pd
import numpy as np
import re
import json
import ast
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

#df = pd.read_csv('movies.csv',parse_dates=['release_date'])
#df_unico = df.drop_duplicates(subset=['id', 'release_date'])
#cantidad_peliculas_mes = df_unico['release_date'].dt.month.value_counts()
#cantidad_peliculas_mes.sort_index(inplace=True)
#cantidad_peliculas = df_movies[]

#df_unico = df_movi.drop_duplicates(subset=['id', 'release_date'])
#cantidad_peliculas_mes = df_unico['release_date'].dt.month.value_counts()
#cantidad_peliculas_mes.sort_index(inplace=True)


### Funcion para convertir los generos de lista de listas a strings separados por ","
def juntar_listas(lista):
  if isinstance(lista, (list)):
    return ','.join([str(elemento[1]) for elemento in lista])
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
stopwords = nltk.corpus.stopwords.words('english')
lemmatizer = WordNetLemmatizer()
### funcion preprocesamiento para tokenizar(lematizar) el texto
def preprocesamiento(texto):
    tokens = word_tokenize(texto.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in stopwords]
    return ' '.join(tokens)

### funcion contiene_genero para verificar si contiene un genero o no
def contiene_genero(genres, genres_to_filter):
    genres_list = [genre.strip() for genre in genres.split(',')]
    return any(genre in genres_list for genre in genres_to_filter)



###############
# Funciones para convertir datos
# convertir diccionarios a listas
def convertir_dicc_to_list(ser):
    lis = []
    for x in ser:
        lista = []
        try:
            if isinstance(x,(str,dict)):
                linea = ast.literal_eval(x) if isinstance(x, str) else x
                if isinstance(linea,(dict)):
                    for clave, valor in linea.items():
                        lista.append([clave,valor])
                else:
                    pass
                lis.append(lista)
            else:
                #lis.append(list())
                lis.append(np.nan)
                pass
        except (ValueError, SyntaxError) as e:
            print(f"Ocurrió una excepción: {e}")
    return lis
## funcion para convertir listas a diccionarios
def convertir_list_to_dicct(ser):
    lista = []
    try:
        for x in ser:
            lis = []
            linea = ast.literal_eval(x)
            for dic in linea:
                lis.append(list(dic.values()))
            lista.append(lis)
        return lista
    except:
        return lista
# Funcion para convertir string a listas
def convertir_str_list(ser):
    lista = []
    try:
        for x in ser:
            lis = []
            linea = ast.literal_eval(x)
            for y in linea:
                for clave, valor in y.items():
                    lis.append([clave,valor])
            lista.append(lis)
        return lista
    except:
        return lista

"""
from sklearn.feature_extraction.text import HashingVectorizer


@app.get("/recomendacionHV/{titulo}")
async def recomendacionHV(titulo: str):
    titulo = str(titulo).strip().lower()
    try:
        linea = df_movies[df_movies['title'] == titulo]
        generos = linea['generos']
        generos_list = generos.str.split(',')
        generos_list = list(generos_list.values)
        df_filtrado = df_movies[df_movies['generos'].apply(lambda x: contiene_genero(x, generos_list[0]))]
        df_filtrado.drop_duplicates(subset=['title'], inplace=True)
        df_filtrado = df_filtrado.reset_index()
        df_filtrado.drop(columns=['index'], inplace=True)
        indices = pd.Series(df_filtrado.index, index=df_filtrado['title'])
        #df_filtrado['processed_overview'] = df_filtrado['overview'].apply(preprocesamiento)

        # Usando HashingVectorizer
        hashing = HashingVectorizer(n_features=10, alternate_sign=False)
        hashing_matrix = hashing.fit_transform(df_filtrado['processed_overview'])

        # Calcular la similitud del coseno
        cosine_sim = linear_kernel(hashing_matrix, hashing_matrix)
        idx = indices[titulo]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        movie_indices = [i[0] for i in sim_scores]
        lista_top = df_movies['title'].iloc[movie_indices].tolist()
        return {f'Las recomendaciones para {titulo} son: ': lista_top}
    except:
        return {"la pelicula no se encuentra en el sistema:": titulo}
    
    
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
        tfidf = TfidfVectorizer(max_df=0.2, max_features=25, sublinear_tf=True)
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

"""