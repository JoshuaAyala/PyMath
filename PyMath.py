# Mini Proyecto
# Autor: Joshua Ayala
# Tijuana, B.C., México.

#-----importaciones-----
import os

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
    decisión = int(input(">: "))
    if (decisión==1):
        sumarMultiplicar()
    elif(decisión==2):
        separarNum()
    elif(decisión==3):
        areas()
    elif(decisión==0):
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
    decisión = int(input(">: "))
    if (decisión==1):
        limite = int(input("¿Cuántos números quieres sumar?: "))
        resultado=0
        i=0
        numero = 0
        while(i<limite):
            i+=1
            numero = float(input("Introduce un valor: "))
            resultado = resultado + numero
            
        print("El resultado de la suma es: ", resultado) 
        
    elif (decisión==2):
        numero = int(input("Introduce el numero del que quieras saber su tabla de multiplicación: "))
        limite = int(input("¿Hasta donde quieres multiplicarlo?: "))
        i=0
        while(i<limite):
            i+=1
            print(numero, "x", i, "=", numero*i)
            
    else:
        print("Error.")
        
restart = True
decisión = 0

while (restart==True):
    os.system('clear')
    banner()
    menu()
