from carte import Carte, ValeurCarte
from combinaison.full import Full

from typing import Iterator

class DetecteurFull : 
    def __init__(self, manipuler_les_cartes):
        self.manipuler_les_cartes = manipuler_les_cartes
        self.carte_presentes_deux_fois = ValeurCarte.INDEFINI
        self.carte_presentes_trois_fois = ValeurCarte.INDEFINI
        self.toutes_les_cartes_presentes_trois_fois = []
        self.toutes_les_cartes_presentes_deux_fois = []

    def detecte_full(self, combinaison : Iterator[Carte]):
        cartes_classes_par_valeur = self.manipuler_les_cartes.compter_cartes(combinaison)
        for carte in cartes_classes_par_valeur :
            nombre_cartes = cartes_classes_par_valeur[carte]
            if nombre_cartes == 3 : 
                self.toutes_les_cartes_presentes_trois_fois.append(carte)
            elif nombre_cartes == 2 : 
                self.toutes_les_cartes_presentes_deux_fois.append(carte)
        if len(self.toutes_les_cartes_presentes_trois_fois) == 1 and len(self.toutes_les_cartes_presentes_deux_fois) == 1 : 
            return Full(self.toutes_les_cartes_presentes_deux_fois[0], self.toutes_les_cartes_presentes_trois_fois[0])
        elif len(self.toutes_les_cartes_presentes_trois_fois ) == 2 : 
            first_choice = self.toutes_les_cartes_presentes_trois_fois[0]
            second_choice = self.toutes_les_cartes_presentes_trois_fois[1]
            if first_choice < second_choice : 
                return Full(first_choice, second_choice)
            else : 
                return Full(second_choice, first_choice)
        else : 
            return None