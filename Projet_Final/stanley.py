import pygame
from constantes import *

class Stanley:
    def __init__(self):
        self.etat = Constantes.BAS
        self.position = 1
        self.action = Constantes.NORMAL

    def actualiserEtat(self, evenement):
        if evenement == pygame.K_SPACE:
            if self.etat == Constantes.BAS and self.position != 1 or self.etat == Constantes.HAUT and self.position != 2:
                self.action = Constantes.SPRAY
        else:
            self.action = Constantes.NORMAL

            if self.etat == Constantes.BAS:
                if evenement == pygame.K_RIGHT:
                    if self.position < 3:
                        self.position += 1
                elif evenement == pygame.K_LEFT:
                    if self.position > 0:
                        self.position -= 1
                elif evenement == pygame.K_UP:
                    if self.position == 1 :
                        self.etat = Constantes.ECHELLE

            elif self.etat == Constantes.ECHELLE:
                if evenement == pygame.K_UP:
                    if self.position == 1:
                        self.position -= 1
                    elif self.position == 0:
                        self.etat = Constantes.HAUT
                        self.position = 2
                elif evenement == pygame.K_DOWN :
                    self.position += 1
                    if self.position == 2:
                        self.etat = Constantes.BAS
                        self.position = 1

            elif self.etat == Constantes.HAUT:
                if evenement == pygame.K_RIGHT:
                    if self.position < 5:
                        self.position += 1
                elif evenement == pygame.K_LEFT:
                    if self.position > 0:
                        self.position -= 1
                elif evenement == pygame.K_DOWN:
                    if self.position == 2 :
                        self.etat = Constantes.ECHELLE
                        self.position = 0
