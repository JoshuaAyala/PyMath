#!/usr/bin/python
#coding: utf-8

# Filename  : operaciones.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/PyMath/packages
# pep8: 100%

import math

# Función Sumar
def Sumar():
    limite = int(input("¿Cuántos números quieres sumar?: "))
    resultado = 0
    i = 0
    numero = 0
    while(i < limite):
        i+=1
        numero = float(input("Introduce un valor: "))
        resultado = resultado + numero

    print("El resultado de la suma es: ", resultado) 

# Función Restar
def Restar():
    limite = int(input("¿Cuántos números quieras restar?: "))
    resultado = float(input("Introduce un valor: "))
    i = 1
    numero = 0
    while(i < limite):
        i+=1
        numero = float(input("Introduce un valor: "))
        resultado = resultado - numero

    print("El resultado de la resta es: ", resultado)

# Función Dividir
def Dividir():
    limite = int(input("¿Cuántos números quieras dividir?: "))
    resultado = float(input("Introduce un valor: "))
    i = 1
    numero = 0
    while(i < limite):
        i+=1
        numero = float(input("Introduce un valor: "))
        resultado = resultado / numero

    print("El resultado de la división es: ", resultado)

# Función Multiplicar
def Multiplicar():
    numero = float(input("Introduce el numero del que quieras saber su tabla de multiplicación: "))
    limite = float(input("¿Hasta donde quieres multiplicarlo?: "))
    i = 0
    while(i < limite):
        i+=1
        print(numero, "x", i, "=", numero*i)

# Función Velocidad
def fisicaVelocidad():
    distancia = float(input("Introduce el valor de la distancia: "))
    tiempo = float(input("Introduce el valor del tiempo: "))
    velocidad = distancia / tiempo
    print("\nEl valor de la velocidad es de: ", velocidad, "V.")

# Función Distancia
def fisicaDistancia():
    velocidad = float(input("Introduce el valor de la velocidad: "))
    tiempo = float(input("Introduce el valor del tiempo: "))
    distancia = velocidad * tiempo
    print("\nEl valor de la distancia es de: ", distancia)

# Función Tiempo
def fisicaTiempo():
    distancia = float(input("Introduce el valor de la distancia: "))
    velocidad = float(input("Introduce el valor de la velocidad: "))
    tiempo = distancia / velocidad
    print("\nEl valor del tiempo es de: ", tiempo)

# Función Área Triángulo
def areaTriangulo():
    base = float(input("Introduce el valor de la base: "))
    altura = float(input("Introduce el valor de la altura: "))
    area = (base * altura) / 2
    print("\nEl valor del área es de: ", area)

# Función Área Círculo
def areaCirculo():
    radio = float(input("Introduce el valor del radio: "))
    area = (radio**2) * math.pi
    print("\nEl área del circulo es: ", area)

# Función Área Cuadrado
def areaCuadrado():
    lado = float(input("Introduce el valor de cualquier lado: "))
    print("\nEl área del cuadrado es ", lado * lado)

# Función Área Rectángulo
def areaRectangulo():
    base = float(input("Introduce el valor de la base: "))
    altura = float(input("Introduce el valor de la altura: "))
    area = base * altura
    print("\nEl área del rectángulo es de: ", area)
