
num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]   # llista de numeros
imparells = []  # acumula numeros imparells
parells = []    # acumula numeros parells

for i in num:  # comproba quien es el numero següent imparell
    if i % 2 == 0:  # separa els parells dels imparells 
        parells.append(i)   # si el numeros es parell s'afegeix a la llista
    else:
        imparells.append(i)   # si el numeros es imparell s'afegeix a la llista                                
    print(f"Numeros imparells {imparells} Numeros parells {parells}")   # i imprimeix els imparells i després els parells
    