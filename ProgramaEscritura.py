"""
Desarrollado por Rosales Benuhmea Aldo
Programa evolutivo de rescritura
"""
import difflib
import tkinter as tk
from tkinter import ttk

PalabraEsp = ["carro", "casa", "perro", "tarjeta", "juego"]
PalabraIn = ["car", "house", "dog", "card", "game"]

def Ingresar_Palabra(Palabra,ListaEsp,ListaIng,significado):
    significado = significado
    ListaEsp.append(Palabra)
    ListaIng.append(significado)
    mensaje="Se agrego la parabra con exito"
    return (ListaEsp,ListaIng,mensaje) 

def Palabra_Similar(palabraSim, ListaEsp):
    # Encontrar las palabras más similares en la lista
    indice_maximo = -1  # Inicializamos con un valor que no es un índice válido
    similitud_maxima = 0

    for i, palabra in enumerate(ListaEsp):
        similitud = difflib.SequenceMatcher(None, palabraSim, palabra).ratio()
        
        if similitud > similitud_maxima:
            similitud_maxima = similitud
            indice_maximo = i

    if indice_maximo != -1:
        SiHay = 1
    else:
        SiHay = 0
        indice_maximo = -1
    return SiHay, indice_maximo



def programa_principal(Palabra, PalabraEsp, PalabraIn, significado):
    mensaje = ""
    mensaje2 = ""
    ingles = ""
    español = ""
    if Palabra == '':
        mensaje = "Ingrese una palabra en el cuadro de español"
    else:
        try:
            indice = PalabraEsp.index(Palabra)
            mensaje = "Palabra Encontrada"
            ingles = PalabraIn[indice]
            español = PalabraEsp[indice]
        except ValueError:
            SiHay, palabraCercana = Palabra_Similar(Palabra, PalabraEsp)
            if SiHay == 1:
                mensaje2 = "Prueba con la palabra " + PalabraEsp[palabraCercana]
                try:
                    indice = PalabraIn.index(Palabra)
                    español = PalabraEsp[indice]
                    ingles = Palabra
                except ValueError:
                    if significado != '':
                        español = Palabra
                        # Actualiza las listas y obtén el mensaje
                        (PalabraEsp, PalabraIn, mensaje) = Ingresar_Palabra(Palabra, PalabraEsp, PalabraIn, significado)  # Agrega el mensaje de ingreso
                    else:
                        español = Palabra
                        mensaje = "Ingresa tu palabra en el cuadro de significado"
            else:
                try:
                    indice = PalabraIn.index(Palabra)
                    mensaje = "Su palabra esta en ingles"
                    español = PalabraEsp[indice]
                    ingles = Palabra
                except ValueError:
                    if significado != '':
                        # Actualiza las listas y obtén el mensaje
                        (PalabraEsp, PalabraIn, nuevo_mensaje) = Ingresar_Palabra(Palabra, PalabraEsp, PalabraIn, significado)
                        mensaje = nuevo_mensaje  # Agrega el mensaje de ingreso
                    else:
                        español = Palabra
                        mensaje = "Ingresa tu palabra en el cuadro de significado"
                
    return mensaje, mensaje2, ingles, español

                

import tkinter as tk

def mostrar_ventana():
    # Crear la ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Traductor")
    ventana_principal.geometry("550x600")  # Aumentamos la altura de la ventana

    def Dale_bogeto():
        Palabra = entry1.get()
        significado = entry3.get()
        mensaje, mensaje2, ingles, español = programa_principal(Palabra, PalabraEsp, PalabraIn, significado)
        label_resultado.config(text=mensaje)
        label_resultado2.config(text=mensaje2)
        entry1.delete(0, tk.END)  # Clear the current text in entry1
        entry1.insert(0, español)
        entry2.delete(0, tk.END)  # Clear the current text in entry2
        entry2.insert(0, ingles)
        entry3.delete(0, tk.END)  # Clear the current text in entry3
    
    def salir():
        ventana_principal.destroy() 

    def imprimir_listas():
        # Destruye todos los widgets en la ventana principal
        for widget in ventana_principal.winfo_children():
            widget.destroy()

        # Crear una etiqueta para mostrar las listas PalabraEsp y PalabraIn
        lista_palabras = tk.Label(ventana_principal, text="Su diccionario esta conformado por:\n", font=("Arial", 12))
        lista_palabras.pack(pady=10)

        # Imprime las listas PalabraEsp y PalabraIn
        for i in range(len(PalabraEsp)):
            lista_palabras.config(text=lista_palabras.cget("text") + f"{PalabraEsp[i]} : {PalabraIn[i]}\n")

        # Botón para volver a la pantalla principal
        boton_volver = tk.Button(ventana_principal, text="Salir", font=("Arial", 12), fg="red", command=salir)
        boton_volver.pack(pady=15)

    # Título con fuente de tamaño 20
    titulo = tk.Label(ventana_principal, text="Programa de Escritura Evolutivo", font=("Arial", 20), fg="#000080")
    titulo.pack(pady=30)

    # Texto secundario centrado
    texto_secundario = tk.Label(ventana_principal, text="Escriba en el cuadro que desea traducir", font=("Arial", 12))
    texto_secundario.pack(pady=1)

    # Cuadro de texto 1
    label1 = tk.Label(ventana_principal, text="Español:", font=("Arial", 11))
    label1.pack(pady=10)
    entry1 = tk.Entry(ventana_principal, width=40)
    entry1.pack(pady=5)

    # Cuadro de texto 2
    label2 = tk.Label(ventana_principal, text="Ingles:", font=("Arial", 11))
    label2.pack(pady=10)
    entry2 = tk.Entry(ventana_principal, width=40)
    entry2.pack(pady=5)

    # Cuadro de texto 3
    label3 = tk.Label(ventana_principal, text="Significado:", font=("Arial", 11))
    label3.pack(pady=10)
    entry3 = tk.Entry(ventana_principal, width=40)
    entry3.pack(pady=5)

    # Etiqueta para mostrar el resultado
    label_resultado = tk.Label(ventana_principal, text="")
    label_resultado.pack(pady=4)
    label_resultado2 = tk.Label(ventana_principal, text="")
    label_resultado2.pack(pady=4)

    # Botón para mostrar el texto
    boton_mostrar = tk.Button(ventana_principal, text="Traducir", font=("Arial", 12), fg="#000080", command=Dale_bogeto)
    boton_mostrar.pack(pady=15)

    # Botón para mostrar el texto
    boton_mostrar = tk.Button(ventana_principal, text="Diccionario", font=("Arial", 12), fg="green", command=imprimir_listas)
    boton_mostrar.pack(pady=15)

    # Iniciar el bucle principal
    ventana_principal.mainloop()


mostrar_ventana()
