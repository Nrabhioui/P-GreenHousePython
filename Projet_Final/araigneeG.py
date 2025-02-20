from constantes import Constantes

class araigneeG:
    def __init__(self):
        self.position = 0
        self.etat = Constantes.NORMAL
        self.delai_deplacement = 4

    def actualiserEtat(self):
        if self.etat == Constantes.NORMAL:
            if self.delai_deplacement > 0:
                self.delai_deplacement -= 1
            elif self.delai_deplacement == 0:
                if self.position < 4:
                    self.position += 1
                    self.delai_deplacement = 4
                else:
                    self.etat = Constantes.TERMINE