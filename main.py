from mru import showMruList, calculateMru
from mruv import showMruvList, calculateMruv
from config import *

def showMenu():
    option = None

    while(option == None):
        print("╔════════════════════════════╗")
        print("║    Elija una opción (x)    ║")
        print("╠════════════════════════════╝")

        for i in range(len(OPTIONS)):
            dato = input("║ " + OPTIONS[i] + ": ")
            if(dato == "X" or dato == "x"):
                option = i
                break

        print("╚═════════════════════════════")
    return option

def calculate(option):
    if(option == 0):
        calculateMru(showMruList())
    else:
        calculateMruv(showMruvList())

opt = showMenu()
calculate(opt)
