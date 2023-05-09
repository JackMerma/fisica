from config import *
import math

variableList = ["Velocidad", "Tiempo", "Distancia"]

def showMruList():
    return showList(variableList)

def calculateMru(data):
    existance = data[0]
    dataList = data[1]
    # tiempo positivo
    if(existance[1] and dataList[1] < 0):
        printResult("El tiempo no puede ser negativo")
        return

    if (existance[0] == -1):
        # existencia de datos
        if(not existance[1] or not existance[2]):
            printResult("Datos insuficientes")
            return

        # procesamiento
        if(dataList[1] == 0):
            printResult("El tiempo no puede ser 0")
        else:
            result = dataList[2] / dataList[1]
            result = str(result)
            printResult("La velocidad es " + result + " m/s")
    elif (existance[1] == -1):
        # existencia de datos
        if(not existance[0] or not existance[2]):
            printResult("Datos insuficientes")
            return

        # procesamiento
        if(dataList[0] == 0):
            printResult("La velocidad no puede ser 0")
        else:
            result = dataList[2] / dataList[0]
            result = str(result)
            printResult("El tiempo es " + result + " s")
    elif (existance[2] == -1):
        # existencia de datos
        if(not existance[0] or not existance[1]):
            printResult("Datos insuficientes")
            return

        # procesamiento
        result = dataList[0] * dataList[1]
        result = str(result)
        printResult("La distancia es " + result + " m")
    else:
        printResult("Nada por calcular")
