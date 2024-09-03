import random
from tkinter import Tk, Button, Label

class Window(Tk):

    def __init__(self):
        super().__init__()
        # Titre de la fenetre
        self.title("Sagesse")
        # Ajout d'un texte
        self.label = Label(text="Ils ne sont grands que parce que nous sommes à genoux. \n-La Boétie")
        self.label.pack()
        # Ajout d'un bouton
        self.button = Button(text="Fermer", command=self.handle_button_press)
        self.button.pack()

    # Gestion de l'evenement du bouton
    def handle_button_press(self):
        self.destroy()

# Creation de la fenetre
window = Window()
# Boucle principale
window.mainloop()


def lire_citation_aleatoire(citations):
    with open(citations, 'r', encoding='utf-8') as f:
        citations = f.readlines()
    return random.choice(citations).strip()


def formater_citation(citations):
    # Séparer la citation et l'auteur
    if "-" in citations:
        texte, auteur = citations.split("-", 1)
    else:
        texte, auteur = citations, ""

    mots = texte.split()
    cit_form = ""
    for i in range(len(mots)):
        cit_form += mots[i] + " "
        if (i + 1) % 3 == 0:
            cit_form += "\n"

    # Ajouter l'auteur avec un saut de ligne
    if auteur:
        cit_form += "\n-" + auteur

    return cit_form


# Utilisation des fonctions
fichier = 'citations.txt'
citation = lire_citation_aleatoire(fichier)
citation_formatee = formater_citation(citation)

# Affichage du label (par exemple, dans une interface Tkinter)
import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text=citation_formatee)
label.pack()
root.mainloop()
