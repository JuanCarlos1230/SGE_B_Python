
minim = 100    # Variable de valor minim   
numero = 280   # Variable del número que es busca i es dintre del rang  

while (minim <= 400):   # El rang dels números de 100 - 400
    #print(minim);  #(Es comenta per evitar tota el buble del 100 al 400)
    minim = minim + 1   #   Va suman 1 al 100 fins arribar a 400 
if (numero >= 100 and numero <= 400):   # Comprovem si el número hi es dins del rang
        print(f"El número {numero} esta drintre del rang");   # Imprimeix el número que hi es dintre del rang               
else:
    print(f"El número {numero} no hi esta drintre del rang");   # Imprimeix el número que no hi es dintre del rang
                            