"""
Módulo 'main' que es el módulo principal del programa.

Autor: Alberto Paramio Galisteo
Licencia: MIT

Este módulo desarrolla ordenadamente las respuestas a las siguientes preguntas:

Ejercicio 1: Descompresión y lectura de ficheros.

Ejercicio 1.1.
- Implementad una función que descomprima ficheros en formato zip y tar.gz.
  La función recibirá como inputs la ruta con el nombre del fichero que se
  quiere descomprimir. La función detectará automáticamente si el fichero
  está comprimido en zip o en tar.gz y mostrará un mensaje de error cuando el
  fichero sea de otro tipo. Utilizad esta función para descomprimir el fichero
  TMDB.zip.

Ejercicio 1.2.
- Implementad una función que lea los csv y los integre en un único dataframe
  utilizando como clave la columna "id" utilizando la librería **pandas**.
  Obtened el tiempo de procesamiento.

Ejercicio 1.3.
- Implementad una función que lea los csv y los integre en un único
  diccionario utilizando como clave la columna "id" utilizando la librería
  **csv**. Obtened el tiempo de procesamiento.

Ejercicio 1.4.
- ¿Qué diferencias se observan en la lectura de los ficheros siguiendo ambos
  métodos? ¿Si los ficheros tuvieran un tamaño de 10GB qué método sería más
  rápido? Justificad la respuesta.

Ejercicio 2: Procesamiento de datos.

Ejercicio 2.1.
- Añadid una variable air_days al dataframe que consista en el número de días
  que una serie ha estado en emisión. Mostrad por pantalla los 10 registros
  del dataset que más días han estado en emisión.

Ejercicio 2.2.
- Cread un diccionario ordenado cuya clave será el nombre de la serie (name)
  y cuyo valor será la dirección web completa de su poster (homepage y
  poster_path). En caso de que homepage o poster_path tengan el valor NaN o "",
  el valor será el string “NOT AVAILABLE”. Mostrad por pantalla los primeros
  5  registros del diccionario.

Ejercicio 3: Filtrado de datos.

Ejercicio 3.1.
- Obtened y mostrad por pantalla los nombres de las series cuyo idioma
  original (original_language) sea el inglés y en cuyo resumen (overview)
  aparezcan las palabras “mystery” o “crime”, sin tener en cuenta mayúsculas
  ni minúsculas.

Ejercicio 3.2.
- Obtened una lista de las series que han empezado en 2023 y han sido
  canceladas. Mostrad por pantalla los primeros 20 elementos de esta lista.

Ejercicio 3.3.
- Obtened un dataframe con los nombres, los nombres originales, las plataformas
 de emisión y las empresas productoras de todas las series cuyo idioma (
 variable languages) sea el japonés y mostrar los primeros 20 registros por
 pantalla. Nota: tened en cuenta que consideramos series en japonés también
 aquellas que tengan idiomas adicionales, por ejemplo, un registro con idioma
 “en, ja, ko” se incluiría.

Ejercicio 4: Análisis gráfico.

Ejercicio 4.1.
- Mostrad en un gráfico de barras el número de series por año de inicio.

Ejercicio 4.2.
- Construid un gráfico de líneas que muestre el número de series de cada
  categoría de la variable “type” producidas en cada década desde 1940. ¿Qué
  cambios de tendencia se observan?

Ejercicio 4.3.
- Obtened el número de series por género y mostrad el porcentaje respecto al
  total en un gráfico circular. Los géneros que representen menos del 1% del
  total se incluirán en la categoría "Other". Tened en cuenta que una serie
  que tenga más de un género deberá incluirse en todas las categorías en que
  esté clasificada y que las series con el campo "genres" vacío no se incluyen.

Ejercicio 5: Conclusiones.
- Redactad un breve informe que recopile las conclusiones obtenidas en el
  análisis realizado.
"""

# Importamos librerías y módulos de interés
import matplotlib.pyplot as plt
import utils

# Ejercicio 1.1.
print('Ejercicio 1.1.')
ruta = 'data/TMDB.zip'
utils.descomprimir_archivo(ruta)
print('')

# Ejercicio 1.2.
print('Ejercicio 1.2.')
dataframes = utils.integrar_csv_en_dataframe('data')
df = dataframes[0]
print(f'El tiempo de ejecución del dataframe ha sido de {dataframes[1]} '
      f'segundos\n')

# Ejercicio 1.3.
print('Ejercicio 1.3.')
diccionarios_filas = utils.integrar_csv_en_dict_por_fila('data')
print(f'El tiempo de procesamiento del diccionario estructurado por filas es '
      f'de {diccionarios_filas[1]} segundos.')
diccionarios_columnas = utils.integrar_csv_en_dict_por_columna('data')
print(f'El tiempo de procesamiento del diccionario estructurado por columnas '
      f'es de {diccionarios_columnas[1]} segundos.\n')


# Ejercicio 1.4.
print('Ejercicio 1.4.')
try:
    with open("docs/Ejercicio_1.4.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no se encuentra.")
except IOError as e:
    print(f"Error de E/S: {e}")


# Ejercicio 2.1.
print('\nEjercicio 2.1.')
df_time_on_air = utils.agregar_columna_time_on_air(dataframes[0])
df_filtrado = df_time_on_air.nlargest(10, 'time_on_air')
print(df_filtrado)

# Ejercicio 2.2.
print('\nEjercicio 2.2.')
diccionario_ordenado = utils.crear_diccionario_ordenado(df)
utils.mostrar_cinco_primeros(diccionario_ordenado)

# Ejercicio 3.1.
print('\nEjercicio 3.1.')
filtro1 = ((df['original_language'].str.lower() == 'en') &
           (df['overview'].str.lower().str.contains('mystery|crime')))
series_filtradas1 = df.loc[filtro1, 'name']
print(series_filtradas1)

# Ejercicio 3.2.
print('\nEjercicio 3.2.')
filtro2 = (df['first_air_date'].dt.year == 2023) & (df['status'] == 'Canceled')
series_filtradas2 = df.loc[filtro2, 'name'].tolist()[:20]
print(series_filtradas2)

# Ejercicio 3.3.
print('\nEjercicio 3.3.')
filtro3 = df['languages'].str.contains('ja', case=False, na=False)
columns = ['name', 'original_name', 'networks', 'production_companies']
df_resultado = df.loc[filtro3, columns].head(20)
print(df_resultado)

# Ejercicio 4.1.
print('\nEjercicio 4.1.')
conteo_series_por_anio = (df['first_air_date'].
                          dt.year.value_counts().sort_index())
plt.bar(conteo_series_por_anio.index, conteo_series_por_anio.values,
        color='skyblue')
plt.xlabel('Año')
plt.ylabel('Número de Series')
plt.title('Número de Series por Año')
plt.show()
print('Ejecutado correctamente.\n')

# Ejercicio 4.2.
print('Ejercicio 4.2.')
df['decade'] = (df['first_air_date'].dt.year // 10) * 10
# Filtrar desde 1940
df = df[df['first_air_date'].dt.year >= 1940].copy()
# Contar el número de series por tipo y década
conteo_series_por_tipo_y_decada = (df.groupby(['decade', 'type'])
                                   .size().unstack().fillna(0))
# Mostrar el gráfico de líneas
conteo_series_por_tipo_y_decada.plot(kind='line', marker='o', figsize=(10, 6))
plt.xlabel('Década')
plt.ylabel('Número de Series')
plt.title('Número de Series por Década y Tipo')
plt.legend(title='Tipo de Serie', loc='upper left')
plt.show()
print('Ejecutado correctamente.\n')

# Ejercicio 4.3.
print('Ejercicio 4.3.')
# Dividir las cadenas en la columna 'genres' y apilar los géneros en un
# nuevo DataFrame
genres_df = (df['genres'].str.split(', ', expand=True).stack()
             .reset_index(level=1, drop=True).rename('genre'))
# Unir el nuevo DataFrame con el original
df_genres = df.drop('genres', axis=1).join(genres_df)
# Contar el número de series por género
conteo_series_por_genero = df_genres['genre'].value_counts()
# Calcular el porcentaje respecto al total
porcentaje_series_por_genero = conteo_series_por_genero / len(df_genres) * 100
# Agrupar géneros que representan menos del 1% en la categoría 'Other'
umbral = 1
otros_generos = porcentaje_series_por_genero[porcentaje_series_por_genero
                                             < umbral].index
porcentaje_series_por_genero['Other'] \
    = porcentaje_series_por_genero[otros_generos].sum()
porcentaje_series_por_genero = porcentaje_series_por_genero.drop(otros_generos)
# Mostrar el gráfico circular
plt.figure(figsize=(8, 8))
plt.pie(porcentaje_series_por_genero, labels=porcentaje_series_por_genero.index,
        autopct='%1.1f%%', startangle=140)
plt.title('Porcentaje de Series por Género')
plt.show()
print('Ejecutado correctamente.')

# Ejercicio 5
print('\nEjercicio 5')
try:
    with open("docs/Ejercicio_5.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no se encuentra.")
except IOError as e:
    print(f"Error de E/S: {e}")
