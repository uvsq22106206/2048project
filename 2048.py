# Projet
# Auteurs : TROADEC-SAMOUR Mariam, TAIBI Yanis, GUEHO Yohan

# Importation des modules

import tkinter as tk
import random

from numpy import save

# Constantes et variables

LARGEUR = 500
HAUTEUR = 800

# Fonctions

def Right():# empiler les lignes vers la droite
    pass

def Left():# empiler les lignes vers la gauche
    pass

def Down():# empiler les lignes vers le bas
    pass

def Up():# empiler les lignes vers le haut
    pass

def Play():# commencer une partie (mettre deux tuile (2 ou 4) de manière aléatoire sur la grille)
    pass

def Exit():# finir la partie et afficher le score (somme des valeurs des cases)
    pass

def Save():# sauvegarder une partie en cours dans un fichier texte
    pass

def Load():# charger une partie enregistrée dans un fichier
    pass

# Programme principal

# Widgets

root = tk.Tk()
mainCanvas = tk.Canvas(root, bg="black", width=LARGEUR, height=HAUTEUR)
gameArea = mainCanvas.create_rectangle(LARGEUR-480, HAUTEUR-780, LARGEUR-20, HAUTEUR-320, fill="red")

# Création des cases

# Boutons

boutonRight = tk.Button(root, text="Right", command=Right)
boutonRight.grid(row=6, column=3, rowspan=2)

boutonLeft = tk.Button(root, text="Left", command=Left)
boutonLeft.grid(row=6, column=0, rowspan=2)

boutonUp = tk.Button(root, text="Up", command=Up)
boutonUp.grid(row=6, column=1, columnspan=2)

boutonDown = tk.Button(root, text="Down", command=Down)
boutonDown.grid(row=7, column=1, columnspan=2)

boutonPlay = tk.Button(root, text="Play", command=Play)
boutonPlay.grid(row=4, column=0, columnspan=2)

boutonExit = tk.Button(root, text="Exit", command=Exit)
boutonExit.grid(row=4, column=2, columnspan=2)

boutonSave = tk.Button(root, text="Save", command=Save)
boutonSave.grid(row=5, column=2, columnspan=2)

boutonLoad = tk.Button(root, text="Load", command=Load)
boutonLoad.grid(row=5, column=0, columnspan=2)



mainCanvas.grid()
root.mainloop()
