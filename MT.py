"""
Desarrollado por Rosales Benuhmea Aldo
El programa de la máquina de Turing debe de reconocer el lenguaje {0^n1^n | n>= 1}. La máquina de Turing se encuentra en el libro de John Hopcroft (ejercicio 8.2, segunda edición). 

1. El programa debe de recibir una cadena definida por el usuario o que sea determinada automáticamente por la máquina, una cadena de longitud como máximo de 1000 caracteres.
2. La salida del programa debe ser a un archivo de texto y utilizando descripciones instantáneas en cada paso de la computación.
3. Animar la máquina de Turing con cadenas menores iguales a 16 caracteres.
"""
import os
import random

    
def limpiar_terminal():
    os.system("cls")

def MaquinadeTuringAni(cadena):
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import matplotlib.animation as animation

    def animacion_maquina_turing(secuencia_cambios, entrada, cadenas):
        estados = {0: (0, 0), 1: (2, 0), 2: (4, 0), 3: (6, 0), 4: (8, 0)}
        transiciones = [(0, 1), (1, 2), (2, 3), (3, 4)]

        def actualizar_animacion(i, ax, circulos, flechas, texto_salida):
            ax.clear()

            for estado, (x, y) in estados.items():
                radio = 0.8 if estado == secuencia_cambios[i] else 0.5 
                color = 'green' if estado == secuencia_cambios[i] else 'white' 
                circulo = patches.Circle((x, y), radius=radio, edgecolor='black', facecolor=color)
                ax.add_patch(circulo)
                ax.text(x, y, estado, ha='center', va='center', fontsize=12)

            # Dibujar flechas para las transiciones
            for transicion in transiciones:
                origen, destino = transicion
                x_origen, y_origen = estados[origen]
                x_destino, y_destino = estados[destino]

                dx = x_destino - x_origen
                dy = y_destino - y_origen
                flecha = ax.arrow(x_origen, y_origen, dx, dy, head_width=0.1, head_length=0.2, fc='black', ec='black')
                flechas[transicion] = flecha

            ax.axis('equal')
            ax.axis('off')

            texto_salida.set_text(f"Entrada: {entrada[i]}   Cadena: {cadenas[i]}")

        fig, (ax_animacion, ax_texto) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]})
        circulos = {}
        flechas = {}

        for estado, (x, y) in estados.items():
            radio = 0.8 if estado == secuencia_cambios[0] else 0.5 
            color = 'green' if estado == secuencia_cambios[0] else 'white' 
            circulo = patches.Circle((x, y), radius=radio, edgecolor='black', facecolor=color)
            ax_animacion.add_patch(circulo)
            ax_animacion.text(x, y, estado, ha='center', va='center', fontsize=12)


        for transicion in transiciones:
            origen, destino = transicion
            x_origen, y_origen = estados[origen]
            x_destino, y_destino = estados[destino]

            dx = x_destino - x_origen
            dy = y_destino - y_origen
            flecha = ax_animacion.arrow(x_origen, y_origen, dx, dy, head_width=0.1, head_length=0.2, fc='black', ec='black')
            flechas[transicion] = flecha

        texto_salida = ax_texto.text(0.5, 0.5, "", ha='center', va='center', fontsize=12, color='black')
        ax_texto.axis('off')

        ani = animation.FuncAnimation(fig, actualizar_animacion, frames=len(secuencia_cambios),
                                    fargs=(ax_animacion, circulos, flechas, texto_salida),
                                    interval=1000, repeat=False)
        plt.title('Maquina de Turnig')
        plt.show()
    with open("descripcion_instantanea_MT.txt", "w") as archivo:
        archivo.write('Evaluación de la Maquina de Turing(IDs):\n')
    
    estado = 0
    posicion = 0
    resultado = 1
    cadena = list(cadena) + ['']
    secuencia = []
    entradas = []
    cadenas = []
    print(cadena)
    
    while True:
        secuencia.append(estado)
        entradas.append(cadena[posicion])
        cadenas.append(''.join(cadena))
        descripcion_instantanea = f"q{estado}, Entada:{cadena[posicion]}, {cadena}\n"
        with open("descripcion_instantanea_MT.txt", "a") as archivo:
            archivo.write(descripcion_instantanea)

        if estado == 0:
            if posicion >= len(cadena):
                resultado = 0
                break
            
            if cadena[posicion] == '0':
                cadena[posicion] = 'X'
                posicion += 1
                estado = 1
                
            elif cadena[posicion] == 'Y':
                posicion += 1
                estado = 3
                
            else:
                resultado = 0
                break
        elif estado == 1:
            if posicion >= len(cadena):
                resultado = 0
                break
            
            if cadena[posicion] == '0':
                posicion += 1
                
            elif cadena[posicion] == '1':
                cadena[posicion] = 'Y'
                posicion -= 1
                estado = 2
                
            elif cadena[posicion] == 'Y':
                posicion += 1
                
            else:
                resultado = 0
                break
        elif estado == 2:
            if posicion >= len(cadena):
                resultado = 0
                break
            
            if cadena[posicion] == '0':
                posicion -= 1
                
            elif cadena[posicion] == 'X':
                posicion += 1
                estado = 0

            elif cadena[posicion] == 'Y':
                posicion -= 1
                
            else:
                resultado = 0
                break
        elif estado == 3:
            if cadena[posicion] == '':
                secuencia.append(4)
                entradas.append('B')
                cadena[posicion] = 'B'
                cadenas.append(''.join(cadena))
                break
                
            elif cadena[posicion] == 'Y':
                posicion += 1
            else:
                resultado = 0
                break
    animacion_maquina_turing(secuencia, entradas, cadenas)
    return resultado


def MaquinadeTuring(cadena):
    with open("descripcion_instantanea_MT.txt", "w") as archivo:
        archivo.write('Evaluación de la Maquina de Turing(IDs):\n')
    
    estado = 0
    posicion = 0
    resultado = 1
    cadena = list(cadena) + ['']
    print(cadena)
    
    while True:
        descripcion_instantanea = f"q{estado}, Entada:{cadena[posicion]}, {cadena}\n"
        with open("descripcion_instantanea_MT.txt", "a") as archivo:
            archivo.write(descripcion_instantanea)

        if estado == 0:
            if posicion >= len(cadena):
                resultado = 0
                break
            
            if cadena[posicion] == '0':
                cadena[posicion] = 'X'
                posicion += 1
                estado = 1
                
            elif cadena[posicion] == 'Y':
                posicion += 1
                estado = 3
                
            else:
                resultado = 0
                break
        elif estado == 1:
            if posicion >= len(cadena):
                resultado = 0
                break
            
            if cadena[posicion] == '0':
                posicion += 1
                
            elif cadena[posicion] == '1':
                cadena[posicion] = 'Y'
                posicion -= 1
                estado = 2
                
            elif cadena[posicion] == 'Y':
                posicion += 1
                
            else:
                resultado = 0
                break
        elif estado == 2:
            if posicion >= len(cadena):
                resultado = 0
                break
            
            if cadena[posicion] == '0':
                posicion -= 1
                
            elif cadena[posicion] == 'X':
                posicion += 1
                estado = 0

            elif cadena[posicion] == 'Y':
                posicion -= 1
                
            else:
                resultado = 0
                break
        elif estado == 3:
            if cadena[posicion] == '':
                break
                
            elif cadena[posicion] == 'Y':
                posicion += 1
            else:
                resultado = 0
                break
    
    return resultado

"""
Estado Actual | Símbolo Leído | Nuevo Estado | Símbolo Escrito | Dirección
----------------------------------------------------------------------------
q0            | 0             | q1           | X               | R
q0            | Y             | q3           | Y               | R
----------------------------------------------------------------------------
q1            | 0             | q1           | 0               | R
q1            | 1             | q2           | Y               | L
q1            | Y             | q1           | Y               | R
----------------------------------------------------------------------------
q2            | 0             | q2           | 0               | L
q2            | X             | q0           | X               | R
q2            | Y             | q2           | Y               | L
----------------------------------------------------------------------------
q3            | ''            | q4           | B               | B
q3            | Y             | q3           | Y               | R
----------------------------------------------------------------------------
q4            |               |              |                 | 
"""


limpiar_terminal()

print("Programa para reconocer el lenguaje libre de contexto {0^n 1^n | n >= 1}")
print("1. Introducir de forma manual la cadena")
print("2. Generar de manera aleatoria una cadena binaria")

auto = int(input("Ingrese el numero de la opcion que desea visualizar: "))

if auto == 1:
    cadena = input("Ingrese la cadena binaria que desea comprobar: ")
    tam = len(cadena)
elif auto == 2:
    tam = random.randint(1, 1000)
    cadena = ''.join(random.choice('01') for _ in range(tam))
    print(f"Cadena generada aleatoriamente: {cadena}")
else:
    print("Opción no válida.")

if tam < 16:
    resultado = MaquinadeTuringAni(cadena)
    #Animar MT
else:
    resultado = MaquinadeTuring(cadena)

print("\nEvaluación del autómata(IDs):")

if resultado == 1:
    print("\nLa cadena pertenece al lenguaje.")
else:
    print("\nLa cadena no pertenece al lenguaje.")

