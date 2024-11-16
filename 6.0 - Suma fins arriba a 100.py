
suma = 0    # variables que acumula la suma
numero = 0  # Si inicialitza a 1 perque el numeros vagin de 1 a 10


while (suma <= 100):   # si el numero es més petit o igual a 10 el bucle contina
    numero = numero + 1
    suma = suma + numero
    print(f"Este el valor del nombres en esta iteración {suma}")   # imprimeix el numero per cada iteració
    