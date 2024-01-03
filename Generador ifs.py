"""
Desarrollado por Rosales Benuhmea Aldo
Elaborar un programa que derive la gramática Backus-Naur que define el condicional IF.

S -> iCtSA
A -> ;eS | epsilon

El programa debe derivar automáticamente la gramática hasta crear un número de IFs 
que sea determinado por el usuario o por la máquina. Mostrar cada paso de todas las 
derivaciones que se realizarán aleatoriamente en un archivo. Además mostrar en otro 
archivo el pseudo-código de la cadena generada con la gramática. El límite establecido 
para realizar las derivaciones es de 1000.
"""
import os
import random
import matplotlib.pyplot as plt

def limpiar_terminal():
    os.system("cls")

def regla1(Cadena):
    if "S" in Cadena:
        indices = [i for i, char in enumerate(Cadena) if char == "S"]
        indice = random.choice(indices)
        Cadena = Cadena[:indice] + "iCtSA" + Cadena[indice + 1:]
        GramaticaBN = "IFs.txt"
        with open(GramaticaBN, "a") as archivo:
            archivo.write("S -> iCtSA\t" + Cadena + "\n")
    else:
        Cadena = Cadena
    return Cadena

def regla2(Cadena):
    if "A" in Cadena:
        indices = [i for i, char in enumerate(Cadena) if char == "A"]
        indice = random.choice(indices)
        Cadena = Cadena[:indice] + "eS" + Cadena[indice + 1:]
        GramaticaBN = "IFs.txt"
        with open(GramaticaBN, "a") as archivo:
            archivo.write("A -> eS  \t" + Cadena + "\n")
    else:
        Cadena = Cadena
    return Cadena

def regla3(Cadena):
    if "A" in Cadena:
        indices = [i for i, char in enumerate(Cadena) if char == "A"]
        indice = random.choice(indices)
        Cadena = Cadena[:indice] + "" + Cadena[indice + 1:]

        GramaticaBN = "IFs.txt"
        with open(GramaticaBN, "a") as archivo:
            archivo.write("A -> E   \t" + Cadena + "\n")
    else:
        Cadena = Cadena
    return Cadena



def Generar_GramaticaBN(tam):

    GramaticaBN = "IFs.txt"
    with open(GramaticaBN, "w") as archivo:
        archivo.write("La evolucion de su gramatica:\n")
    
    Gramatica = 'S'
    Gramatica = regla1(Gramatica)
    NumIfs = 1
    while tam > NumIfs:
        regla = random.choice([0,1])
        if regla == 0:
            Gramatica = regla1(Gramatica)
            NumIfs = NumIfs + 1

        elif regla == 1:
            reglaX = random.choice([0,1])
            if reglaX == 0:
                Gramatica = regla2(Gramatica)
            elif reglaX == 1:
                Gramatica = regla3(Gramatica)
    return Gramatica

def Generar_pseudo(Gramatica):
    Pseudocodigo = "Pseudocodigo.txt"
    with open(Pseudocodigo, "w") as archivo:
        archivo.write("Pseudocodigo:\n")
    n = 0
    for elemento in Gramatica:
        if elemento == "i":
            with open(Pseudocodigo, "a") as archivo:
                archivo.write(("\t" * n) + "If")
            n = n + 1
        elif elemento == "C":
            with open(Pseudocodigo, "a") as archivo:
                archivo.write("(Conditional)")
        elif elemento == "t":
            with open(Pseudocodigo, "a") as archivo:
                archivo.write(" then\n")
        elif elemento == "S":
            with open(Pseudocodigo, "a") as archivo:
                archivo.write(("\t" * n) + "Sentences\n")

        elif elemento == "e":
            n = n - 1
            with open(Pseudocodigo, "a") as archivo:
                archivo.write(("\t" * n) + "elif\n")
            n = n + 1
        
        elif elemento == "A":
            n = n - 1
            with open(Pseudocodigo, "a") as archivo:
                archivo.write(("\t" * n) + "end\n")
    print("Termine ;)")

limpiar_terminal()
print("Programa para generar la gramática Backus-Naur que define el condicional IF")
print("1. Introduzca la longitud de su gramatica")
print("2. Longitud de gramatica aleatoria")
auto = input("Ingrese el numero de la opcion que desea vizualizar:")
auto = int(auto)
if auto == 1:
    tam = input("Ingrezca la longitud de su gramatica:")
    tam = int(tam)
elif auto == 2:
    tam = random.randint(1, 1000)
    print(f'Su gramatica tiene una tamaño de {tam} elementos')

Gramatica = Generar_GramaticaBN(tam)
print(Gramatica)
Generar_pseudo(Gramatica)
