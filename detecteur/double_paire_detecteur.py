from carte import Carte, CouleurCarte, ValeurCarte
from combinaison.double_paire import DoublePaire

from typing import Iterator


class DoublePairDetecteur : 
    def __init__(self):
        pass

    def trouve_double_paire(self, combination: Iterator[Carte]):
        premiere_paire_detecte = False
        premiere_paire_valeur = ValeurCarte.INDEFINI
        deuxieme_paire_detecte = False
        deuxieme_paire_valeur = ValeurCarte.INDEFINI
        haute_carte = ValeurCarte.INDEFINI
        carte_precedente = Carte(ValeurCarte.INDEFINI, CouleurCarte.INDEFINI)
        for carte in combination : 
            if carte_precedente == Carte(ValeurCarte.INDEFINI, CouleurCarte.INDEFINI) :
                carte_precedente = carte
                continue
            else : 
                if carte.valeur == carte_precedente.valeur :
                    if premiere_paire_detecte == False :
                        premiere_paire_detecte = True
                        premiere_paire_valeur = carte.valeur
                    else :
                        deuxieme_paire_detecte = True
                        deuxieme_paire_valeur = carte.valeur
            carte_precedente = carte
        if premiere_paire_detecte and deuxieme_paire_detecte : 
            for carte in combination :
                if carte.valeur != premiere_paire_valeur and carte.valeur != deuxieme_paire_valeur : 
                    if haute_carte == ValeurCarte.INDEFINI : 
                        haute_carte = carte.valeur
                    elif haute_carte < carte.valeur : 
                        haute_carte = carte.valeur
            return DoublePaire(premiere_paire_valeur, deuxieme_paire_valeur, haute_carte) 
        else : 
            return None