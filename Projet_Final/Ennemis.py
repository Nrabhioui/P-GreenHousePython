from random import *
from constantes import Constantes

class Ennemis:
    def __init__(self):
        self.delai_creation_ennemi = 16  # Initialisation du délai à 16
        self.types_ennemis = [Constantes.GUEPE, Constantes.CHENILLE_G, Constantes.CHENILLE_D, Constantes.ARAIGNEE_G, Constantes.ARAIGNEE_D]

    def actualiserEtat(self):
        if self.delai_creation_ennemi > 0:
            self.delai_creation_ennemi -= 1
            return Constantes.AUCUN_ENNEMI
        else:
            ennemi_a_creer = choice(self.types_ennemis) #choix aléatoire
            self.delai_creation_ennemi = self.nouveau_delai()  # Recharge du délai
            return ennemi_a_creer

    def nouveau_delai(self):
        # Génère un nouveau délai entre 10 et 15
        return randint(10, 15)
