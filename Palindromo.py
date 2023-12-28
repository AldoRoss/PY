"""
Desarrollado por Rosales Benuhmea Aldo
Programa para generar palindromos
"""
import os
import random
import matplotlib.pyplot as plt

def limpiar_terminal():
    os.system("cls")

def regla1(Cadena):
    Cadena = Cadena.replace("P", "")
    return Cadena
def regla2(Cadena):
    Cadena = Cadena.replace("P", "0")
    return Cadena
def regla3(Cadena):
    Cadena = Cadena.replace("P", "1")
    return Cadena
def regla4(Cadena):
    Cadena = Cadena.replace("P", "0P0")
    return Cadena
def regla5(Cadena):
    Cadena = Cadena.replace("P", "1P1")
    return Cadena
def Generar_Palindromo(tam):
    Cadena = 'P'
    Palindromo = "palindromo.txt"
    with open(Palindromo, "w") as archivo:
        archivo.write("La evolucion de su Palindromo:\n")
    
    if tam % 2 == 0:
        for i in range(int(tam/2)):
            regla = random.choice([0,1])
            if regla == 0:
                Cadena = regla4(Cadena)
                with open(Palindromo, "a") as archivo:
                    archivo.write("4: P -> 0P0 \t" + Cadena + "\n")    
            elif regla == 1:
                Cadena = regla5(Cadena)
                with open(Palindromo, "a") as archivo:
                    archivo.write("5: P -> 1P1 \t" + Cadena + "\n") 
        Cadena = regla1(Cadena)
        with open(Palindromo, "a") as archivo:
            archivo.write("1: P -> E   \t" + Cadena + "\n") 
    else:
        for i in range(int((tam - 1)/2)):
            regla = random.choice([0,1])
            if regla == 0:
                Cadena = regla4(Cadena)
                with open(Palindromo, "a") as archivo:
                    archivo.write("4: P -> 0P0 \t" + Cadena + "\n")    
            elif regla == 1:
                Cadena = regla5(Cadena)
                with open(Palindromo, "a") as archivo:
                    archivo.write("5: P -> 1P1 \t" + Cadena + "\n") 

        regla = random.choice([0,1])
        if regla == 0:
            Cadena = regla2(Cadena)
            with open(Palindromo, "a") as archivo:
                archivo.write("2: P -> 0   \t" + Cadena + "\n") 
        else:
            Cadena = regla3(Cadena)
            with open(Palindromo, "a") as archivo:
                archivo.write("3: P -> 1   \t" + Cadena + "\n") 
    return Cadena

limpiar_terminal()
print("Programa para generar un palindromo")
print("1. Introduzca la longitud del palindromo")
print("2. Longitud del palindromo aleatorio")
auto = input("Ingrese el numero de la opcion que desea vizualizar:")
auto = int(auto)
if auto == 1:
    tam = input("Ingrezca la longitud de su palindromo:")
    tam = int(tam)
elif auto == 2:
    tam = random.randint(1, 10000)
    print(f'Su palindromo tiene una tamaño de {tam} elementos')
Palindromo = Generar_Palindromo(tam)
print(Palindromo)