from constantes import Constantes

class Guepe:
    def __init__(self):
        self.position = 0  # Position initiale de la guêpe
        self.etat = Constantes.NORMAL  # État initial de la guêpe
        self.delai_deplacement = 10  # Délai d'attente avant le prochain déplacement

    def actualiserEtat(self):
        if self.etat == Constantes.NORMAL:
            if self.delai_deplacement > 0:
                self.delai_deplacement -= 1
            elif self.delai_deplacement == 0:
                if self.position == 0:
                    self.position = 1
                    self.delai_deplacement = 10
                elif self.position == 1:
                    self.etat = Constantes.TERMINE