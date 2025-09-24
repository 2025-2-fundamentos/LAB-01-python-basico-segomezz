"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    lista = [("A", 0), ("B", 0), ("C", 0), ("D", 0), ("E", 0)]
    with open("files/input/data.csv", "r", encoding="UTF-8") as archivo:
        reader = csv.reader(archivo, delimiter="\t")
        for row in reader:
            letra=row[0]
            numero=int(row[1])
            for i in range(len(lista)):
                if lista[i][0]==letra:
                    lista[i]=(letra, lista[i][1]+numero)
                    break
    return lista
lista = [("A", 0), ("B", 0), ("C", 0), ("D", 0), ("E", 0)]
