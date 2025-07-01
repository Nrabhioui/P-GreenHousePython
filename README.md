# P-GreenHousePython

## Description

Ce projet est un jeu développé en Python avec Pygame, simulant la défense d’une serre contre des envahisseurs (guêpes, chenilles, araignées). Le joueur incarne Stanley, le gardien de la serre, et doit protéger les fleurs et le chat en éliminant les ennemis à l’aide d’un spray insecticide.

## Fonctionnalités principales

- **Déplacement et actions de Stanley** : Contrôle du personnage principal pour protéger les éléments de la serre.
- **Gestion d’ennemis variés** : Guêpes, chenilles (gauche/droite), araignées (gauche/droite), avec comportements spécifiques.
- **Système de score et d’échec** : Perte de points de vie si un ennemi atteint un ami, gain de score en éliminant les ennemis.
- **Animations et interface graphique** : Utilisation de nombreuses images pour l’affichage dynamique de la serre, des personnages et du score.

## Structure du projet

```
Projet_Final/
├── amis/                # Images des amis (fleurs, chat)
├── chiffres/            # Images des chiffres pour le score
├── ennemis/             # Images des ennemis (guêpe, chenille, araignée)
├── insecticide/         # Images du spray
├── stanley/             # Images de Stanley (différentes positions)
├── images/              # Images principales (greenhouse, icônes)
├── Ennemis.py           # Gestion des ennemis et de leur génération
├── araigneeD.py         # Classe araignée droite
├── araigneeG.py         # Classe araignée gauche
├── chenilleD.py         # Classe chenille droite
├── chenilleG.py         # Classe chenille gauche
├── constantes.py        # Constantes du jeu (états, types, etc.)
├── guepe.py             # Classe guêpe
├── jeu.py               # Logique principale du jeu
├── main.py              # Point d’entrée du jeu
├── presentation.py      # Gestion de l’affichage Pygame
├── stanley.py           # Classe Stanley (joueur)
```

## Installation

1. Installe Python 3.x.
2. Installe les dépendances :
   ```bash
   pip install pygame
   ```
3. Place toutes les images dans les dossiers correspondants (voir structure ci-dessus).

## Lancement du jeu

Dans le dossier `Projet_Final`, exécute :
```bash
python main.py
```

## Contrôles

- Les contrôles sont gérés par les événements clavier (flèches, espace) pour déplacer Stanley et utiliser le spray.

## Dépendances

- Python 3.x
- Pygame

## Auteurs

- Nassim
