from carte import Carte, CouleurCarte, ValeurCarte
from combinaison.couleur import Couleur

from typing import Iterator

class CouleurDetecteur : 
    def __init__(self, manipulation_cartes):
        self.manipulation_cartes = manipulation_cartes 

    #TODO améliorer le code
    def trouve_couleur(self, combinaison : Iterator[Carte]):
        cartes_ranges_par_couleur = self.manipulation_cartes.regrouper_par_couleur(combinaison)
        couleur_carte_recherche = CouleurCarte.INDEFINI
        haute_carte = ValeurCarte.INDEFINI
        for couleur_carte in cartes_ranges_par_couleur : 
            nbre_cartes = cartes_ranges_par_couleur[couleur_carte]
            if nbre_cartes >= 5 : 
                couleur_carte_recherche = couleur_carte
                break

        if couleur_carte_recherche != CouleurCarte.INDEFINI:
            for carte in combinaison :
                if couleur_carte_recherche == carte.couleur :
                    if haute_carte == ValeurCarte.INDEFINI or haute_carte < carte.valeur :
                        haute_carte = carte.valeur

        if couleur_carte_recherche != CouleurCarte.INDEFINI :
            return Couleur(couleur_carte_recherche, haute_carte)
        else : 
            return None