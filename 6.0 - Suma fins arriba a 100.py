
suma = 0    # Variabla que acumula la suma
numero = 0  # Sí inicialitza a 0 perque no hi ha numero encara

while (suma <= 100):   # Sí el número es més petit o igual a 10 el bucle continua
    numero = numero + 1
    suma = suma + numero
    print(f"Aquest es el valor del número en aquesta iteració {suma}")   # Imprimeix el número per cada iteració
    