from config import *

variableList = ["Velocidad final", "Velocidad inicial", "Aceleración",
                "Tiempo", "Distancia"]

def showMruvList():
    return showList(variableList)

def calculateMruv(data):
    existance = data[0]
    dataList = data[1]
    # tiempo positivo
    if(existance[1] and dataList[1] < 0):
        printResult("El tiempo no puede ser negativo")
        return

    # factor de aceleracion
    fact = 1
    if(existance[2] and dataList[2] < 0):
        fact = -1

    if(existance[0] == -1):
        # existencia de datos
        if(not existance[1] or not existance[2] or not existance[3]):
            printResult("Datos insuficientes")
            return

        # procesamiento
        result = dataList[1] + dataList[2] * dataList[3] * fact
        result = str(result)
        printResult("La velocidad final es " + result + " m/s")
    elif(existance[1] == -1):
        # existencia para formula 1
        existance1 = True
        if(not existance[0] or not existance[2] or not existance[3]):
            existance1 = False

        # existencia para formula 2
        if(not existance1):
            if(not existance[2] or not existance[3] or not existance[4]):
                printResult("Datos insuficientes")
                return

        if(existance1): # formula 1
            result = dataList[0] - dataList[2] * dataList[3] * fact
            result = str(result)
            printResult("La velocidad inicial es " + result + " m/s")
        else: # formula 2
            # procesamiento
            if(dataList[3] == 0):
                printResult("El tiempo no puede ser 0")
            else:
                result = (dataList[4] - 0.5 * dataList[2] * (dataList[3] ** 2) * fact) / dataList[3]
                result = str(result)
                printResult("La velocidad inicial es " + result + " m/s")

    elif(existance[2] == -1):
        # existencia para formula 1
        existance1 = True
        if(not existance[0] or not existance[1] or not existance[3]):
            existance1 = False

        # existencia para formula 2
        if(not existance1):
            if(not existance[1] or not existance[3] or not existance[4]):
                printResult("Datos insuficientes")
                return

        if(existance1): # formula 1
            if(dataList[3] == 0):
                printResult("El tiempo no puede ser 0")
            else:
                result = (dataList[0] - dataList[1]) / (dataList[3] * fact)
                result = str(result)
                printResult("La aceleracion es " + result + " m/s^2")
        else: # formula 2
            if(dataList[3] == 0):
                printResult("El tiempo no puede ser 0")
            else:
                result = (dataList[4] - dataList[1] * dataList[3]) / (fact * 0.5 * dataList[3] ** 2)
                result = str(result)
                printResult("La aceleracion es " + result + " m/s^2")
    elif(existance[3] == -1):
        # existencia de datos
        if(not existance[0] or not existance[1] or not existance[2]):
            printResult("Datos insuficientes")
            return

        # procesamiento
        if(dataList[2] == 0):
            printResult("La aceleracion no puede ser 0")
        else:
            result = (dataList[0] - dataList[1]) / (dataList[2] * fact)
            result = str(result)
            printResult("El tiempo es " + result + " s")
    elif(existance[4] == -1):
        # existencia de datos
        if(not existance[1] or not existance[2] or not existance[3]):
            printResult("Datos insuficientes")
            return

        # procesamiento
        result = dataList[1] * dataList[3] + fact * 0.5 * dataList[2] * dataList[3] ** 2
        result = str(result)
        printResult("La distancia es " + result + " m")
    else:
        printResult("Nada por calcular")
