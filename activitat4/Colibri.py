
from Cotxe import Cotxe 

class Colibri(Cotxe):
    # Constructor
    def __init__(self, tamany, velocitat, color, anys, nom):
        # Cridem directament al constructor de la classe (Cotxe)
        Cotxe.__init__(self, tamany, velocitat, color, anys, nom)
        # No cal redefinir els atributs, ja que Cotxe els gestiona.       