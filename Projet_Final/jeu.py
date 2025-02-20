import time
from presentation import *
from stanley import *
from Ennemis import *
from guepe import *
from chenilleG import *
from chenilleD import *
from araigneeG import *
from araigneeD import *

class Jeu:
    def __init__(self):
        self.presentation = Presentation()   # attribut pour la couche présentation
        self.stanley = Stanley()             # attribut pour Stanley
        # ...                                 # attributs pour les ennemis, le score, ...
        self.amis = [Constantes.NORMAL] * 5
        self.ennemis = Ennemis()
        self.guepe = None
        self.echec = 0
        self.score = 0
        self.chenilleG = []
        self.chenilleD = []
        self.araigneeG = []
        self.araigneeD = []


        # ----------------------------------------------------------------------------
    # méthode qui contient la boucle principale du jeu
    def demarrer(self):
        while True:
            # le code de gestion du déplacement des ennemis et des collisions va venir ici ...
            self.gererGuepe()
            self.gererChenilleG()
            self.gererChenilleD()
            self.gererAraigneeG()
            self.gererAraigneeD()

            #type_ennemi = Constantes.CHENILLE_D

            #Afficher la guepe
            if type_ennemi == Constantes.GUEPE:
                if self.guepe is None:
                    self.guepe = Guepe()

            #Afficher la chenille G
            elif type_ennemi == Constantes.CHENILLE_G:
                NouvelleChenilleG = chenilleG()
                self.chenilleG.append(NouvelleChenilleG)

            # Afficher la chenille D
            elif type_ennemi == Constantes.CHENILLE_D:
                NouvelleChenilleD = chenilleD()
                self.chenilleD.append(NouvelleChenilleD)

            # Afficher les araignée G
            elif type_ennemi == Constantes.ARAIGNEE_G:
                NouvelleAraigneeG = araigneeG()
                self.araigneeG.append(NouvelleAraigneeG)

            # Afficher les araignés D
            elif type_ennemi == Constantes.ARAIGNEE_D:
                NouvelleAraigneeD = araigneeD()
                self.araigneeD.append(NouvelleAraigneeD)


            # le code de génération des ennemis va venir ici ...

            if self.echec == 3 :
                self.presentation.attendreFermetureFenetre()
            # récupérer l'événement du joueur et changer l'état de Stanley

            self.stanley.actualiserEtat(self.presentation.lireEvenement())

            # mettre à jour l'image à l'écran

            self.actualiserEcran()

            # attendre 100 millisecondes (délai de référence)

            time.sleep(0.1)

    # ----------------------------------------------------------------------------
    # méthode qui met à jour l'image du jeu à l'écran

    def gererGuepe(self):

        if self.guepe is not None:
            self.guepe.actualiserEtat()
            if self.stanley.etat == Constantes.BAS and self.stanley.position == 2 and self.stanley.action == Constantes.SPRAY:
                self.guepe = None
                self.score += 1

            else:
                if self.guepe.etat == Constantes.TERMINE:
                    self.amis[4] = Constantes.TOUCHE
                    self.echec += 1
                    self.actualiserEcran()
                    time.sleep(1.5)
                    self.amis[4] = Constantes.NORMAL
                    self.guepe = None

    def gererChenilleG(self):
        i = 0
        while i < len(self.chenilleG):
            ch = self.chenilleG[i]
            ch.actualiserEtat()
            if (ch.position == 0 and self.stanley.etat == Constantes.HAUT and self.stanley.position == 0 and self.stanley.action == Constantes.SPRAY
                    or ch.position == 1 and self.stanley.etat == Constantes.HAUT and self.stanley.position == 0 and self.stanley.action == Constantes.SPRAY):
                self.chenilleG.pop(i)
                self.score += 1
            elif (ch.position == 2 and self.stanley.etat == Constantes.HAUT and self.stanley.position == 1 and self.stanley.action == Constantes.SPRAY
                  or ch.position == 3 and self.stanley.etat == Constantes.HAUT and self.stanley.position == 1 and self.stanley.action == Constantes.SPRAY):
                self.chenilleG.pop(i)
                self.score += 1
            else:
                i += 1


        if len(self.chenilleG) != 0:

            if self.chenilleG[0].etat == Constantes.TERMINE:
                self.amis[0] = Constantes.TOUCHE
                self.echec += 1
                self.actualiserEcran()
                time.sleep(1.5)
                self.amis[0] = Constantes.NORMAL
                self.chenilleG.pop(0)

    def gererChenilleD(self):
        i = 0
        while i < len(self.chenilleD):
            ch = self.chenilleD[i]
            ch.actualiserEtat()
            if (
                    ch.position == 1 and self.stanley.etat == Constantes.HAUT and self.stanley.position == 3 and self.stanley.action == Constantes.SPRAY
                    or ch.position == 2 and self.stanley.etat == Constantes.HAUT and self.stanley.position == 3 and self.stanley.action == Constantes.SPRAY):
                self.chenilleD.pop(i)
                self.score += 1
            elif (
                    ch.position == 3 and self.stanley.etat == Constantes.HAUT and self.stanley.position == 4 and self.stanley.action == Constantes.SPRAY
                    or ch.position == 4 and self.stanley.etat == Constantes.HAUT and self.stanley.position == 4 and self.stanley.action == Constantes.SPRAY):
                self.chenilleD.pop(i)
                self.score += 1
            elif (
                    ch.position == 5 and self.stanley.etat == Constantes.HAUT and self.stanley.position == 5 and self.stanley.action == Constantes.SPRAY
                    or ch.position == 6 and self.stanley.etat == Constantes.HAUT and self.stanley.position == 5 and self.stanley.action == Constantes.SPRAY):
                self.chenilleD.pop(i)
                self.score += 1
            else:
                i += 1

        if len(self.chenilleD) != 0:
            if self.chenilleD[0].etat == Constantes.TERMINE:
                self.amis[1] = Constantes.TOUCHE
                self.echec += 1
                self.actualiserEcran()
                time.sleep(1.5)
                self.amis[1] = Constantes.NORMAL
                self.chenilleD.pop(0)
    def gererAraigneeG(self):
        i = 0
        while i < len(self.araigneeG):
            ar = self.araigneeG[i]
            ar.actualiserEtat()
            if ar.position == 4 and self.stanley.etat == Constantes.BAS and self.stanley.position == 0 and self.stanley.action == Constantes.SPRAY:
                self.araigneeG.pop(i)
                self.score += 1
            else:
                i += 1

        if len(self.araigneeG) != 0:
            if self.araigneeG[0].etat == Constantes.TERMINE:
                self.amis[2] = Constantes.TOUCHE
                self.echec += 1
                self.actualiserEcran()
                time.sleep(1.5)
                self.amis[2] = Constantes.NORMAL
                self.araigneeG.pop(0)

    def gererAraigneeD(self):
        i = 0
        while i < len(self.araigneeD):
            ar = self.araigneeD[i]
            ar.actualiserEtat()
            if ar.position == 0 and self.stanley.etat == Constantes.BAS and self.stanley.position == 3 and self.stanley.action == Constantes.SPRAY:
                self.araigneeD.pop(i)
                self.score += 1
            else:
                i += 1

        if len(self.araigneeD) != 0:
            if self.araigneeD[0].etat == Constantes.TERMINE:
                self.amis[3] = Constantes.TOUCHE
                self.echec += 1
                self.actualiserEcran()
                time.sleep(1.5)
                self.amis[3] = Constantes.NORMAL
                self.araigneeD.pop(0)

    def actualiserEcran(self):
        self.presentation.effacerImageInterne()

        self.presentation.afficherStanley(self.stanley.etat, self.stanley.position,
                                          self.stanley.action)

        #Amis
        for position, etat in enumerate(self.amis):
            self.presentation.afficherAmi(position, etat)

        #Ennemis
        if self.guepe is not None:
            self.presentation.afficherGuepe(self.guepe.position)

        if len(self.chenilleG) != 0:
            for i in self.chenilleG:
                self.presentation.afficherChenilleG(i.position)

        if len(self.chenilleD) != 0:
            for i in self.chenilleD:
                self.presentation.afficherChenilleD(i.position)

        if len(self.araigneeG) != 0:
            for i in self.araigneeG:
                self.presentation.afficherAraigneeG(i.position)

        if len(self.araigneeD) != 0:
            for i in self.araigneeD:
                self.presentation.afficherAraigneeD(i.position)

        self.presentation.afficherEchecs(self.echec)
        self.presentation.afficherScore(self.score)
        self.presentation.actualiserFenetreGraphique()


