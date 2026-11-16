from carte import Carte, ValeurCarte
from combinaison.paire import Paire 

from typing import Iterator


class PaireDetecteur: 
    def __init__(self, manipuler_cartes):
        self.manipuler_cartes = manipuler_cartes

    def detecte_paire(self, combinaison : Iterator[Carte]):
        cartes_regroupees_par_valeur = self.manipuler_cartes.compter_cartes(combinaison)
        une_paire_presente = False
        paire_valeur = ValeurCarte.INDEFINI
        carte_haute_valeur_hors_paire = ValeurCarte.INDEFINI
        for carte in cartes_regroupees_par_valeur : 
            number_cards = cartes_regroupees_par_valeur[carte]
            if number_cards == 2 : 
                une_paire_presente = True
                paire_valeur = carte                
            else : 
                if carte > carte_haute_valeur_hors_paire : 
                    carte_haute_valeur_hors_paire = carte
        if une_paire_presente : 
            return Paire(paire_valeur, carte_haute_valeur_hors_paire)