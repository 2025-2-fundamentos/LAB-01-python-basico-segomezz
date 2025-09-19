"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    lista = [("A", 0), ("B", 0), ("C", 0), ("D", 0), ("E", 0)]
    with open("/Users/sebastiangomezzapata/Universidad/Semestre 2025-II/Fundamentos de Analítica/LAB-01-python-basico-segomezz/files/input/data.csv", "r", encoding="UTF-8") as archivo:
        reader = csv.reader(archivo, delimiter="\t")
        for row in reader:
            letra = row[0]
            for i in range(len(lista)):
                if lista[i][0] == letra:
                    lista[i] = (letra, lista[i][1] + 1)
                    break
    return lista
