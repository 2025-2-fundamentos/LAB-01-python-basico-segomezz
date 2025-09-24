"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    import csv
    resultado= {}
    with open("files/input/data.csv", "r", encoding="UTF-8") as archivo:
        reader = csv.reader(archivo, delimiter="\t")
        for row in reader:
           clave=row[0]
           diccionario=row[4].split(",")
           suma=0
           for elemento in diccionario:
                _, valor= elemento.split(":")
                valor=int(valor)
                suma+=valor
           if clave not in resultado:
                resultado[clave]=suma
           else:
                resultado[clave]+=suma
    return resultado 