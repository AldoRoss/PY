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
        print("Si Cumple :)")
        Valor = 1
    else:
        print("No cumple :(")
        Valor = 0
    return Valor

cadena = input("ingrese su cadena:")
Cumple = ClasificadorPareidad(cadena)
print(Cumple)
 