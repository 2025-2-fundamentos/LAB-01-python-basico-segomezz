"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    lista=[("A", 0,1000), ("B", 0,1000), ("C", 0,1000), ("D", 0,1000), ("E", 0,1000)]
    with open("files/input/data.csv", "r", encoding="UTF-8") as archivo:
        reader = csv.reader(archivo, delimiter="\t")
        for row in reader:
            letra=row[0]
            numero=int(row[1])
            for i in range(len(lista)):
                if lista[i][0]==letra:
                    if numero>lista[i][1]:
                        lista[i]=(letra, numero, lista[i][2])
                    if numero<lista[i][2]:
                        lista[i]=(letra, lista[i][1], numero)
                    break
    return lista

