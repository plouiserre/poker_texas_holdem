from carte import Carte, ValeurCarte
from combinaison.carre import Carre
from typing import Iterator

class CarreDetecteur : 
    def __init__(self, manipuler_cartes):
        self.manipuler_cartes = manipuler_cartes

    def detecte_carre(self, combinaison : Iterator[Carte]):
        carte_presente_quatre_fois = ValeurCarte.INDEFINI
        valeur_carte_hors_carre = ValeurCarte.INDEFINI   
        cartes_regroupes_par_valeur = self.manipuler_cartes.compter_cartes(combinaison)
        for carte in cartes_regroupes_par_valeur : 
            nombre_cartes = cartes_regroupes_par_valeur[carte]
            if nombre_cartes == 4 :
                carte_presente_quatre_fois = carte
            else :
                if valeur_carte_hors_carre == ValeurCarte.INDEFINI or valeur_carte_hors_carre < carte :
                    valeur_carte_hors_carre = carte
        if carte_presente_quatre_fois != ValeurCarte.INDEFINI :
            return Carre(carte_presente_quatre_fois, valeur_carte_hors_carre)
        else : 
            return None