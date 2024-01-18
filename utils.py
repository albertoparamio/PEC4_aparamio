"""
Módulo 'utils' con funciones de utilidad para procesar archivos y datos.

Autor: Alberto Paramio Galisteo
Licencia: MIT

Funciones:
- descomprimir_archivo(ruta_archivo: str) -> None:
  Descomprime un archivo en formato zip o tar.gz según su extensión.

- descomprimir_zip(ruta_archivo: str) -> None:
  Descomprime un archivo en formato zip.

- descomprimir_tar_gz(ruta_archivo: str) -> None:
  Descomprime un archivo en formato tar.gz.

- integrar_csv_en_dataframe(ruta: str) -> Tuple[pd.DataFrame, float]:
  Lee todos los archivos CSV de la ruta dada y los integra en un único
  DataFrame utilizando el proceso especificado.

- integrar_csv_en_dict_por_fila(ruta: str) -> Union[Dict[str, Dict[str, any]],
  float]:
  Lee todos los archivos CSV de la ruta dada y los integra en un diccionario
  utilizando el proceso especificado, agrupando por filas.

- integrar_csv_en_dict_por_columna(ruta: str) -> Union[Dict[str, List[any]],
  float]:
  Lee todos los archivos CSV de la ruta dada y los integra en un diccionario
  utilizando el proceso especificado, agrupando por columnas.

- mostrar_cinco_primeros(diccionario: Dict[str, Dict[str, Any]]) -> None:
  Muestra los cinco primeros registros de un diccionario.

- agregar_columna_time_on_air(dataframe: pd.DataFrame) -> pd.DataFrame:
  Agrega una columna llamada "time_on_air" al DataFrame, calculando la
  diferencia entre las fechas de las columnas "last_air_date" y
  "first_air_date".

- crear_diccionario_ordenado(dataframe) -> dict:
  Crea un diccionario ordenado a partir de un DataFrame con condiciones
  específicas. Las claves son el nombre de la serie ('name'), y los valores
  son diccionarios con 'homepage' y 'poster_path', con valores 'NOT
  AVAILABLE' en caso de NaN o "".
"""

# Importación de módulos de interés
import zipfile
import tarfile
import os
from typing import Tuple, Dict, List, Union, Any
import pandas as pd
import time


def descomprimir_archivo(ruta_archivo: str) -> None:
    """
    Descomprime un archivo en formato zip o tar.gz según su extensión.

    Parámetros:
    - ruta_archivo (str): La ruta del archivo que se desea descomprimir.

    No retorna ningún valor, pero descomprime el archivo en el directorio
    que contiene el archivo original según su extensión y muestra un mensaje
    de éxito. Si la extensión no es compatible o el archivo no existe,
    imprime un mensaje de error.
    """
    if not os.path.exists(ruta_archivo):
        print("Error: El archivo no se encuentra en la ruta suministrada.")
        return

    # Obtener la extensión del archivo
    extension = os.path.splitext(ruta_archivo)[1].lower()

    # Descomprimir según la extensión
    if extension == '.zip':
        descomprimir_zip(ruta_archivo)
    elif extension == '.tar.gz' or extension == '.tgz':
        descomprimir_tar_gz(ruta_archivo)
    else:
        print("Error: Formato de archivo no compatible.")


def descomprimir_zip(ruta_archivo: str) -> None:
    """
    Descomprime un archivo en formato zip.

    Parámetros:
    - ruta_archivo (str): La ruta del archivo que se desea descomprimir.

    No retorna ningún valor, pero descomprime el archivo en el directorio
    que contiene el archivo original y muestra un mensaje de éxito.
    """
    with zipfile.ZipFile(ruta_archivo, 'r') as zip_ref:
        zip_ref.extractall(os.path.dirname(ruta_archivo))
    print(f"Descomprimido correctamente: {ruta_archivo}")


def descomprimir_tar_gz(ruta_archivo: str) -> None:
    """
    Descomprime un archivo en formato tar.gz.

    Parámetros:
    - ruta_archivo (str): La ruta del archivo que se desea descomprimir.

    No retorna ningún valor, pero descomprime el archivo en el directorio
    que contiene el archivo original y muestra un mensaje de éxito.
    """
    with tarfile.open(ruta_archivo, 'r:gz') as tar_ref:
        tar_ref.extractall(os.path.dirname(ruta_archivo))
    print(f"Descomprimido correctamente: {ruta_archivo}")


def integrar_csv_en_dataframe(ruta: str) -> Tuple[pd.DataFrame, float]:
    """
    Lee todos los archivos CSV de la ruta dada y los integra en un único
    DataFrame utilizando el proceso especificado.

    Parámetros:
    - ruta (str): La ruta del directorio que contiene los archivos CSV.

    Retorna:
    - Tuple[pd.DataFrame, float]: Una tupla que contiene el DataFrame resultante
      con la integración de los CSV y el tiempo de ejecución en segundos.
    """
    # Capturar el tiempo de inicio
    inicio_tiempo = time.time()

    # Obtener la lista de archivos CSV en la ruta
    archivos_csv = [archivo for archivo in os.listdir(ruta)
                    if archivo.endswith('.csv')]

    if not archivos_csv:
        print("No se encontraron archivos CSV en la ruta proporcionada.")
        # Retorna un DataFrame vacío y tiempo 0 si no hay archivos CSV
        return pd.DataFrame(), 0.0

    try:
        # Inicializar el DataFrame con el primer archivo CSV
        primer_archivo_csv = os.path.join(ruta, archivos_csv[0])

        # Verificar que el archivo no esté vacío antes de intentar leerlo
        if os.path.getsize(primer_archivo_csv) > 0:
            dataframes = pd.read_csv(primer_archivo_csv)
        else:
            print(f"El archivo CSV {primer_archivo_csv} está vacío.")
            return pd.DataFrame(), 0.0

        # Iterar sobre los archivos CSV restantes
        for archivo_csv in archivos_csv[1:]:
            ruta_completa = os.path.join(ruta, archivo_csv)

            # Verificar que el archivo no esté vacío antes de intentar leerlo
            if os.path.getsize(ruta_completa) > 0:
                df_actual = pd.read_csv(ruta_completa)

                # Fusionar los DataFrames basándonos en la columna "id"
                dataframes = pd.merge(dataframes, df_actual, on='id',
                                      how='outer')
            else:
                print(f"El archivo CSV {ruta_completa} está vacío.")

    except pd.errors.EmptyDataError:
        print("Error: Al menos uno de los archivos CSV está vacío.")
        return pd.DataFrame(), 0.0
    except pd.errors.ParserError:
        print("Error: Problema al analizar al menos uno de los archivos CSV.")
        return pd.DataFrame(), 0.0

    # Capturar el tiempo de finalización
    fin_tiempo = time.time()
    # Calcular el tiempo de ejecución
    tiempo_ejecucion = round((fin_tiempo - inicio_tiempo), 3)

    return dataframes, tiempo_ejecucion


def integrar_csv_en_dict_por_fila(ruta: str) \
        -> Union[Dict[str, Dict[str, any]], float]:
    """
    Lee todos los archivos CSV de la ruta dada y los integra en un diccionario
    utilizando el proceso especificado.

    Parámetros:
    - ruta (str): La ruta del directorio que contiene los archivos CSV.

    Retorna:
    - Union[Dict[str, Dict[str, any]], float]: Un diccionario que contiene los
      registros resultantes con la integración de los CSV, donde cada clave es
      el valor único de la columna "id", y el tiempo de ejecución en segundos.
    """
    # Capturar el tiempo de inicio
    inicio_tiempo = time.time()

    # Obtener la lista de archivos CSV en la ruta
    archivos_csv = [archivo for archivo in os.listdir(ruta)
                    if archivo.endswith('.csv')]

    if not archivos_csv:
        print("No se encontraron archivos CSV en la ruta proporcionada.")
        # Retorna un diccionario vacío y tiempo 0 si no hay archivos CSV
        return {}, 0.0

    # Inicializar el diccionario
    diccionario_resultado = {}

    # Iterar sobre los archivos CSV
    for archivo_csv in archivos_csv:
        ruta_completa = os.path.join(ruta, archivo_csv)

        # Leer el archivo CSV actual
        df_actual = pd.read_csv(ruta_completa)

        # Iterar sobre las filas del DataFrame actual
        for _, fila in df_actual.iterrows():
            # Obtener el valor de la columna "id"
            id_valor = fila["id"]

            # Crear el diccionario para el id si aún no existe
            if id_valor not in diccionario_resultado:
                diccionario_resultado[id_valor] = {}

            # Agregar los pares clave-valor al diccionario del id
            for columna, valor in fila.items():
                diccionario_resultado[id_valor][columna] = valor

    # Capturar el tiempo de finalización
    fin_tiempo = time.time()
    # Calcular el tiempo de ejecución
    tiempo_ejecucion = round((fin_tiempo - inicio_tiempo), 3)

    return diccionario_resultado, tiempo_ejecucion


def integrar_csv_en_dict_por_columna(ruta: str) -> Union[Dict[str, List[any]],
float]:
    """Integra datos de archivos CSV en un diccionario por columna.

    Args:
        ruta (str): La ruta al directorio que contiene los archivos CSV.

    Returns:
        Union[Dict[str, List[any]], float]: Un diccionario que contiene listas
        de valores por columna, o 0.0 si no hay archivos CSV.

    Raises:
        Exception: Se genera una excepción en caso de error durante la
        ejecución.

    Note:
        Esta función recorre todos los archivos CSV en la ruta proporcionada y
        crea un diccionario donde las claves son los nombres de las columnas
        y los valores son  listas con todos los valores de esa columna a lo
        largo de los archivos CSV.

        Si no se encuentran archivos CSV, la función retorna un diccionario
        vacío y 0.0 como tiempo de ejecución.

        Si ocurre algún error durante la ejecución, se imprime un mensaje de
        error y se retorna un diccionario vacío y 0.0 como tiempo de ejecución.
    """
    try:
        # Capturar el tiempo de inicio
        inicio_tiempo = time.time()

        # Obtener la lista de archivos CSV en la ruta
        archivos_csv = [archivo for archivo in os.listdir(ruta)
                        if archivo.endswith('.csv')]

        if not archivos_csv:
            print("No se encontraron archivos CSV en la ruta proporcionada.")
            # Retorna un diccionario vacío y tiempo 0 si no hay archivos CSV
            return {}, 0.0

        # Inicializar el diccionario
        diccionario_resultado = {}

        # Iterar sobre los archivos CSV
        for archivo_csv in archivos_csv:
            ruta_completa = os.path.join(ruta, archivo_csv)

            # Leer el archivo CSV actual solo si no está vacío
            if os.stat(ruta_completa).st_size > 0:
                df_actual = pd.read_csv(ruta_completa)

                # Iterar sobre las columnas del DataFrame actual
                for columna in df_actual.columns:
                    # Crear la lista para la columna si aún no existe
                    if columna not in diccionario_resultado:
                        diccionario_resultado[columna] = []

                    # Agregar los registros de la columna a la lista
                    diccionario_resultado[columna].extend(df_actual[columna].
                                                          tolist())

        # Capturar el tiempo de finalización
        fin_tiempo = time.time()
        # Calcular el tiempo de ejecución
        tiempo_ejecucion = round((fin_tiempo - inicio_tiempo), 3)

        return diccionario_resultado, tiempo_ejecucion

    except Exception as e:
        print(f"Error en la función integrar_csv_en_dict_por_columna: {e}")
        return {}, 0.0


def mostrar_cinco_primeros(diccionario: Dict[str, Dict[str, Any]]) -> None:
    """
    Muestra los cinco primeros registros de un diccionario.

    Parameters:
    - diccionario: Diccionario a mostrar
    """
    for clave, valor in list(diccionario.items())[:5]:
        print(f'{clave}: {valor}')


def agregar_columna_time_on_air(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega una columna llamada "time_on_air" al DataFrame, calculando la
    diferencia entre las fechas de las columnas "last_air_date" y
    "first_air_date".

    Parámetros:
    - dataframe (pd.DataFrame): El DataFrame al que se le agregará la columna.

    Retorna:
    - pd.DataFrame: El DataFrame original con la nueva columna "time_on_air"
    agregada.
    """
    # Verificar si las columnas "last_air_date" y "first_air_date" existen en
    # el DataFrame
    if ('last_air_date' not in dataframe.columns or 'first_air_date'
            not in dataframe.columns):
        print("Error: Las columnas 'last_air_date' y 'first_air_date' deben "
              "estar presentes en el DataFrame.")
        return dataframe

    # Convertir las columnas de fechas al tipo datetime si no lo están
    dataframe['last_air_date'] = pd.to_datetime(dataframe['last_air_date'])
    dataframe['first_air_date'] = pd.to_datetime(dataframe['first_air_date'])

    # Calcular la diferencia entre las fechas y crear la nueva columna
    # "time_on_air"
    dataframe['time_on_air'] = (dataframe['last_air_date']
                                - dataframe['first_air_date'])

    return dataframe


def crear_diccionario_ordenado(dataframe):
    """
    Crea un diccionario ordenado a partir de un DataFrame con las siguientes
    condiciones:
    - Clave: nombre de la serie ('name')
    - Valor: diccionario con 'homepage' y 'poster_path', con valores
      'NOT AVAILABLE' en caso de NaN o ""

    Parameters:
    - dataframe: DataFrame con columnas 'name', 'homepage' y 'poster_path'

    Returns:
    - dict_ordenado: Diccionario ordenado según las especificaciones
    """
    dict_ordenado = {}

    for index, row in dataframe.iterrows():
        name = row['name']
        homepage = row['homepage'] \
            if (pd.notna(row['homepage']) and row['homepage'] != '') \
            else 'NOT AVAILABLE'
        poster_path = row['poster_path'] \
            if (pd.notna(row['poster_path']) and row['poster_path'] != '') \
            else 'NOT AVAILABLE'

        dict_ordenado[name] = {'homepage': homepage, 'poster_path': poster_path}

    return dict_ordenado
