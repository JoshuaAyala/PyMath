#!/usr/bin/python
#coding: utf-8

# Filename  : PyMath.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/PyMath
# pep8: 100%

#-----importaciones-----
from packages.operaciones import *
from packages.banners import *

import os, math, platform, time

# declaración de variables
decision = 0
OSsystem = platform.system()

# Menú Principal
def menu(decision):
    decision = int(input("Selecciona una opción:\n[1] Aritmetica.\n[2] Física.\n[3] Áreas.\n\n[0] Salir.\n\n>: "))
    if (decision==1):
        aritmeticaMenu(decision)
    elif(decision==2):
        fisicaMenu(decision)
    elif(decision==3):
        areasMenu(decision)
    elif(decision==0):
        os.system('exit')
    else:
        print("Error")
        goBack()

# Menú de la opción [1] Aritmética
def aritmeticaMenu(decision):
    checkOSandCleanohYeah()
    aritmeticaBanner()
    subdecision = int(input("Selecciona una opción´:\n[1] Suma.\n[2] Resta.\n[3] División.\n[4] Multiplicación.\n\n[0] Volver.\n\n>: "))
    if(subdecision == 1):
        Sumar()
        goBack()
    elif(subdecision == 2):
        Restar()
        goBack()
    elif(subdecision == 3):
        Dividir()
        goBack()
    elif(subdecision == 4):
        Multiplicar()
        goBack()
    elif(subdecision == 0):
        main()
    else:
        print("Opción equivocada")
        time.sleep(2)
        aritmeticaMenu(decision)

# Menú de la opción [2] Física
def fisicaMenu(decision):
    checkOSandCleanohYeah()
    fisicaBanner()
    subdecision = int(input("Selecciona una opción:\n[1] Velocidad.\n[2] Distancia.\n[3] Tiempo.\n\n[0] Volver.\n\n>: "))
    if(subdecision == 1):
        fisicaVelocidad()
        goBack()
    elif(subdecision == 2):
        fisicaDistancia()
        goBack()
    elif(subdecision == 3):
        fisicaTiempo()
        goBack()
    elif(subdecision == 0):
        main()
    else:
        print("Error")
        time.sleep(1)
        fisicaMenu(decision)

# Menú de la opción [3] Áreas
def areasMenu(decision):
    checkOSandCleanohYeah()
    areasBanner()
    subdecision = int(input("Selecciona una opción´:\n[1] Triángulo.\n[2] Círculo.\n[3] Cuadrado.\n[4] Rectángulo.\n\n[0] Volver.\n\n>: "))
    if(subdecision == 1):
        areaTriangulo()
        goBack()
    elif(subdecision == 2):
        areaCirculo()
        goBack()
    elif(subdecision == 3):
        areaCuadrado()
        goBack()
    elif(subdecision == 4):
        areaRectangulo()
        goBack()
    elif(subdecision == 0):
        main()
    else:
        print("Error")
        time.sleep(1)
        areasMenu(decision)

# Función para regresar a main
def goBack():
    print("")
    goBack = int(input("¿Quieres regresar al menu?\n[1] Sí.\n[0] No.\n\n>:"))
    if(goBack==1):
        main()
    elif(goBack==0):
        exit()
    else:
        print("Error.")
        time.sleep(1)
        goBack()

# Saber que sistema operativo se usa y saber qué comando usar
def checkOSandCleanohYeah():
    if(OSsystem=="Linux" or OSsystem=="Darwin" or OSsystem=="MacOS"):
        os.system('clear')
    else:
        (os.system('cls'))

# Función main
def main():
    checkOSandCleanohYeah()
    mainbanner()
    menu(decision)

if __name__ == '__main__':
    main()
