#!/usr/bin/python
# coding=utf-8

# Filename  : PyMath.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/PyMath

#-----importaciones-----
import os, math, platform

# declaración de variables
decision = 0
OSsystem = platform.system()

def goBack():
    print("")
    goBack = int(input("¿Quieres regresar al menu?\n[1] Sí.\n[0] No.\n\n>:"))
    if(goBack==1):
        main()
    elif(goBack==0):
        exit()
    else:
        print("Error.")

def banner ():
    print("+==============================================+")
    print("+                                              +")
    print("+      ▄▄▄· ▄· ▄▌• ▌ ▄ ·.  ▄▄▄· ▄▄▄▄▄ ▄ .▄     +")
    print("+     ▐█ ▄█▐█▪██▌·██ ▐███▪▐█ ▀█ •██  ██▪▐█     +")
    print("+      ██▀·▐█▌▐█▪▐█ ▌▐▌▐█·▄█▀▀█  ▐█.▪██▀▐█     +")
    print("+     ▐█▪·• ▐█▀·.██ ██▌▐█▌▐█ ▪▐▌ ▐█▌·██▌▐▀     +")
    print("+     .▀     ▀ • ▀▀  █▪▀▀▀ ▀  ▀  ▀▀▀ ▀▀▀ ·     +")
    print("+=================Joshua Ayala=================+")
    print("")
    
def menu():
    print("Selecciona una opción:")
    print("[1] Sumar/Multiplicar.")
    print("[2] Separación de números pares e impares.")
    print("[3] Áreas (círculo, rectángulo).\n")
    print("[0] Salir.")
    decision = int(input(">: "))
    if (decision==1):
        sumarMultiplicar()
    elif(decision==2):
        separarNum()
    elif(decision==3):
        areas()
    elif(decision==0):
        restart=False
        os.system('exit')
    else:
        restart=False
        print("Error")


def sumarMultiplicar():
    print("¿Quieres sumar o multiplicar?\n")
    print("[1] Sumar.")
    print("[2] Multiplicar.\n")
    print("[0] Regresar.")
    decision = int(input(">: "))
    if (decision==1):
        limite = int(input("¿Cuántos números quieres sumar?: "))
        resultado=0
        i=0
        numero = 0
        while(i<limite):
            i+=1
            numero = float(input("Introduce un valor: "))
            resultado = resultado + numero
            
        print("El resultado de la suma es: ", resultado) 
        goBack()
        
    elif (decision==2):
        numero = int(input("Introduce el numero del que quieras saber su tabla de multiplicación: "))
        limite = int(input("¿Hasta donde quieres multiplicarlo?: "))
        i=0
        while(i<limite):
            i+=1
            print(numero, "x", i, "=", numero*i)

        goBack()
    elif (decision==0):
        main()
    else:
        print("Error.")

def separarNum():
    i=0
    impares = []
    pares = []
    limite = int(input("Introduce hasta donde quieres separar los numeros:\n>: "))
    while(i<limite):
        i+=1
        if(i%2==0):
            pares.append(i)
        else:
            impares.append(i)

    print("Pares: ", pares)
    print("")
    print("Impares: ", impares)
    goBack()
def areas():
    print("¿Quieres calcular el área de un círculo o la de un rectángulo?\n")
    print("[1] Círculo.")
    print("[2] Rectángulo.\n")
    print("[0] Regresar.")
    decision = int(input(">: "))
    if (decision==1):
        radio = int(input("Introduce el valor del radio: "))
        area = (radio**2)*math.pi
        print("El area del circulo es: ", area)
    elif (decision==2):
        base = int(input("Introduce el valor de la base: "))
        altura = int(input("Introduce el valor de la altura: "))
        area = base * altura
        print("El area del rectangulo es: ", area)
    elif (decision==0):
        main()
    else:
        print("Error.")

    goBack()
def main():
    if(OSsystem=="Linux" or OSsystem=="MacOS"):
        os.system('clear')
    else:
        (os.system('cls'))
    banner()
    menu()

main()
