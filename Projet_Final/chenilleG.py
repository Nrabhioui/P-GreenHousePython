from constantes import Constantes

class chenilleG :
    def __init__(self):
        self.position = 4
        self.etat = Constantes.NORMAL
        self.delai_deplacement = 6

    def actualiserEtat(self):
        if self.etat == Constantes.NORMAL:
            if self.delai_deplacement > 0:
                self.delai_deplacement -= 1
            elif self.delai_deplacement == 0:
                if self.position > 0:
                    self.position -= 1
                    self.delai_deplacement = 6
                else:
                    self.etat = Constantes.TERMINE


