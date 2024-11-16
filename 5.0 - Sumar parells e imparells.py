num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50] # llista de numeros
imparells = []  # acumula numeros imparells
parells = []    # acumula numeros parells
sumaparells = 0    # guarda la suma de numeros parells
sumaimparells = 0   # guarda suma de numeros imparells

for i in num:  # comproba quien es el numero següent imparell
    if i % 2 == 0:
        parells.append(i)   # si el numeros es parell s'afegeix a la llista
        sumaparells += i    # acumula la suma dels parells y la suma a la i   
    else:
        imparells.append(i)   # si el numeros es imparell s'afegeix a la llista                                
        sumaimparells += i    # acumula la suma dels imparells y la suma a la i   
    # imprimeix les sumes de cada iteracio dels imparells i dels parells
    print(f"Numeros imparells {sumaimparells} Numeros parells {sumaparells}")   