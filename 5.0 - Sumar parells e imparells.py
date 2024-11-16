num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50] # Llista de números
parells = []    # Acumula números parells
imparells = []  # Acumula números imparells
sumaparells = 0    # Guarda la suma de números parells
sumaimparells = 0   # Guarda suma de números imparells

for i in num:  # Comproba cual es el número següent 
    if i % 2 == 0:
        parells.append(i)   # Sí el número es parell s'afegeix a la llista
        sumaparells += i    # Acumula la suma dels parells y la suma a la i   
    else:
        imparells.append(i)   # Sí el números es imparell s'afegeix a la llista                                
        sumaimparells += i    # Acumula la suma dels imparells y la suma a la i   
    # Imprimeix les sumes de cada iteració dels parells i dels imparells
    print(f"Números parells {sumaparells} Números imparells {sumaimparells}")   