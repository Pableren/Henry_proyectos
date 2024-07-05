#libreria de funciones:
import pandas as pd
import numpy as np
import re
import json
import ast

df = pd.read_csv('movies.csv',parse_dates=['release_date'])
#df_unico = df.drop_duplicates(subset=['id', 'release_date'])
#cantidad_peliculas_mes = df_unico['release_date'].dt.month.value_counts()
#cantidad_peliculas_mes.sort_index(inplace=True)
#cantidad_peliculas = df_movies[]

#df_unico = df_movi.drop_duplicates(subset=['id', 'release_date'])
#cantidad_peliculas_mes = df_unico['release_date'].dt.month.value_counts()
#cantidad_peliculas_mes.sort_index(inplace=True)

def cantidad_mes(df):
    df_unico = df.drop_duplicates(subset=['id', 'release_date'])
    cantidad_peliculas = df_unico['release_date'].dt.month.value_counts()
    cantidad_peliculas.sort_index(inplace=True)
    return cantidad_peliculas

def cantidad_peliculas_mes(mes: str):
    df_unico = df.drop_duplicates(subset=['id', 'release_date'])
    cantidad_peliculas_mes = df_unico['release_date'].dt.month.value_counts()
    cantidad_peliculas_mes.sort_index(inplace=True)
    if str(mes).lower() == "enero":
        dic = dict({"la cantidad de peliculas estrenadas en enero fue de: ":str(cantidad_peliculas_mes[1])})
        return dic
    elif str(mes).lower() == "febrero":
        dic = dict({"la cantidad de peliculas estrenadas en febrero fue de: ":str(cantidad_peliculas_mes[2])})
        return dic
    elif str(mes).lower()== "marzo":
        dic = dict({"la cantidad de peliculas estrenadas en marzo fue de: ":str(cantidad_peliculas_mes[3])})
        return dic
    elif str(mes).lower()== "abril":
        dic = dict({"la cantidad de peliculas estrenadas en abril fue de: ":str(cantidad_peliculas_mes[4])})
        return dic
    elif str(mes).lower()== "mayo":
        dic = dict({"la cantidad de peliculas estrenadas en mayo fue de: ":str(cantidad_peliculas_mes[5])})
        return dic
    elif str(mes).lower()== "junio":
        dic = dict({"la cantidad de peliculas estrenadas en junio fue de: ":str(cantidad_peliculas_mes[6])})
        return dic
    elif str(mes).lower()== "julio":
        dic = dict({"la cantidad de peliculas estrenadas en julio fue de: ":str(cantidad_peliculas_mes[7])})
        return dic
    elif str(mes).lower()== "agosto":
        dic = dict({"la cantidad de peliculas estrenadas en agosto fue de: ":str(cantidad_peliculas_mes[8])})
        return dic
    elif str(mes).lower()== "septiembre":
        dic = dict({"la cantidad de peliculas estrenadas en septiembre fue de: ":str(cantidad_peliculas_mes[9])})
        return dic
    elif str(mes).lower()== "octubre":
        dic = dict({"la cantidad de peliculas estrenadas en octubre fue de: ":str(cantidad_peliculas_mes[10])})
        return dic
    elif str(mes).lower()== "noviembre":
        dic = dict({"la cantidad de peliculas estrenadas en noviembre fue de: ":str(cantidad_peliculas_mes[11])})
        return dic
    elif str(mes).lower()== "diciembre":
        dic = dict({"la cantidad de peliculas estrenadas en diciembre fue de: ":str(cantidad_peliculas_mes[12])})
        return dic
    else:
        print("valor no valido, use solo letras sin tildes")
        return {}

enero = cantidad_peliculas_mes('enero')
#print(enero)

#def cantidad_filmaciones_dia( Dia ): Se ingresa un día en idioma Español.
# Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.
# Ejemplo de retorno: X cantidad de películas fueron estrenadas en los días X

def cantidad_filmaciones_diaDelMes(dia: int):
    df_unico = df.drop_duplicates(subset=['id', 'release_date'])
    peliculas_dia = df_unico['release_date'].dt.day.value_counts()
    peliculas_dia.sort_index(inplace=True)
    retorno = peliculas_dia[dia]
    return {f"la cantidad de peliculas estrenadas el dia {dia} es:":retorno}
peliculas = cantidad_filmaciones_diaDelMes(30)
#print(peliculas)
#print(type(peliculas))


def cantidad_filmaciones_diaDeSemana(dia: str):
    dia = str(dia).lower()
    #print(dia)
    df_unico = df.drop_duplicates(subset=['id', 'release_date'])
    peliculas_dia = df_unico['release_date'].dt.day_of_week.value_counts()
    peliculas_dia.sort_index(inplace=True)
    indice = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
    peliculas_dia.index = indice
    #print(peliculas_dia)
    #retorno = peliculas_dia[dia]
    if (dia == 'lunes'):
        retorno = {f"la cantidad de peliculas estrenadas un {dia} fueron: ":peliculas_dia[dia]}
        return retorno
    elif (dia == 'martes'):
        retorno = {f"la cantidad de peliculas estrenadas un {dia} fueron: ":peliculas_dia[dia]}
        return retorno
    elif (dia == 'miercoles'):
        retorno = {f"la cantidad de peliculas estrenadas un {dia} fueron: ":peliculas_dia[dia]}
        return retorno
    elif (dia == 'jueves'):
        retorno = {f"la cantidad de peliculas estrenadas un {dia} fueron: ":peliculas_dia[dia]}
        return retorno
    elif (dia == 'viernes'):
        retorno = {f"la cantidad de peliculas estrenadas un {dia} fueron: ":peliculas_dia[dia]}
        return retorno
    elif (dia == 'sabado'):
        retorno = {f"la cantidad de peliculas estrenadas un {dia} fueron: ":peliculas_dia[dia]}
        return retorno
    elif (dia == 'domingo'):
        retorno = {f"la cantidad de peliculas estrenadas un {dia} fueron: ":peliculas_dia[dia]}
        return retorno

peliculas_semana = cantidad_filmaciones_diaDeSemana('domingo')
print(peliculas_semana)
#print(type(peliculas_semana))

#def score_titulo( titulo_de_la_filmación ):
#   Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.
# Ejemplo de retorno: La película X fue estrenada en el año X con un score/popularidad de X
def score_titulo(titulo):
    titulo = str(titulo)
    titulo = titulo.strip()
    df_unico = df.drop_duplicates(subset=['title'])
    #df["id_b"] = df['belong_to_collection'][0]
    print(df['id_b'])
    print(df_unico.columns)
    #df_unico.dropna(inplace=True,axis=0)
    filtrado = df_unico[df_unico['title'] == titulo]
    #print(filtrado)
    if filtrado.empty:
        return f"No se encontró información sobre la filmación '{titulo}'."
    titulo = filtrado['title'].values[0]
    año = filtrado['release_year'].values[0]
    score = filtrado['popularity'].values[0]
    return f"La película {titulo} fue estrenada en el año {año} con un score/popularidad de {score}."
#var = score_titulo(" Toy Story ")
#print(var)


def votos_titulo(titulo):
    titulo = str(titulo).strip().lower()
    df['title'] = df['title'].str.lower()
    #print(titulo_min)
    filmacion = df[df['title'] == titulo]
    try:
        if filmacion['vote_count'].values[0] < 2000:
            return {f"la pelicula {titulo} no supera las 2000 votaciones necesarias para entrar en este ranking":{titulo}}
        if filmacion.empty:
            return {f"No se encontró información sobre la filmación:'":{titulo}}
        titulo = filmacion['title'].values[0]
        año = filmacion['release_year'].values[0]
        votos = filmacion['vote_count'].values[0]
        promedio = filmacion['vote_average'].values[0]
        return {f"la pelicula {titulo} fue estrenada en el año {año}. La misma cuenta con un total de {votos} valoraciones, con un promedio de {promedio}":titulo}
    except:
        return {f"No se encontró información sobre la filmación:'":{titulo}}

"""
df = df.rename(columns={'id': 'id_credit'})
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


async def get_director(director: str):
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


"""

###############
# Funciones para convertir datos

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


