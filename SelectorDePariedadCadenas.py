"""
Desarrollado por Rosales Benuhmea Aldo
4to Programa: Protocolo
"""
import random
import os
import time
import networkx as nx
import matplotlib.pyplot as plt

def limpiar_terminal():
    os.system("cls")

def ClasificadorPareidad(Cadena_binaria):
    estado = 0
    for bit in Cadena_binaria:
        elemento = bit
        if estado == 0 and elemento == "0":
            estado = 1
        elif estado == 0 and elemento == "1":
            estado = 2
        elif estado == 1 and elemento == "0":
            estado = 0
        elif estado == 1 and elemento == "1":
            estado = 3
        elif estado == 2 and elemento == "0":
            estado = 3
        elif estado == 2 and elemento == "1":
            estado = 0
        elif estado == 3 and elemento == "0":
            estado = 2
        elif estado == 3 and elemento == "1":
            estado = 1
    if estado == 0:
        #print("Si Cumple :)")
        Valor = 1
    else:
        #print("No cumple :(")
        Valor = 0
    return Valor

def generar_cadena_binaria():
    cadena = ''.join(str(random.randint(0, 1)) for _ in range(64))
    cadena = str(cadena)
    return cadena

def graficar_Automata():
    G = nx.DiGraph()

    G.add_nodes_from(['q0', 'q1', 'q2', 'q3'])

    G.add_edge('q0', 'q1', label='0')
    G.add_edge('q1', 'q0', label='0')
    G.add_edge('q2', 'q3', label='0')
    G.add_edge('q3', 'q2', label='0')
    G.add_edge('q0', 'q2', label='1')
    G.add_edge('q2', 'q0', label='1')
    G.add_edge('q1', 'q3', label='1')
    G.add_edge('q3', 'q1', label='1')

    pos = {
        'q0': (-1, 0.5),
        'q1': (1, 0.5),
        'q2': (-1, -0.5),
        'q3': (1, -0.5)
    }

    node_sizes = {
        'q0': 2000,
        'q1': 1000,
        'q2': 1000,
        'q3': 1000
    }

    node_colors = {
        'q0': 'turquoise',
        'q1': 'lightblue',
        'q2': 'lightblue',
        'q3': 'lightblue'
    }

    labels = {(i, j): G[i][j]['label'] for i, j in G.edges()}
    nx.draw(G, pos, with_labels=True, node_size=[node_sizes[n] for n in G.nodes], node_color=[node_colors[n] for n in G.nodes])

    plt.annotate(
        "start",
        xy=(-1, 0.5),
        xytext=(-1, 1),
        arrowprops=dict(arrowstyle="-", color="black")
    )

    plt.plot([1.5, 1.5], [-1.5, 1.5], color='black', linestyle='-', linewidth=2)

    plt.plot([-1.5, -1.5], [-1.5, 1.5], color='black', linestyle='-', linewidth=2)

    plt.plot([-1.5, 1.5], [1.5, 1.5], color='black', linestyle='-', linewidth=2)

    plt.plot([-1.5, 1.5], [-1.5, -1.5], color='black', linestyle='-', linewidth=2)

    circle1 = plt.Circle((2.5, 0.75), 0.2, color='turquoise', ec='black')
    circle2 = plt.Circle((2.5, -0.75), 0.2, color='turquoise', ec='black')

    plt.gca().add_patch(circle1)
    plt.gca().add_patch(circle2)

    plt.text(2.5, 0.75, "Ready", ha='center', va='center', fontsize=12)
    plt.text(2.5, -0.75, "Sending", ha='center', va='center', fontsize=12)

    midpoint_x = (2.5 + 2.5) / 2
    midpoint_y = (0.75 + (-0.75)) / 2

    plt.annotate("Data In", xy=(midpoint_x, midpoint_y), ha='center', va='center', fontsize=12, color="black")

    plt.plot([2.5, 2.5], [0.55, -0.55], color='black', linestyle='-', linewidth=2)

    plt.annotate("", xy=(1.5, 0.75), xytext=(2.3, 0.75), arrowprops=dict(arrowstyle="<-", color="black"))

    plt.annotate("", xy=(2.3, -0.75), xytext=(1.5, -0.75), arrowprops=dict(arrowstyle="<-", color="black"))

    circle_arrow_x = 2.5
    circle_arrow_y = -0.85  
    circle_radius = 0.2
    plt.annotate(
        "",
        xy=(circle_arrow_x, circle_arrow_y - circle_radius), 
        xytext=(circle_arrow_x + circle_radius, circle_arrow_y),  
        arrowprops=dict(arrowstyle="->, head_width=0.1, head_length=0.1", color="black")
    )

    plt.annotate(
        "start",
        xy=(2.5, 0.75),
        xytext=(2.5, 1.5),
        arrowprops=dict(arrowstyle="-", color="black")
    )

    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.axis('off')
    plt.show()


limpiar_terminal()
n = 1000000

archivoPrueba = "DatosPrueba.txt"
archivoAceptados = "DatosAceptado.txt"
archivoRechazados = "DatosRechazados.txt"
with open(archivoAceptados, 'w') as archivo:
    archivo.truncate(0)
with open(archivoRechazados, 'w') as archivo:
    archivo.truncate(0)
contador = 0
Interruptor = 1
while Interruptor == 1:
    contador = contador + 1  
    print(f"Prueba {contador}")  
    with open(archivoPrueba, "w") as archivo:
            archivo.write("Su universo: {E\n")

    with open(archivoAceptados, "a") as archivo:
            archivo.write("Su universo prueba " + str(contador)+ ": {E\n")

    with open(archivoRechazados, "a") as archivo:
            archivo.write("Su universo prueba " + str(contador)+ ": {E\n")

    for i in range (1,n):

        with open(archivoPrueba, "a") as archivo:
                archivo.write(generar_cadena_binaria() + "\n")
        i = i+1
        
    print("Cadenas Generadas")
    print("Pausa iniciada")
    time.sleep(2)
    print("Empieza a Clasificar")

    with open(archivoPrueba, 'r') as archivo:
        Primer = True
        for linea in archivo:
            if Primer:
                Primer = False
                continue 
            Cadena = linea.strip() 
            if ClasificadorPareidad(Cadena) == 1:
                with open(archivoAceptados, "a") as archivo:
                    archivo.write(Cadena + "\n")
            else:
                with open(archivoRechazados, "a") as archivo:
                    archivo.write(Cadena + "\n")             

    with open(archivoAceptados, "a") as archivo:
        archivo.write("}\n")

    with open(archivoRechazados, "a") as archivo:
        archivo.write("}\n")  
    print("Termine de Clasificar, al cerrar la imagen se reiniciara el automata")  
    graficar_Automata()
    Interruptor  = random.choice([0, 1])
print(f"Termino el programa y se repitio {contador} veces")



