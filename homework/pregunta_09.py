"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    resultado= {}
    with open("files/input/data.csv", "r", encoding="UTF-8") as archivo:
        reader = csv.reader(archivo, delimiter="\t")
        for row in reader:
           diccionario=row[4].split(",")
           for elemento in diccionario:
                clave, valor= elemento.split(":")
                valor=int(valor)
                if clave not in resultado:
                    resultado[clave]=1
                else:
                    resultado[clave]+=1
    return resultado

