from carte import Carte, ValeurCarte
from combinaison.carte_haute import CarteHaute

from typing import Iterator

class CarteHauteDetecteur : 
    def __init__(self):
        pass

    def detecte_carte_haute(self, combinaison : Iterator[Carte]):
        carte_haute_valeur = ValeurCarte.DEUX
        for carte in combinaison : 
            if carte_haute_valeur < carte.valeur : 
                carte_haute_valeur = carte.valeur
        return CarteHaute(carte_haute_valeur)