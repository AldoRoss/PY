"""
Desarrollado por Rosales Benuhmea Aldo
4to Programa: Tablero
"""
import os
import random
import tkinter as tk

colores_iniciales = {
    1: "turquoise",
    2: "white",
    3: "turquoise",
    4: "white",
    5: "white",
    6: "turquoise",
    7: "white",
    8: "turquoise",
    9: "turquoise",
    10: "white",
    11: "turquoise",
    12: "white",
    13: "white",
    14: "turquoise",
    15: "white",
    16: "turquoise"
}


ventana = tk.Tk()
ventana.title("Tablero 4x4")

filas, columnas = 4, 4
casillas = {}

def cambiar_color_casilla(numero, color):
    casilla = casillas[numero]
    casilla.config(bg=color)

def cambiar_colores_secuencia(lista_secuencia,color):
    colores_originales = [colores_iniciales[num] for num in lista_secuencia]
    nuevos_estados = [(num, color) for num in lista_secuencia]

    def restaurar_colores_originales():
        for i, numero in enumerate(lista_secuencia):
            cambiar_color_casilla(numero, colores_originales[i])

    for i, (numero, color) in enumerate(nuevos_estados):
        ventana.after(2000 * i, cambiar_color_casilla, numero, color)
        ventana.after(2000 * (i + 1), restaurar_colores_originales)

for fila in range(filas):
    for columna in range(columnas):
        i = fila * 4 + columna + 1
        color = colores_iniciales[i]

        casilla = tk.Label(ventana, text=str(i), bg=color, width=10, height=5, font=("Helvetica", 12))
        casilla.grid(row=fila, column=columna)

        casillas[i] = casilla

ventana.withdraw()

def limpiar_terminal():
    os.system("cls")

def generar_cadena_binaria(Tam):
    cadena = ''.join(random.choice(["B", "N"]) for _ in range(Tam))
    cadena = str(cadena)
    return cadena
def CaminoAlExito(archivo):
    with open(archivo, 'r') as archivo:
        lineas = archivo.readlines()

    if len(lineas) >= 2:
        segunda_linea = lineas[1].strip()  
        if segunda_linea:
            segunda_linea_lista = [int(numero) for numero in segunda_linea.split(', ')]
            return segunda_linea_lista
        else:
            return [] 
    else:
        return [] 

def Siguiente_estado(elemento, estado):
    if estado == 1 and elemento == "B":
        estadoSiguiente = [2,5]
    elif estado == 1 and elemento == "N":
        estadoSiguiente = [6]
    elif estado == 2 and elemento == "B":
        estadoSiguiente = [5,7]
    elif estado == 2 and elemento == "N":
        estadoSiguiente = [1,3,6]
    elif estado == 3 and elemento == "B":
        estadoSiguiente = [2,4,7]
    elif estado == 3 and elemento == "N":
        estadoSiguiente = [6,8]
    elif estado == 4 and elemento == "B":
        estadoSiguiente = [7]
    elif estado == 4 and elemento == "N":
        estadoSiguiente = [3,8]
    elif estado == 5 and elemento == "B":
        estadoSiguiente = [2,10]
    elif estado == 5 and elemento == "N":
        estadoSiguiente = [1,6,9]
    elif estado == 6 and elemento == "B":
        estadoSiguiente = [2,5,7,10]
    elif estado == 6 and elemento == "N":
        estadoSiguiente = [1,3,9,11]
    elif estado == 7 and elemento == "B":
        estadoSiguiente = [2,4,10,12]
    elif estado == 7 and elemento == "N":
        estadoSiguiente = [3,6,8,11]
    elif estado == 8 and elemento == "B":
        estadoSiguiente = [4,7,10]
    elif estado == 8 and elemento == "N":
        estadoSiguiente = [3,11]
    elif estado == 9 and elemento == "B":
        estadoSiguiente = [5,10,13]
    elif estado == 9 and elemento == "N":
        estadoSiguiente = [6,14]
    elif estado == 10 and elemento == "B":
        estadoSiguiente = [5,7,13,15]
    elif estado == 10 and elemento == "N":
        estadoSiguiente = [6,9,11,14]
    elif estado == 11 and elemento == "B":
        estadoSiguiente = [7,10,12,15]
    elif estado == 11 and elemento == "N":
        estadoSiguiente = [6,8,14,16]
    elif estado == 12 and elemento == "B":
        estadoSiguiente = [7,11]
    elif estado == 12 and elemento == "N":
        estadoSiguiente = [8,11,16]
    elif estado == 13 and elemento == "B":
        estadoSiguiente = [10]
    elif estado == 13 and elemento == "N":
        estadoSiguiente = [9,14]
    elif estado == 14 and elemento == "B":
        estadoSiguiente = [10,13,15]
    elif estado == 14 and elemento == "N":
        estadoSiguiente = [9,11]
    elif estado == 15 and elemento == "B":
        estadoSiguiente = [10,12]
    elif estado == 15 and elemento == "N":
        estadoSiguiente = [11,14,16]
    elif estado == 16 and elemento == "B":
        estadoSiguiente = [12,15]
    elif estado == 16 and elemento == "N":
        estadoSiguiente = [11]
    return estadoSiguiente

def generar_arbol(estado, Jugada, archivo, ruta_actual=[]):
    if Jugada == "":
        archivo.write(", ".join(map(str, ruta_actual)) + "\n")
        return

    elemento = Jugada[0]
    Jugada = Jugada[1:]
    tamSig = len(estado)
    for i in range(0, tamSig):
        estado_siguiente = Siguiente_estado(elemento, estado[i])
        generar_arbol(estado_siguiente, Jugada, archivo, ruta_actual + [estado[i]])

def Ganador1er(cadena):
    if cadena.endswith("16") == True:
        valor=1
    else:
        valor=0
    return valor

def Ganador2do(cadena):
    if cadena.endswith("13") == True:
        valor=1
    else:
        valor=0
    return valor
limpiar_terminal()
archivoJugadas1 = "PosiblesJugadasJug1.txt"
archivoJugadas2 = "PosiblesJugadasJug2.txt"
print("Programa del Tablero")
print("Jugadores")
print("1. Un jugador")
print("2. Dos Jugadores")
Jugadores = input("introduzca la opción que desea realizar: ")
Jugadores = int(Jugadores)
print("Opciones")
print("1. Introduzca su jugada")
print("2. Escoger una jugada aleatoria")
Selector = input("introduzca la opción que desea realizar: ")
Selector = int(Selector)

if Jugadores == 1:
    with open(archivoJugadas1, "w") as archivo:
        archivo.write("Sus posibles Jugadas son:\n")
    if Selector == 1:
        Jugada = input("Ingrese su Jugada (Ejemplo: BBNBN):")
    elif Selector == 2:
        TamJugada = input("Ingrese el tamaño de su jugada:")
        TamJugada = int(TamJugada)
        Jugada = generar_cadena_binaria(TamJugada)
    print("Su jugada es: " + Jugada)
    elementoVacio = "N"
    Jugada = Jugada + elementoVacio
    estado = [1]
    with open(archivoJugadas1, "a") as archivo:
        generar_arbol(estado, Jugada, archivo)
    with open("GanadorJugador1.txt", "w") as archivo:
        archivo.write("Las jugadas ganadoras del primer jugador son:\n")
    with open("GanadorJugador1.txt", 'r') as archivo:
        Primer = True
        for linea in archivo:
            if Primer:
                Primer = False
                continue 
            Cadena = linea.strip() 
            if Ganador1er(Cadena) == 1:
                with open("GanadorJugador1.txt", "a") as archivo:
                    archivo.write(Cadena + "\n")
            else:
                pass 
    caminoalExito1 = CaminoAlExito('GanadorJugador1.txt')
    cambiar_colores_secuencia(caminoalExito1,'green')
elif Jugadores == 2:
    with open(archivoJugadas1, "w") as archivo:
        archivo.write("Sus posibles Jugadas son:\n")
    with open(archivoJugadas2, "w") as archivo:
        archivo.write("Sus posibles Jugadas son:\n")
    if Selector == 1 and Jugadores == 2:
        Jugada1 = input("Ingrese su jugada 1(Ejemplo: BBNBN):")
        Jugada2 = input("Ingrese su jugada 2(Ejemplo: BBNBN):")
    elif Selector == 2 and Jugadores == 2:
        TamJugada = input("Ingrese el tamaño de su jugada:")
        TamJugada = int(TamJugada)
        Jugada1 = generar_cadena_binaria(TamJugada)
        print("Jugador 1: " + Jugada1)
        Jugada2 = generar_cadena_binaria(TamJugada)
        print("Jugador 2: " + Jugada2)
    elementoVacio = "N"
    Jugada1 = Jugada1 + elementoVacio
    Jugada2 = Jugada2 + elementoVacio
    estado1 = [1]
    estado2 = [4]
    #Jugador1
    with open("PosiblesJugadasJug1.txt", "a") as archivo1:
        generar_arbol(estado1, Jugada1, archivo1)
    #Jugador2
    with open("PosiblesJugadasJug2.txt", "a") as archivo2:
        generar_arbol(estado2, Jugada2, archivo2)
    #Definimos las jugadas ganadoras
    with open("GanadorJugador1.txt", "w") as archivo:
        archivo.write("Las jugadas ganadoras del primer jugador son:\n")
    with open("PosiblesJugadasJug1.txt", 'r') as archivo:
        Primer = True
        for linea in archivo:
            if Primer:
                Primer = False
                continue 
            Cadena = linea.strip() 
            if Ganador1er(Cadena) == 1:
                with open("GanadorJugador1.txt", "a") as archivo:
                    archivo.write(Cadena + "\n")
            else:
                pass            

    with open("GanadorJugador2.txt", "w") as archivo:
        archivo.write("Las jugadas ganadoras del segundo jugador son:\n")
    with open("PosiblesJugadasJug2.txt", 'r') as archivo:
        Primer = True
        for linea in archivo:
            if Primer:
                Primer = False
                continue 
            Cadena = linea.strip() 
            if Ganador2do(Cadena) == 1:
                with open("GanadorJugador2.txt", "a") as archivo:
                    archivo.write(Cadena + "\n")
            else:
                pass  
    caminoalExito1 = CaminoAlExito('GanadorJugador1.txt')
    caminoalExito2 = CaminoAlExito('GanadorJugador2.txt')
    cambiar_colores_secuencia(caminoalExito1,'green')
    cambiar_colores_secuencia(caminoalExito2,'red')

ventana.deiconify()
ventana.mainloop()
print("Termine llorando :(")
