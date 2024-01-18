# PEC4_aparamio

Este proyecto corresponde al resultado de la entrega de la PEC4 (práctica 4) 
de la asignatura Programación para la Ciencia de Datos, realizado por Alberto 
Paramio Galisteo, correspondiente al cuatrimestre de otoño-invierno del curso 
2023-2024 del Máster de Ciencia de Datos de la Universitat Oberta de 
Catalunya (UOC).

## Contenido del Proyecto

- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Tests](#tests)
- [Ejecución de Pruebas](#ejecución-de-pruebas)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Estructura del Proyecto

- PEC4_aparamio/
  - data/ 
    - `__init__.py`  
    - `TMDB.zip`
    - `TMDB_distribution.csv` 
    - `TMDB_info.csv` 
    - `TMDB_overview.csv`
  - docs/ 
    - `__init__.py`
    - `Ejercicio_1.4.txt`
    - `Ejercicio_5.txt`
  - tests/ 
    - `__init__.py`
    - `tests.py`
  - venv/ 
  - `__init__.py`
  - `main.py`
  - `README.md`
  - `requirements.txt`
  - `setup.py`
  - `utils.py`

A continuación, se describe brevemente la estructura de directorios del 
proyecto:
- El directorio principal PEC_aparamio/ recoge los siguientes módulos: main.
  py ejecuta el programa, README.md recoge la información general, 
  requirements.txt recoge todas las librerías que son necesarias tener 
  instaladas para el correcto funcionamiento del programa, y utils.py que 
  recoge todas las funciones que se utilizan en el programa.
- El directorio data/ recoge el archivo comprimido TMDB.zip, junto con los 
  tres archivos resultantes de la descompresión de éste, que son: 
  TMDB_distribution.csv, TMDB_info.csv y TMDB_overview.csv.
- El directorio docs/ recoge dos archivos .txt que corresponden a las 
  respuestas textuales a las preguntas de los ejercicios 1.4. y 5 
  respectivamente.
- El directorio tests/ recoge el archivo tests.py con todos los tests 
  unitarios que se han creado, para comprobar el correcto funcionamiento de 
  varias funciones del archivo utils.py del directorio principal del programa.
- El directorio venv/ que recoge el entorno virtual del programa.

## Requisitos

Asegúrate de tener instaladas las siguientes librerías:

- contourpy==1.2.0
- cycler==0.12.1
- fonttools==4.47.2
- kiwisolver==1.4.5
- matplotlib==3.8.2
- numpy==1.26.3
- packaging==23.2
- pandas==2.1.4
- pillow==10.2.0
- pyparsing==3.1.1
- python-dateutil==2.8.2
- pytz==2023.3.post1
- six==1.16.0
- tzdata==2023.4

Para instalar las dependencias, puedes utilizar el siguiente comando:

```bash
pip install -r requirements.txt
```

## Instalación

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/albertoparamio/PEC4_aparamio
   ```
2. **Acceder al directorio del proyecto:**

  Desde el terminal, sitúate en el directorio del programa PEC4_aparamio 
  mediante el comando **cd**

3. **Instalar dependencias:**

  Asegúrate de tener Python 3.x instalado. Luego crea y activa un entorno 
  virtual.

  Crear un entorno virtual
  ```bash
  python -m venv venv
  ```

  Activar entorno virtual (Linux/Mac)
  ```bash
  source venv/bin/activate
  ```
  
  Activar entorno virtual (Windows)
  ```bash
  venv\Scripts\activate
  ```
  Instalar los requerimientos
  ```bash
  pip install -r requirements.txt
  ```

## Uso

1. **Ejecutar el programa**

  ```bash
  python main.py
  ```
  Esto ejecutará el programa automáticamente.

2. **Desactivar el entorno virtual**

  Si has creado un entorno virtual, desactívalo cuando hayas terminado.
  
  Desactivar entorno virtual (Linux/Mac)
  ```bash
  deactivate
  ```
  Desactivar entorno virtual (Windows)
  ```bash
  venv\Scripts\deactivate
  ```  

## Tests

El Módulo 'tests' contiene clases de prueba para las funciones del módulo 
'utils'.

Las clase de prueba son las siguientes

Clases de prueba:
- TestDescomprimirArchivo(unittest.TestCase):
  Clase de prueba para la función descomprimir_archivo.

- TestIntegrarCSVEnDataFrame(unittest.TestCase):
  Clase de prueba para la función integrar_csv_en_dataframe.

- TestIntegrarCSVEnDictPorColumna(unittest.TestCase):
  Clase de prueba para la función integrar_csv_en_dict_por_columna.

Cada clase de prueba contiene métodos de prueba que verifican el comportamiento
correcto de las funciones correspondientes.

Métodos de configuración y limpieza:
- setUp(self) -> None:
  Configura el entorno antes de cada prueba, creando un directorio temporal
  para las pruebas.

- tearDown(self) -> None:
  Realiza la limpieza después de cada prueba, eliminando el directorio temporal
  después de las pruebas.

Métodos de prueba:
- test_descomprimir_archivo_zip(self) -> None:
  Prueba la descompresión de un archivo ZIP.

- test_descomprimir_archivo_tar_gz(self) -> None:
  Prueba la descompresión de un archivo tar.gz.

- test_descomprimir_archivo_no_existente(self) -> None:
  Prueba la descompresión de un archivo que no existe.

- test_integrar_csv_en_dataframe_archivos_validos(self) -> None:
  Prueba la integración de archivos CSV válidos en un DataFrame.

- test_integrar_csv_en_dataframe_sin_archivos_csv(self) -> None:
  Prueba la función integrar_csv_en_dataframe sin archivos CSV.

- test_integrar_csv_en_dataframe_archivos_vacios(self) -> None:
  Prueba la integración de archivos CSV vacíos en un DataFrame.

- test_integrar_csv_en_dict_por_columna_archivos_validos(self) -> None:
  Prueba la integración de archivos CSV válidos en un diccionario por columna.


## Ejecución de Pruebas

Para asegurarte de que el código funciona correctamente, puedes ejecutar las 
pruebas unitarias incluidas en el proyecto. Asegúrate de tener las dependencias 
de desarrollo instaladas ejecutando:
  ```bash
  pip install -r requirements-dev.txt
  ```
Ejecuta las pruebas ejecutando el módulo tests.py como main.

## Contribución

¡Gracias por considerar contribuir a este proyecto! Si deseas participar, sigue 
estos pasos:

1. Fork el repositorio en GitHub.
2. Crea una rama para tu contribución: `git checkout -b mi-contribucion`.
3. Realiza tus cambios y asegúrate de que las pruebas pasen.
4. Haz commit de tus cambios: `git commit -m "Añade nueva característica"`.
5. Sube tus cambios a tu repositorio fork: `git push origin mi-contribucion`.
6. Abre un Pull Request en el repositorio original.

## Licencia

MIT License

Copyright (c) [2024] [Alberto Paramio Galisteo]

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
de este software y de los archivos de documentación asociados (el "Software"), 
para tratar en el Software sin restricción, incluidos, entre otros, los derechos
utilizar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y / o 
vender copias del Software, y permitir a las personas a quienes se les 
proporciona el Software hacerlo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permisos se incluirán en todos
copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O
IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO EL
LOS TITULARES DE DERECHOS DE AUTOR O LOS TITULARES DE DERECHOS DE AUTOR SERÁN 
RESPONSABLES DE CUALQUIER RECLAMO, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA 
ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, SURGIENDO DE, FUERA DE O EN RELACIÓN 
CON EL SOFTWARE O EL USO O OTROS TRATOS EN EL SOFTWARE.