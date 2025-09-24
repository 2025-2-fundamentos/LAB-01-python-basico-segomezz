"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    resultado= {}
    with open("files/input/data.csv", "r", encoding="UTF-8") as archivo:
        reader = csv.reader(archivo, delimiter="\t")
        for row in reader:
           col2=int(row[1])
           col4=row[3].split(",")
           for letra in col4:
                if letra not in resultado:
                    resultado[letra]=col2
                else:
                    resultado[letra]+=col2
    return dict(sorted(resultado.items()))
