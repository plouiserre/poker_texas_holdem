from carte import Carte, ValeurCarte
from combinaison.double_paire import DoublePaire

from typing import Iterator


class DoublePairDetecteur : 
    def __init__(self, manipulation_cartes):
        self.manipulation_cartes = manipulation_cartes 

    def trouve_double_paire(self, combinaison: Iterator[Carte]):
        cartes_regroupees_par_valeur = self.manipulation_cartes.compter_cartes(combinaison)
        double_paires = False
        valeur_premiere_pair = ValeurCarte.DEUX
        valeur_seconde_pair = ValeurCarte.DEUX
        haute_carte_hors_pair = ValeurCarte.DEUX
        nombre_de_pairs = 0
        for carte in cartes_regroupees_par_valeur : 
            nombre_cartes = cartes_regroupees_par_valeur[carte]
            if nombre_cartes >= 2 : 
                nombre_de_pairs = nombre_de_pairs + 1 
                if nombre_de_pairs == 1 :
                    valeur_premiere_pair = carte
                else : 
                    double_paires = True
                    if carte > valeur_premiere_pair : 
                        valeur_seconde_pair = valeur_premiere_pair
                        valeur_premiere_pair = carte
                    else : 
                        valeur_seconde_pair = carte
            else : 
                if carte > haute_carte_hors_pair : 
                    haute_carte_hors_pair = carte
        if double_paires : 
            return DoublePaire(valeur_premiere_pair, valeur_seconde_pair, haute_carte_hors_pair)
        else : 
            return None