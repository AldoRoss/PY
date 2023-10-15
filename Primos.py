"""
Desarrollado por Rosales Benuhmea Aldo
1er Programa: imprimir el las posibles combinaciones binarias para E*
2do Programa: graficar la cadena y el número de elementos de la cadena
3er Programa: imprimir los números primos y graficarlos
"""
import os
import random
import math
import matplotlib.pyplot as plt

def limpiar_terminal():
    os.system("cls")

def es_primo_miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Descomponer n-1 en la forma 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Realizar k iteraciones del Test de Miller-Rabin
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def validar_Entrada_Numerica(entrada):
    if entrada.isdigit():
        entrada = int(entrada)
        print("Su número es " + str(entrada))
    else:
        print("Ha ingresado una letra")
    return entrada

def Convertir_Binario(numero):
    cadena_binaria = ""

    while numero > 0:
        residuo = numero % 2
        cadena_binaria = str(residuo) + cadena_binaria
        numero //= 2

    return cadena_binaria

def Contador_1s(cadena_binaria):
    contador_unos = 0

    for bit in cadena_binaria:
        if bit == '1':
            contador_unos += 1
    return contador_unos

def Graficar_Datos(dato, numero_dato,NumFigure):
    plt.figure(NumFigure)
    plt.plot(numero_dato, dato, '.', markersize=1, color='black')

salida = 0
while salida == 0:
    limpiar_terminal()
    print("Programa para ver las cadenas de los números primos")
    NumerosRevisar = input("¿Cuantos números desea revisar?")
    NumerosRevisar = (validar_Entrada_Numerica(NumerosRevisar))
    archivoDecimal = "conjuntoPrimosDecimal.txt"
    archivoBinario = "ConjuntoPrimosBinario.txt"
    with open(archivoDecimal, "w") as archivo:
        archivo.write("Su universo: {E\n")
    with open(archivoBinario, "w") as archivo:
        archivo.write("Su universo: {E\n")
    i = 1
    for i in range (1,NumerosRevisar+1):

        if es_primo_miller_rabin(i):
            with open(archivoDecimal, "a") as archivo:
                archivo.write(str(i) + "\n")
            with open(archivoBinario, "a") as archivo:
                archivo.write(Convertir_Binario(i) + "\n")
            i = i+1
                        
        else:
            i = i+1
    with open(archivoDecimal, "a") as archivo:
        archivo.write("}")
    with open(archivoBinario, "a") as archivo:
        archivo.write("}")

    print("Termine Parte1")  

    contador = 1
    with open(archivoBinario, 'r') as archivo:
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


    contador = []
    log10 = []

    with open(archivoBinario, 'r') as archivo:
        lineas = archivo.readlines()

    lineas = lineas[1:-1]
    for ix, linea in enumerate(lineas):
        Cadena = linea.strip()
        if Contador_1s(Cadena)==0:
            pass
        else:
            log10 = math.log10(Contador_1s(Cadena))

            Graficar_Datos(log10,ix,2)
    plt.title('Log10')
    plt.xlabel('Número elemento')
    plt.ylabel('Número de 1s')
    plt.show()
    plt.close(2)

    print("Estoy Cansado Jefe :(")                
    salida = input("Ingrese 0 si desea probar otro valor o 1 si desea salir:")
    salida = int(salida)
print("Fin del programa")