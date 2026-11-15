from carte import Carte, ValeurCarte
from combinaison.full import Full

from typing import Iterator

class DetecteurFull : 
    def __init__(self, manipuler_les_cartes):
        self.manipuler_les_cartes = manipuler_les_cartes

    def detecte_full(self, combinaison : Iterator[Carte]):
        cartes_triees =  self.manipuler_les_cartes.compter_cartes(combinaison)
        valeur_cartes_presente_deux_fois = ValeurCarte.INDEFINI
        valeur_cartes_presente_trois_fois = ValeurCarte.INDEFINI
        for valeur_carte in cartes_triees : 
            occurence = cartes_triees[valeur_carte]
            if occurence == 2 : 
                valeur_cartes_presente_deux_fois = valeur_carte
            elif occurence == 3 :
                valeur_cartes_presente_trois_fois = valeur_carte
        return Full(valeur_cartes_presente_deux_fois, valeur_cartes_presente_trois_fois)