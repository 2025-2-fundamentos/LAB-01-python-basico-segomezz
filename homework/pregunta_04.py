"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    lista=[("01", 0), ("02", 0), ("03", 0), ("04", 0), ("05", 0), ("06", 0), ("07", 0), ("08", 0), ("09", 0), ("10", 0), ("11", 0), ("12", 0)]
    with open("files/input/data.csv", "r", encoding="UTF-8") as archivo:
        reader = csv.reader(archivo, delimiter="\t")
        for row in reader:
            fecha= row[2]
            mes=fecha[5:7]
            for i in range(len(lista)):
                if lista[i][0]==mes:
                    lista[i]=(mes, lista[i][1]+1)
                    break
    return lista
            
