from setuptools import setup, find_packages

setup(
    name='PEC4_aparamio',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # Lista de dependencias
        'contourpy==1.2.0',
        'cycler==0.12.1',
        'fonttools==4.47.2',
        'kiwisolver==1.4.5',
        'matplotlib==3.8.2',
        'numpy==1.26.3',
        'packaging==23.2',
        'pandas==2.1.4',
        'pillow==10.2.0',
        'pyparsing==3.1.1',
        'python-dateutil==2.8.2',
        'pytz==2023.3.post1',
        'six==1.16.0',
        'tzdata==2023.4',
    ],
    entry_points={
        # Punto de entrada para ejecución de comandos
        'console_scripts': [
            'ejecutar=main:main',
        ],
    },
    author='Alberto Paramio Galisteo',
    description='PEC4 de la asignatura Programación para la Ciencia de Datos',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/albertoparamio/PEC4_aparamio',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)