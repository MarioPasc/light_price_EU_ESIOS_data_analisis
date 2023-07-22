import urllib.request as urlreq
from datetime import datetime, timedelta
import json
import os

#region Funciones


def get_json(indicator, start_str, end_str, headers_req):
    """
    :param indicator: Indicador del Mercado SPOT Diario
    :param start_str: Start date
    :param end_str: End date
    :param headers_req: Headers de la petición a la API
    :return:
    """
    url = 'https://api.esios.ree.es/indicators/' + indicator + '?start_date=' + start_str + '&end_date=' + end_str
    req = urlreq.Request(url, headers=headers_req)
    with urlreq.urlopen(req) as response_req:
        try:
            json_data = response_req.read().decode('utf-8')
        except:
            json_data = response_req.readall().decode('utf-8')
    return json.loads(json_data)


def get_indicators(headers_req):
    """
    :param headers_req: Headers de la solicitud a la API
    :return:
    """
    url = 'https://api.esios.ree.es/offer_indicators'
    req = urlreq.Request(url, headers=headers_req)
    with urlreq.urlopen(req) as response:
        try:
            json_data = response.read().decode('utf-8')
        except:
            json_data = response.readall().decode('utf-8')
    return json.loads(json_data)


def get_file_name(num):
    return f'data-{num}-ESIOS.json'

#endregion


# region  Datos propios de la solicitud
TOKEN = "015e8781f5ece93118fff662ab82dcfb41e3c001d8e63538dadb4c99256a3291"
headers = {
    'Accept': 'application/json; application/vnd.esios-api-v1+json',
    'Content-Type': 'application/json',
    'Host': 'api.esios.ree.es',
    'x-api-key': f'{TOKEN}',
    'Cookie': ''
}
# endregion

#region Main


'''
El segundo numero de la iteración (en este caso, 23) es el día máximo del mes de julio para el que se solicita la información
La información también puede solicitarse de otros meses cambiando el mes de 7 a otro, incluso el año, un ejemplo sería:
    
for i in range(1, 32):
    start_date = datetime(2020, 9, i).strftime('%Y-%m-%dT%H:%M:%S')
    end_date = datetime(2020, 9, i+1).strftime('%Y-%m-%dT%H:%M:%S')
'''
for i in range(1, 23):
    start_date = datetime(2023, 7, i).strftime('%Y-%m-%dT%H:%M:%S')
    end_date = datetime(2023, 7, i+1).strftime('%Y-%m-%dT%H:%M:%S')
    print(start_date, end_date)
    res = get_json("600", start_date, end_date, headers)

    archivo = get_file_name(i)
    directorio = 'D:\OneDrive\Documentos\datasets\precioluz_json'
    try:
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        else:
            ruta_completa = os.path.join(directorio, archivo)
            with open(ruta_completa, "w") as archivo_json:
                json.dump(res, archivo_json)
    except json.JSONDecodeError:
        print(f'Error de decodificacion JSON para archivo {archivo}')


#endregion
