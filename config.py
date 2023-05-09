import numpy as np

OPTIONS = ["MRU", "MRUV"]

def showList(variableList):
    dataList = np.zeros(len(variableList))
    existance = np.zeros(len(variableList))

    print("╔════════════════════════════════════════════╗")
    print("║      Coloque el dato, una 'x' o vacío      ║")
    print("╠════════════════════════════════════════════╝")

    for i in range(len(variableList)):
        dato = input("║ " + variableList[i] + ": ")
        if(dato == "X" or dato == "x"):
            existance[i] = -1
        elif (dato == ""):
            pass
        else:
            dataList[i] = float(dato)
            existance[i] = 1

    print("╚════════════════════════════════════════════╝")

    return [existance, dataList]

def printResult(mnsj):
    print("╔════════════════════════════════════════════╗")
    print("║ " + mnsj)
    print("╚════════════════════════════════════════════╝")
