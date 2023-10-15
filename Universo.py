"""
Desarrollado por Rosales Benuhmea Aldo
Programa para imprimir el las posibles combinaciones binarias para E*
"""
import os
import random
import matplotlib.pyplot as plt
import time
import math
import gc
    

def limpiar_terminal():
    os.system("cls")

def Generar_cadenas(tam, cadena_actual=""):
    if len(cadena_actual) == tam:
        return [cadena_actual]
    cadenas = []
    cadenas += Generar_cadenas(tam, cadena_actual + "0")
    cadenas += Generar_cadenas(tam, cadena_actual + "1")
    
    return cadenas

def Contador_1s(cadena_binaria):
    contador_unos = 0

    for bit in cadena_binaria:
        if bit == '1':
            contador_unos += 1
    return contador_unos

def Graficar_Datos(dato, numero_dato,NumFigure):
    plt.figure(NumFigure)
    plt.plot(numero_dato, dato, '.', markersize=1, color='black')

def Generador_Universo_Binario(Numero_Potencia):
    Universo = "conjunto.txt"
    with open(Universo, "w") as archivo:
            archivo.write("Su universo: {E\n")
    
    for i in range (1,Numero_Potencia+1):
        cadenas_binarias = Generar_cadenas(i)

        with open(Universo, "a") as archivo:
            for cadena in cadenas_binarias:    
                archivo.write( cadena + "\n")

        i = i+1    
    
    with open(Universo, "a") as archivo:
        archivo.write("}")
    gc.collect()
    return("Termine :o")

salida = 0
while salida == 0:
    limpiar_terminal()
    plt.clf()
    print("Practica 1 TC")
    print("Opciones")
    print("1. Introduzca la potencia")
    print("2. Escoger una potencia aleatoria")
    Selector = input("introduzca la opción que desea realizar: ")
    Selector = int(Selector)

    if Selector == 1:
        Potencia = input("Ingrese hasta el valor que desea conocer entre 0 y 100:")
        Potencia = int(Potencia)
        tiempo_inicio = time.time()
        print(Generador_Universo_Binario(Potencia))
        
    elif Selector == 2:
        print("ha seleccionado el modo AUTOMATICO")
        Numero_Aleatorio = random.randint(1, 20)
        tiempo_inicio = time.time()
        print("Su número es:" + str(Numero_Aleatorio))
        print(Generador_Universo_Binario(Numero_Aleatorio))

        
    else:
        print("No se puede realizar la operación")


    contador = 1
   
    with open('conjunto.txt', 'r') as archivo:
        Primer = True
        for linea in archivo:
            if Primer:
                Primer = False
                continue 
            Cadena = linea.strip() 
            unos = Contador_1s(Cadena)
            Graficar_Datos(unos,contador,1)
            contador = contador + 1
    plt.title('Valores de 1')
    plt.xlabel('Número elemento')
    plt.ylabel('Número de 1s')
    plt.show()
    plt.close(1)

    plt.clf
    with open('conjunto.txt', 'r') as archivo:
        lineas = archivo.readlines()

    lineas = lineas[1:-1]

    for ix, linea in enumerate(lineas):
        Cadena = linea.strip()
        if Contador_1s(Cadena)==0:
            pass
        else:
            log10 = math.log10(Contador_1s(Cadena))

            Graficar_Datos(log10,ix,1)
    plt.title('Log10')
    plt.xlabel('Número elemento')
    plt.ylabel('Número de 1s')
    tiempo_fin = time.time()
    plt.show()
    plt.close(1)
    
        # Calcula la diferencia de tiempo
    tiempo_total = tiempo_fin - tiempo_inicio

    print(f"Tiempo total de ejecución: {tiempo_total} segundos")
    salida = input("Ingrese 0 si desea probar otro valor o 1 si desea salir:")
    salida = int(salida)
print("Fin del programa")

