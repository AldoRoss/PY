"""
Desarrollado por Rosales Benuhmea Aldo
Programar un autómata de pila que sirva para reconocer el lenguaje libre de contexto {0^n 1^n | n >= 1}.

Adicionalmente, el programa debe de contar con las siguientes características:

La cadena puede ser ingresada por el usuario o automáticamente. Si es aleatoriamente, la cadena no podrá ser mayor a 100,000 caracteres.
Mandar a un archivo y en pantalla la evaluación del autómata a través de descripciones instantáneas (IDs).
Animar el autómata de pila, solo si la cadena es menor igual a 10 caracteres.
En el reporte deben de estar pantallas del programa en ejecución de todas las características solicitadas.
"""
import os
import random
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
    
def limpiar_terminal():
    os.system("cls")

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0
    
    def no_esta_vacia(self):
        return not self.esta_vacia()

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None 

def evaluar_cadena(cadena):
    with open("descripcion_instantanea.txt", "w") as archivo:
            archivo.write('Evaluación del autómata(IDs):\n')
    pila = Pila()
    estado = 0
    descripcion_instantanea = f"q{estado}, Z, {cadena}, Z0"
    resultado = 1

    for elemento in cadena:
        # Estado Inicial
        if estado == 0:
            if elemento == '0':
                pila.apilar('X')
                estado = 1
            else:
                resultado = 0
        # Recibe los 0's
        elif estado == 1:
            if elemento == '0':
                pila.apilar('X')
            elif elemento == '1':
                pila.desapilar()
                estado = 2
            else:
                resultado = 0
        # Recibe los 1's
        elif estado == 2:
            if elemento == '1':
                if pila.no_esta_vacia():
                    pila.desapilar()
                else:
                    estado = 0
                    resultado = 0
            else:
                resultado = 0

        descripcion_instantanea = f"q{estado}, {pila.items[::-1]}, {cadena}, {elemento} \n"
        with open("descripcion_instantanea.txt", "a") as archivo:
            archivo.write(descripcion_instantanea)

    return estado == 2 and pila.esta_vacia() and resultado, descripcion_instantanea

def evaluar_cadena_ani(cadena):
    with open("descripcion_instantanea.txt", "w") as archivo:
            archivo.write('Evaluación del autómata(IDs):\n')
    pila = Pila()
    estado = 0
    descripcion_instantanea = f"q{estado}, Z, {cadena}, Z0"
    resultado = 1
    secuencia = []
    contador = 0 
    for elemento in cadena:
        # Estado Inicial
        if estado == 0:
            if elemento == '0':
                pila.apilar('X')
                contador = contador + 1
                estado = 1
            else:
                resultado = 0
                contador = contador - 1
            
        # Recibe los 0's
        elif estado == 1:
            if elemento == '0':
                pila.apilar('X')
                contador = contador + 1
            elif elemento == '1':
                pila.desapilar()
                contador = contador - 1
                estado = 2
            else:
                resultado = 0
        # Recibe los 1's
        elif estado == 2:
            if elemento == '1':
                if pila.no_esta_vacia():
                    pila.desapilar()
                    contador = contador - 1
                else:
                    estado = 0
                    resultado = 0
                    contador = contador - 1
            else:
                resultado = 0
                contador = contador - 1
        secuencia.append(contador)
        descripcion_instantanea = f"q{estado}, {pila.items[::-1]}, {cadena}, {elemento}\n"
        with open("descripcion_instantanea.txt", "a") as archivo:
            archivo.write(descripcion_instantanea)
        
    animarPila(secuencia)
    return estado == 2 and pila.esta_vacia() and resultado, descripcion_instantanea


def animarPila(secuencia):
    fig, ax = plt.subplots()

    white = (1, 1, 1)
    green = (0, 1, 0)
    red = (1, 0, 0)

    frames = []
    for i in range(10):
        rect = patches.Rectangle((0, i), 5, 1, linewidth=2, edgecolor='black', facecolor=white)
        ax.add_patch(rect)
        frames.append(rect)

    def CambioColor(frame):
        color = green
        time.sleep(2)
        if frame < len(secuencia):
            cabeza = secuencia[frame]
            #limpia la pila
            for k in range(10):
                frames[k].set_facecolor(white)
            if cabeza < 0:
                color = red
            for i in range(abs(cabeza)):
                frames[i].set_facecolor(color)
        return frames

    ani = animation.FuncAnimation(fig, CambioColor, frames=range(len(secuencia) + 2), init_func=lambda: frames, blit=True, interval=100, repeat=False)
    plt.title('Animación de la Pila')
    plt.axis('equal')
    plt.show()

limpiar_terminal()

print("Programa para reconocer el lenguaje libre de contexto {0^n 1^n | n >= 1}")
print("1. Introducir de forma manual la cadena")
print("2. Generar de manera aleatoria una cadena binaria")

auto = int(input("Ingrese el numero de la opcion que desea visualizar: "))

if auto == 1:
    cadena = input("Ingrese la cadena binaria que desea comprobar: ")
    tam = len(cadena)
elif auto == 2:
    tam = random.randint(1, 100)
    cadena = ''.join(random.choice('01') for _ in range(tam))
    print(f"Cadena generada aleatoriamente: {cadena}")
else:
    print("Opción no válida.")

if tam < 11:
    resultado, descripcion_instantanea = evaluar_cadena_ani(cadena)
else:
    resultado, descripcion_instantanea = evaluar_cadena(cadena)

print("\nEvaluación del autómata(IDs):")
print(descripcion_instantanea)

if resultado == 1:
    print("\nLa cadena pertenece al lenguaje.")
else:
    print("\nLa cadena no pertenece al lenguaje.")

