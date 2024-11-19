
num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]   # Llista de números
parells = []    # Acumula números parells
imparells = []  # Acumula números imparells

for i in num:  # Comproba quien es el número següent imparell
    if i % 2 == 0:  # Separa els parells dels imparells 
        parells.append(i)   # Sí el números es parell s'afegeix a la llista
    else:
        imparells.append(i)   # Sí el números es imparell s'afegeix a la llista                                
    print(f"Números parells {parells} Números imparells {imparells}")   # i imprimeix els imparells i després els parells
    