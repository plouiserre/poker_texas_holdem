from carte import Carte, CouleurCarte, ValeurCarte
from combinaison.couleur import Couleur

from typing import Iterator

class CouleurDetecteur : 
    def __init__(self):
        pass

    def trouve_couleur(self, combinaison : Iterator[Carte]):
        couleur_carte_avant = CouleurCarte.INDEFINI
        couleur_occurence = 0
        couleur_presente = False
        for carte in combinaison :
            if couleur_occurence == 5 :
                couleur_presente = True
                break
            if couleur_carte_avant == carte.couleur :
                couleur_occurence += 1
                continue
            else : 
                couleur_carte_avant = carte.couleur
                couleur_occurence = 1
                continue

        haute_carte = ValeurCarte.INDEFINI
        for carte in combinaison :
            if couleur_carte_avant == carte.couleur :
               if haute_carte == ValeurCarte.INDEFINI or haute_carte < carte.valeur :
                   haute_carte = carte.valeur

        if couleur_presente :
            return Couleur(couleur_carte_avant, haute_carte)
        else : 
            return None