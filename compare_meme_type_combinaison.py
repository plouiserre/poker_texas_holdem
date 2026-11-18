from combinaison.brelan import Brelan
from combinaison.carre import Carre
from combinaison.carte_haute import CarteHaute
from combinaison.couleur import Couleur
from combinaison.double_paire import DoublePaire
from combinaison.full import Full
from combinaison.paire import Paire
from combinaison.quinte_flush import QuinteFlush
from combinaison.suite import Suite
from gagnant import GAGNANT

class CompareMemeTypeCombinaison : 
    def __init__(self):
        pass

    def compare_combinaisons(self, PREMIERE_COMBINAISON, DEUXIEME_COMBINAISON) : 
        if type(PREMIERE_COMBINAISON) is CarteHaute and type(DEUXIEME_COMBINAISON) is CarteHaute:
            return self.__compare_deux_combinaisons_carte_haute(PREMIERE_COMBINAISON, DEUXIEME_COMBINAISON)
        elif type(PREMIERE_COMBINAISON) is Paire and type(DEUXIEME_COMBINAISON) is Paire: 
            return self.__compare_deux_combinaisons_avec_paire(PREMIERE_COMBINAISON, DEUXIEME_COMBINAISON)
        elif type(PREMIERE_COMBINAISON) is DoublePaire and type(DEUXIEME_COMBINAISON) is DoublePaire : 
            return self.__compare_combinaisons_avec_double_paires(PREMIERE_COMBINAISON, DEUXIEME_COMBINAISON)
        elif type(PREMIERE_COMBINAISON) is Brelan and type(DEUXIEME_COMBINAISON) is Brelan : 
            return self.__compare_deux_combinaisons_avec_brelans(PREMIERE_COMBINAISON, DEUXIEME_COMBINAISON)
        elif type(PREMIERE_COMBINAISON) is Suite and type(DEUXIEME_COMBINAISON) is Suite : 
            return self.__compare_deux_combinaisons_avec_suite(PREMIERE_COMBINAISON, DEUXIEME_COMBINAISON)        
        elif type(PREMIERE_COMBINAISON) is Full and type(DEUXIEME_COMBINAISON) is Full : 
                    return self.__compare_deux_combinaisons_avec_full(PREMIERE_COMBINAISON, DEUXIEME_COMBINAISON)
        elif type(PREMIERE_COMBINAISON) is Couleur and type(DEUXIEME_COMBINAISON) is Couleur : 
            return self.__compare_deux_combinaisons_avec_couleur(PREMIERE_COMBINAISON, DEUXIEME_COMBINAISON)
        elif type(PREMIERE_COMBINAISON) is Carre and type(DEUXIEME_COMBINAISON) is Carre:
            return self.__compare_deux_combinaisons_avec_carre(PREMIERE_COMBINAISON, DEUXIEME_COMBINAISON)
        elif type(PREMIERE_COMBINAISON) is QuinteFlush and type(DEUXIEME_COMBINAISON) is QuinteFlush:
            return self.__compare_deux_combinaisons_avec_quinte_flush(PREMIERE_COMBINAISON, DEUXIEME_COMBINAISON)

    def __compare_deux_combinaisons_carte_haute(self, PREMIERE_COMBINAISON : CarteHaute, DEUXIEME_COMBINAISON : CarteHaute) -> GAGNANT: 
                if PREMIERE_COMBINAISON.value < DEUXIEME_COMBINAISON.value : 
                    return GAGNANT.DEUXIEME_COMBINAISON
                elif DEUXIEME_COMBINAISON.value < PREMIERE_COMBINAISON.value : 
                    return GAGNANT.PREMIERE_COMBINAISON 
                else :
                    return GAGNANT.EGALITE
                    
    def __compare_deux_combinaisons_avec_paire(self, PREMIERE_COMBINAISON : Paire, DEUXIEME_COMBINAISON : Paire) -> GAGNANT:
        if PREMIERE_COMBINAISON.value < DEUXIEME_COMBINAISON.value : 
            return GAGNANT.DEUXIEME_COMBINAISON
        elif DEUXIEME_COMBINAISON.value < PREMIERE_COMBINAISON.value : 
            return GAGNANT.PREMIERE_COMBINAISON
        else : 
            if PREMIERE_COMBINAISON.high_value_rest_of_cards < DEUXIEME_COMBINAISON.high_value_rest_of_cards : 
                return GAGNANT.DEUXIEME_COMBINAISON
            elif DEUXIEME_COMBINAISON.high_value_rest_of_cards < PREMIERE_COMBINAISON.high_value_rest_of_cards :
                return GAGNANT.PREMIERE_COMBINAISON
            else : 
                return GAGNANT.EGALITE

    def __compare_combinaisons_avec_double_paires(self, PREMIERE_COMBINAISON : DoublePaire, DEUXIEME_COMBINAISON : DoublePaire) -> GAGNANT : 
        if PREMIERE_COMBINAISON.first_pair_value < DEUXIEME_COMBINAISON.first_pair_value : 
            return GAGNANT.DEUXIEME_COMBINAISON
        elif DEUXIEME_COMBINAISON.first_pair_value < PREMIERE_COMBINAISON.first_pair_value : 
            return GAGNANT.PREMIERE_COMBINAISON
        elif PREMIERE_COMBINAISON.first_pair_value == DEUXIEME_COMBINAISON.first_pair_value : 
            if PREMIERE_COMBINAISON.second_pair_value < DEUXIEME_COMBINAISON.second_pair_value : 
                return GAGNANT.DEUXIEME_COMBINAISON
            elif DEUXIEME_COMBINAISON.second_pair_value < PREMIERE_COMBINAISON.second_pair_value : 
                return GAGNANT.PREMIERE_COMBINAISON
            elif PREMIERE_COMBINAISON.second_pair_value == DEUXIEME_COMBINAISON.second_pair_value : 
                if PREMIERE_COMBINAISON.high_value_rest_of_cards < DEUXIEME_COMBINAISON.high_value_rest_of_cards :
                    return GAGNANT.DEUXIEME_COMBINAISON
                else :
                    return GAGNANT.PREMIERE_COMBINAISON

    def __compare_deux_combinaisons_avec_brelans(self, PREMIERE_COMBINAISON : Brelan, DEUXIEME_COMBINAISON : Brelan): 
        if PREMIERE_COMBINAISON.value < DEUXIEME_COMBINAISON.value :
            return GAGNANT.DEUXIEME_COMBINAISON
        elif DEUXIEME_COMBINAISON.value < PREMIERE_COMBINAISON.value : 
            return GAGNANT.PREMIERE_COMBINAISON
        elif PREMIERE_COMBINAISON.value == DEUXIEME_COMBINAISON.value : 
            if PREMIERE_COMBINAISON.high_value_rest_of_cards < DEUXIEME_COMBINAISON.high_value_rest_of_cards :
                return GAGNANT.DEUXIEME_COMBINAISON
            elif DEUXIEME_COMBINAISON.high_value_rest_of_cards < PREMIERE_COMBINAISON.high_value_rest_of_cards : 
                return GAGNANT.PREMIERE_COMBINAISON

    def __compare_deux_combinaisons_avec_suite(self, PREMIERE_COMBINAISON : Suite, DEUXIEME_COMBINAISON : Suite):
        if PREMIERE_COMBINAISON.value < DEUXIEME_COMBINAISON.value : 
            return GAGNANT.DEUXIEME_COMBINAISON 
        elif DEUXIEME_COMBINAISON.value < PREMIERE_COMBINAISON.value : 
            return GAGNANT.PREMIERE_COMBINAISON

    def __compare_deux_combinaisons_avec_couleur(self, PREMIERE_COMBINAISON : Couleur, DEUXIEME_COMBINAISON : Couleur):
        if PREMIERE_COMBINAISON.high_value < DEUXIEME_COMBINAISON.high_value : 
            return GAGNANT.DEUXIEME_COMBINAISON 
        elif DEUXIEME_COMBINAISON.high_value < PREMIERE_COMBINAISON.high_value : 
            return GAGNANT.PREMIERE_COMBINAISON

    def __compare_deux_combinaisons_avec_full(self, PREMIERE_COMBINAISON : Full, DEUXIEME_COMBINAISON : Full):
        if PREMIERE_COMBINAISON.trois_fois != DEUXIEME_COMBINAISON.trois_fois : 
            if PREMIERE_COMBINAISON.trois_fois < DEUXIEME_COMBINAISON.trois_fois : 
                return GAGNANT.DEUXIEME_COMBINAISON
            else : 
                return GAGNANT.PREMIERE_COMBINAISON
        else :
            if PREMIERE_COMBINAISON.deux_fois < DEUXIEME_COMBINAISON.deux_fois : 
                return GAGNANT.DEUXIEME_COMBINAISON
            elif DEUXIEME_COMBINAISON.deux_fois < PREMIERE_COMBINAISON.deux_fois : 
                return GAGNANT.PREMIERE_COMBINAISON
            else : 
                return GAGNANT.EGALITE


    def __compare_deux_combinaisons_avec_carre(self, PREMIERE_COMBINAISON : Carre, DEUXIEME_COMBINAISON : Carre):
        if PREMIERE_COMBINAISON.value < DEUXIEME_COMBINAISON.value : 
            return GAGNANT.DEUXIEME_COMBINAISON 
        elif DEUXIEME_COMBINAISON.value < PREMIERE_COMBINAISON.value : 
            return GAGNANT.PREMIERE_COMBINAISON
        elif PREMIERE_COMBINAISON.value == DEUXIEME_COMBINAISON.value : 
            if PREMIERE_COMBINAISON.high_value_rest_of_cards < DEUXIEME_COMBINAISON.high_value_rest_of_cards : 
                return GAGNANT.DEUXIEME_COMBINAISON 
            elif DEUXIEME_COMBINAISON.high_value_rest_of_cards < PREMIERE_COMBINAISON.high_value_rest_of_cards :
                return GAGNANT.PREMIERE_COMBINAISON

    def __compare_deux_combinaisons_avec_quinte_flush(self, PREMIERE_COMBINAISON : QuinteFlush, DEUXIEME_COMBINAISON : QuinteFlush):
        if PREMIERE_COMBINAISON.value < DEUXIEME_COMBINAISON.value : 
            return GAGNANT.DEUXIEME_COMBINAISON 
        elif DEUXIEME_COMBINAISON.value < PREMIERE_COMBINAISON.value : 
            return GAGNANT.PREMIERE_COMBINAISON