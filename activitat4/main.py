
# De l'arxiu cotxe impotem la classe cotxe.     
from Cotxe import Cotxe 
# Importem Colibri de l'arxiu Colibri.
from Colibri import Colibri

# Aquestes son les tres instancies de cotxe.
cotxe_1 = Cotxe(tamany = "Berlina", color = "Vermell", nom = "Seat Leon", velocitat = 240, anys = 8)
cotxe_2 = Cotxe(tamany = "Petit", color = "Azul", nom = "Ford fiesta", velocitat = 220, anys = 5)
cotxe_3 = Cotxe(tamany = "Familiar", color = "Negro", nom = "Renault Capture", velocitat = 240, anys = 2)

# Mostrem 3 getters de la primera instancia de Cotxe (cotxe_1)
print("Mostrem 3 getters de l'instancia cotxe_1:")
print(cotxe_1.getTamany())
print(cotxe_1.getColor())
print(cotxe_1.getNom())

# Amb els setters, modifico 2 atributs de cotxe_2 
cotxe_2.setTamany("Familiar") 
cotxe_2.setColor("Blanc")

# Amb els getters mostrem els atributs modificats de cotxe_2
print()
print("Mostrem 2 atributs dels getters modificats amb els setters:") 
print(cotxe_2.getTamany())
print(cotxe_2.getColor())

# Amb aquest print deixo una linia en blanc per separar cotxe de colibrí
print()

# Aquestes son les tres instancies de colibrí 
colibri_1 = Cotxe(tamany = "Petit", color = "Vermell", nom = "Archilochus", velocitat = 100, anys = 2)
colibri_2 = Cotxe(tamany = "Petit", color = "Verd", nom = "Trochilus", velocitat = 60, anys = 4)
colibri_3 = Cotxe(tamany = "Mitja", color = "Groc", nom = "Thalassinus", velocitat = 60, anys = 2)

# Mostrem 4 getters de la primera instancia de colibrí (colibrí_1)
print("Mostrem 4 getters de l'instancia colibrí_1:")
print(colibri_1.getTamany())
print(colibri_1.getColor())
print(colibri_1.getNom())
print(colibri_1.getAnys())

# Amb els setters modifico 2 atributs de colibrí_3 
colibri_3.setTamany("Gran") 
colibri_3.setNom("Colibrí bec d'espasa")

# Amb els getters mostrem els atributs modificats de colibrí_3 
print()
print("Mostrem 2 atributs dels getters modificats amb els setters:") 
print(colibri_3.getTamany())
print(colibri_3.getNom())

