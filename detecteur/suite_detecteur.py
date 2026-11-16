from carte import Carte, ValeurCarte
from combinaison.suite import Suite
from manipuler_cartes import TypesClassement
from typing import Iterator

class SuiteDetecteur : 
    def __init__(self, manipuler_cartes):
        self.manipuler_cartes = manipuler_cartes
        self.carte_haute_valeur = ValeurCarte.DEUX
        self.as_present = False
        self.carte_deux_present = False
        self.carte_roi_present = False


    def detecte_suite(self, combinaison : Iterator[Carte]) : 
        toutes_suites = []
        if len(combinaison) >= 5 :
            toutes_cartes_triees = self.manipuler_cartes.trier_cartes(combinaison, 5, TypesClassement.GARDER_UN_DOUBLON)            
            toutes_suites = self.__trouver_suite_a_partir_toutes_cartes_triees(toutes_cartes_triees)
            return self.__trouver_meilleure_suite(toutes_suites)            
        else : 
            return None         

    def __trouver_suite_a_partir_toutes_cartes_triees (self, toutes_cartes_triees):
        toutes_suites = []
        for cartes_triees in toutes_cartes_triees:
            toutes_les_suites_possibles = self.__determiner_toutes_les_suites_possibles(cartes_triees)
            if toutes_les_suites_possibles == None : 
                continue
            for suite_possible in toutes_les_suites_possibles : 
                suite = self.__determiner_suite(suite_possible)
                if suite != None : 
                    toutes_suites.append(suite)
                else : 
                    continue
        return toutes_suites
        
    def __determiner_toutes_les_suites_possibles(self, cartes_triees):
        if len(cartes_triees) == 5 :
            return [cartes_triees]
        elif len(cartes_triees) == 6 : 
            return [cartes_triees[1 :6], cartes_triees]
        elif len(cartes_triees) == 7 : 
            return [cartes_triees[2 :], cartes_triees[1 :6], cartes_triees[0 :5]]            

    def __determiner_suite(self, cartes_triees):        
        if len(cartes_triees) >= 5 :
            cartes_triees_sont_valides = self.__analyser_cartes_triees(cartes_triees)
            if cartes_triees_sont_valides == False : 
                return None
            elif self.as_present == False or (self.as_present and self.carte_deux_present): 
                return Suite(self.carte_haute_valeur)
            elif self.as_present and self.carte_roi_present : 
                return Suite(ValeurCarte.AS)
            else :
                return None
        else : 
            return None

    def __analyser_cartes_triees(self, cartes_triees):
        cartes_triees_sont_valides = True
        derniere_valeur = ValeurCarte.INDEFINI
        self.__initialiser_tous_les_verifs_cartes_importantes()
        for carte in cartes_triees :
            if carte.valeur == ValeurCarte.AS :
                self.as_present = True
                continue 
            elif carte.valeur == ValeurCarte.ROI : 
                self.carte_roi_present = True
            elif carte.valeur == ValeurCarte.DEUX : 
                self.carte_deux_present = True
            self.carte_haute_valeur = carte.valeur
            if derniere_valeur != ValeurCarte.INDEFINI : 
                if carte.valeur - derniere_valeur > 1 : 
                    cartes_triees_sont_valides = False
            derniere_valeur = carte.valeur
        return cartes_triees_sont_valides

    def __initialiser_tous_les_verifs_cartes_importantes(self):
        self.as_present = False
        self.carte_deux_present = False
        self.carte_roi_present = False

    def __trouver_meilleure_suite(self, toutes_suites):
        if len(toutes_suites) == 1 :
            return toutes_suites[0]
        else : 
            best_quinte = None 
            high_carte = None 
            for suite in toutes_suites:
                if high_carte == None or high_carte < suite.high_carte : 
                    best_quinte = suite
            return best_quinte