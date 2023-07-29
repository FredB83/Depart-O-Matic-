from tkinter import *
from tkinter import ttk
import tkinter as tk
import technician as tsc

def keltech():
    result= int(entree.get())
    for secteur,zone in tsc.secteurs.items():
        for i in zone :
            if i == result:
                technicians = tsc.tech[secteur]
                label_valeur.config(text=f"C'est le secteur : {secteur} ! ")
                label_valeur2.config(text=f"C'est le secteur de {technicians}")


def afficher_valeur():
    valeur = entree.get()
    label_valeur.config(text=f"La valeur saisie est : {valeur}")

# Créer une instance de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("DEPARTEMENT O MATIC")

f1=Frame(fenetre, width=800, height=800)
title = tk.Label(fenetre, text="Entrez le département : ")
title.pack()

entree = tk.Entry(fenetre)
entree.pack()

b1=Button(fenetre, text="Validez",command=keltech)
b1.pack(fill="both")

label_valeur = tk.Label(fenetre, text="")
label_valeur.pack()

label_valeur2 = tk.Label(fenetre, text="")
label_valeur2.pack()

f1.pack()


# Lancer la boucle principale Tkinter
fenetre.mainloop()
