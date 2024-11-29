
class Cotxe:
    # Constructor
    def __init__(self, tamany, velocitat, color, anys, nom):
        #Atributs 
        self.tamany = tamany
        self.velocitat = velocitat
        self.color = color
        self.anys = anys
        self.nom = nom

    # Getters i Setters
    def getTamany(self): 
        return self.tamany
    def setTamany(self, new_tamany):
        self.tamany = new_tamany

    def getVelocitat(self):
        return self.velocitat
    def setVelocitat(self, new_velocitat):
        self.velocitat= new_velocitat
    
    def getColor(self):
        return self.color
    def setColor(self, new_color):
        self.color = new_color

    def getAnys(self):
        return self.anys
    def setAnys(self, new_anys):
        self.anys = new_anys

    def getNom(self):
        return self.nom
    def setNom(self, new_nom):
        self.nom = new_nom
        