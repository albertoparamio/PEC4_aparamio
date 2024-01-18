"""
Módulo 'tests' con clases de prueba para las funciones del módulo 'utils'.

Autor: Alberto Paramio Galisteo
Licencia: MIT

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

"""

# Importamos librerías y módulos de interés
import unittest
import os
import tempfile
import shutil
import zipfile
import tarfile
import pandas as pd
from ..utils import (descomprimir_archivo, integrar_csv_en_dataframe,
                     integrar_csv_en_dict_por_columna)


class TestDescomprimirArchivo(unittest.TestCase):
    """Clase de prueba para la función descomprimir_archivo."""

    def setUp(self) -> None:
        """Configura el entorno antes de cada prueba.

        Crea un directorio temporal para las pruebas.
        """
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        """Realiza la limpieza después de cada prueba.

        Elimina el directorio temporal después de las pruebas.
        """
        shutil.rmtree(self.temp_dir)

    def test_descomprimir_archivo_zip(self) -> None:
        """Prueba la descompresión de un archivo ZIP.

        - Crea un archivo ZIP de prueba.
        - Llama a la función descomprimir_archivo.
        - Verifica si el archivo se descomprimió correctamente.
        """
        archivo_prueba = os.path.join(self.temp_dir, 'archivo_de_prueba.txt')
        with open(archivo_prueba, 'w') as f:
            f.write("Contenido de prueba")

        zip_file_path = os.path.join(self.temp_dir, 'archivo_prueba.zip')
        with zipfile.ZipFile(zip_file_path, 'w') as zip_ref:
            zip_ref.write(archivo_prueba, 'archivo_de_prueba.txt')

        # Llamar a la función descomprimir_archivo
        descomprimir_archivo(zip_file_path)

        # Verificar si el archivo se descomprimió correctamente
        extracted_file_path = os.path.join(self.temp_dir,
                                           'archivo_de_prueba.txt')
        self.assertTrue(os.path.exists(extracted_file_path),
                        f"Error: No se encontró el archivo descomprimido: "
                        f"{extracted_file_path}")

    def test_descomprimir_archivo_tar_gz(self) -> None:
        """Prueba la descompresión de un archivo tar.gz.

        - Crea un archivo tar.gz de prueba.
        - Llama a la función descomprimir_archivo.
        - Verifica si el archivo se descomprimió correctamente.
        """
        archivo_prueba = os.path.join(self.temp_dir, 'archivo_de_prueba.txt')
        with open(archivo_prueba, 'w') as f:
            f.write("Contenido de prueba")

        tar_gz_file_path = os.path.join(self.temp_dir, 'archivo_prueba.tar.gz')
        with tarfile.open(tar_gz_file_path, 'w:gz') as tar_ref:
            tar_ref.add(archivo_prueba, arcname='archivo_de_prueba.txt')

        # Llamar a la función descomprimir_archivo
        descomprimir_archivo(tar_gz_file_path)

        # Verificar si el archivo se descomprimió correctamente
        extracted_file_path = os.path.join(self.temp_dir,
                                           'archivo_de_prueba.txt')
        self.assertTrue(os.path.exists(extracted_file_path),
                        f"Error: No se encontró el archivo descomprimido: "
                        f"{extracted_file_path}")

    def test_descomprimir_archivo_no_existente(self) -> None:
        """Prueba la descompresión de un archivo que no existe.

        - Intenta descomprimir un archivo que no existe.
        - Verifica que se imprima un mensaje de error.
        """
        archivo_inexistente = os.path.join(self.temp_dir,
                                           'archivo_inexistente.zip')
        descomprimir_archivo(archivo_inexistente)

        # Verificar que se imprima un mensaje de error
        self.assertLogs(level='ERROR')


class TestIntegrarCSVEnDataFrame(unittest.TestCase):
    """Clase de prueba para la función integrar_csv_en_dataframe."""

    def setUp(self) -> None:
        """Configura el entorno antes de cada prueba.

        Crea un directorio temporal para las pruebas.
        """
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        """Realiza la limpieza después de cada prueba.

        Elimina el directorio temporal después de las pruebas.
        """
        shutil.rmtree(self.temp_dir)

    def test_integrar_csv_en_dataframe_archivos_validos(self) -> None:
        """Prueba la integración de archivos CSV válidos en un DataFrame.

        - Crea archivos CSV de prueba.
        - Llama a la función integrar_csv_en_dataframe.
        - Verifica el resultado esperado y el tiempo de ejecución.
        """
        archivo1 = os.path.join(self.temp_dir, 'archivo1.csv')
        archivo2 = os.path.join(self.temp_dir, 'archivo2.csv')

        contenido_csv = "id,valor\n1,100\n2,200\n3,300"

        with open(archivo1, 'w') as f1, open(archivo2, 'w') as f2:
            f1.write(contenido_csv)
            f2.write(contenido_csv)

        # Llamar a la función integrar_csv_en_dataframe
        resultado, tiempo_ejecucion = integrar_csv_en_dataframe(self.temp_dir)

        # Verificar el resultado esperado
        esperado = pd.DataFrame({'id': [1, 2, 3], 'valor_x': [100, 200, 300],
                                 'valor_y': [100, 200, 300]})
        pd.testing.assert_frame_equal(esperado, resultado)

        # Verificar que el tiempo de ejecución sea mayor que 0
        self.assertGreater(tiempo_ejecucion, 0)

    def test_integrar_csv_en_dataframe_sin_archivos_csv(self) -> None:
        """Prueba la función integrar_csv_en_dataframe sin archivos CSV.

        - Llama a la función integrar_csv_en_dataframe sin archivos CSV.
        - Verifica que el resultado sea un DataFrame vacío y el tiempo de
          ejecución sea 0.
        """
        resultado, tiempo_ejecucion = integrar_csv_en_dataframe(self.temp_dir)

        # Verificar que el resultado sea un DataFrame vacío
        self.assertTrue(resultado.empty)

        # Verificar que el tiempo de ejecución sea igual a 0
        self.assertEqual(tiempo_ejecucion, 0)

    def test_integrar_csv_en_dataframe_archivos_vacios(self) -> None:
        """Prueba la integración de archivos CSV vacíos en un DataFrame.

        - Crea un archivo CSV vacío.
        - Llama a la función integrar_csv_en_dataframe con un archivo CSV vacío.
        - Verifica que el resultado sea un DataFrame vacío y el tiempo de
          ejecución sea 0.
        """
        archivo_vacio = os.path.join(self.temp_dir, 'archivo_vacio.csv')
        open(archivo_vacio, 'a').close()

        # Llamar a la función integrar_csv_en_dataframe con un archivo CSV vacío
        resultado, tiempo_ejecucion = integrar_csv_en_dataframe(self.temp_dir)

        # Verificar que el resultado sea un DataFrame vacío
        self.assertTrue(resultado.empty)

        # Verificar que el tiempo de ejecución sea igual a 0
        self.assertEqual(tiempo_ejecucion, 0)


class TestIntegrarCSVEnDictPorColumna(unittest.TestCase):
    """Clase de prueba para la función integrar_csv_en_dict_por_columna."""

    def setUp(self) -> None:
        """Configura el entorno antes de cada prueba.

        Crea un directorio temporal para las pruebas.
        """
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        """Realiza la limpieza después de cada prueba.

        Elimina el directorio temporal después de las pruebas.
        """
        shutil.rmtree(self.temp_dir)

    def test_integrar_csv_en_dict_por_columna_archivos_validos(self) -> None:
        """Prueba la integración de archivos CSV válidos en un diccionario por
           columna.

        - Crea archivos CSV de prueba.
        - Llama a la función integrar_csv_en_dict_por_columna.
        - Verifica el resultado esperado y el tiempo de ejecución.
        """
        archivo1 = os.path.join(self.temp_dir, 'archivo1.csv')
        archivo2 = os.path.join(self.temp_dir, 'archivo2.csv')

        contenido_csv = "id,valor\n1,100\n2,200\n3,300"

        with open(archivo1, 'w') as f1, open(archivo2, 'w') as f2:
            f1.write(contenido_csv)
            f2.write(contenido_csv)

        # Llamar a la función integrar_csv_en_dict_por_columna
        resultado, tiempo_ejecucion = (
            integrar_csv_en_dict_por_columna(self.temp_dir))

        if not os.listdir(self.temp_dir):
            # Si no hay archivos CSV, esperamos un diccionario vacío
            esperado = {}
        else:
            # Si hay archivos CSV, definimos el resultado esperado
            esperado = {'id': [1, 2, 3, 1, 2, 3],
                        'valor': [100, 200, 300, 100, 200, 300]}

        # Verificar el resultado esperado
        self.assertEqual(esperado, resultado)

        # Verificar que el tiempo de ejecución sea mayor que 0
        self.assertGreater(tiempo_ejecucion, 0)


if __name__ == '__main__':

    # Crear un cargador de pruebas
    loader = unittest.TestLoader()

    # Cargar y ejecutar las pruebas para la clase TestDescomprimirArchivo
    suite_descomprimir = loader.loadTestsFromTestCase(TestDescomprimirArchivo)
    unittest.TextTestRunner(verbosity=2).run(suite_descomprimir)

    # Cargar y ejecutar las pruebas para la clase TestIntegrarCSVEnDataFrame
    suite_integrar = loader.loadTestsFromTestCase(TestIntegrarCSVEnDataFrame)
    unittest.TextTestRunner(verbosity=2).run(suite_integrar)

    # Cargar y ejecutar las pruebas para la clase
    # TestIntegrarCSVEnDictPorColumna
    suite_integrar = (
        loader.loadTestsFromTestCase(TestIntegrarCSVEnDictPorColumna))
    unittest.TextTestRunner(verbosity=2).run(suite_integrar)
