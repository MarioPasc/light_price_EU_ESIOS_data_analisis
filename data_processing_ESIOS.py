import json
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


#region Funciones

def df_pais(df):
    '''
    
    Parameters
    ----------
    df : TYPE. pd.DataFrame
        DESCRIPTION. Dataframe con los paises, precio de la luz por horas y hora

    Returns
    -------
    dict_df : TYPE. pd.DataFrame
        DESCRIPTION. Devuelve un diccionario tal que la clave es el pais y el valor es el dataframe con los datos asociados a ese pais

    '''
    dict_df = {}
    for geo_name, df_group in df.groupby('geo_name'):
        dict_df[geo_name] = df_group.copy()
    return dict_df

def r_atip_val(df, val):
    '''

    Parameters
    ----------
    df : TYPE. pd.DataFrame
        DESCRIPTION. Dataframe con la columna 'value'
    val : TYPE. int16, int32, int64, ...
        DESCRIPTION. Valor mínimo

    Returns
    -------
    df : TYPE. pd.DataFrame
        DESCRIPTION. Devuelve el dataframe eliminando valores atípicos

    '''
    df = df.drop(df[df['value']<val].index)
    return df

def create_df(lista):
    '''

    Parameters
    ----------
    lista : TYPE. list
        DESCRIPTION. Lista de tuplas de valores [avg_price, day]

    Returns
    -------
    df : TYPE. pd.DataFrame
        DESCRIPTION. DataFrame con los datos pasados en la lista

    '''
    df = pd.DataFrame(lista, columns=['avg_price', 'day'])
    df = df.sort_values(by='day')
    df['avg_price'] = df['avg_price'].apply(func=lambda x: x/1000)
    return df

#endregion

#region Variables necesarias

input_folder = "D:\OneDrive\Documentos\datasets\precioluz_json"
columns = ['value', 'datetime', 'geo_id', 'geo_name']
dict_avg = {}

#endregion

#region Apertura de archivo e inicio del preprocesamiento
datalist = os.listdir(input_folder)
datalist.sort(key=lambda x: int(x.split('-')[1]))
for file in datalist:

    complete_rute = os.path.join(input_folder, file)

    if os.path.exists(complete_rute):
        try:
            with open(complete_rute, "r") as archivo_json:
                data_file = json.load(archivo_json)
        except OSError:
            print(f'File {complete_rute} not found / corrupt')
    else:
        print(f'File in {complete_rute} not found')

    #Nos quedamos solo con los valores del parámetros indicator
    data_file = data_file['indicator']['values']
    
    #Filtramos los datos solo para quedarnos con los valores especificados en columns 
    filtered_data = []
    for val in data_file:
        filtered_data.append([val[col] for col in columns])
    #Creamos un DataFrame con los datos del archivo json actual
    df_temp = pd.DataFrame(data=filtered_data, columns=columns)
    #Creamos un diccionario cuya clave es el pais y valor es el dataframe con los datos asociados a ese pais 
    dict_paises = df_pais(df_temp)
    
    for key in dict_paises.keys():
        #Eliminamos dos columnas que no aportan información
        dict_paises[key] = dict_paises[key].drop('geo_id', axis=1).drop('geo_name', axis=1)
        #Eliminamos los valores atípicos que haya podido proporcionar la API
        dict_paises[key] = r_atip_val(dict_paises[key], -10)
        #Separamos entre valores y fecha para poder manipular los datos mejor
        valores, fecha = np.array(dict_paises[key].value), np.array(dict_paises[key].datetime)
        #Creamos una lista de dos valores, el primero es el precio medio de la luz para ese dia, y el segundo es el dia
        tupla = [np.mean(np.array(valores)).round(3), (fecha[0][8] + fecha[0][9])]
        if key not in dict_avg.keys():
            dict_avg[key] = [tupla]
        else:
            dict_avg[key].append(tupla)  
        
 #endregion
 
 #region Representacion
 
for key in dict_avg.keys():
    #Creamos un df con los datos de la lista
    avg_df = create_df(dict_avg.get(key))
    #Visualizamos los datos en diferentes gráficas
    plt.scatter(x=avg_df['day'], y=avg_df['avg_price'], color='red')
    plt.plot(avg_df['day'], avg_df['avg_price'], color='blue')
    plt.legend(['Avg price for that day', 'Evolution of price'])
    plt.title(f'Precio para {key}')
    plt.xlabel('Día del mes de Julio')
    plt.ylabel('SPOT (€/kW) ')
    plt.savefig(f'D:\OneDrive\Documentos\imagenespython\precioluz\precioluz-{key}.png')
    plt.show() 
 
 #endregion
