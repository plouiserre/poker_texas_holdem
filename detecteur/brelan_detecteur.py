from carte import Carte, ValeurCarte
from combinaison.brelan import Brelan

from typing import Iterator

class BrelanDetecteur :
    def __init__(self, manipuler_cartes):
        self.manipuler_cartes = manipuler_cartes

    def detecte_brelan(self, combinaison : Iterator[Carte]):
        cartes_regroupes_par_valeur = self.manipuler_cartes.compter_cartes(combinaison)
        brelan_present = False
        valeur_brelan = ValeurCarte.DEUX
        valeur_carte_haute_hors_brelan = ValeurCarte.DEUX
        for carte in cartes_regroupes_par_valeur : 
            nombres_cartes = cartes_regroupes_par_valeur[carte]
            if nombres_cartes == 3 : 
                brelan_present = True
                valeur_brelan = carte
            else : 
                if carte > valeur_carte_haute_hors_brelan : 
                    valeur_carte_haute_hors_brelan = carte
        if brelan_present : 
            return Brelan(valeur_brelan, valeur_carte_haute_hors_brelan)
        else : 
            return None