from carte import Carte
from typing import Iterator


class MeilleureCombinaisonDetecteur():
    def __init__(self, carte_haute_detecteur, paire_detecteur, double_paires_detecteur, brelan_detecteur, suite_detecteur, couleur_detecteur, full_detecteur, carre_detecteur, quinte_flush_detecteur):
        self.carte_haute_detecteur = carte_haute_detecteur
        self.paire_detecteur = paire_detecteur
        self.double_paires_detecteur = double_paires_detecteur
        self.brelan_detecteur = brelan_detecteur
        self.suite_detecteur = suite_detecteur
        self.couleur_detecteur = couleur_detecteur
        self.full_detecteur = full_detecteur
        self.carre_detecteur = carre_detecteur
        self.quinte_flush_detecteur = quinte_flush_detecteur

    def detecte_meilleure_combinaison(self, combinaison):
        quinte_flush = self.__detecte_quinte_flush(combinaison)
        carre = self.__detecte_carre(combinaison)
        full = self.__detecte_full(combinaison)
        couleur = self.__detecte_couleur(combinaison)
        suite = self.__detecte_suite(combinaison)
        brelan = self.__detecte_brelan(combinaison)
        double_paire = self.__detecte_double_paires(combinaison)
        paire= self.__detecte_paire(combinaison)
        carte_haute = self.__detecte_carte_haute(combinaison)
        if quinte_flush != None : 
            return quinte_flush
        elif carre != None : 
            return carre
        elif full != None : 
            return full
        elif couleur != None : 
            return couleur
        elif suite != None : 
            return suite
        elif brelan != None : 
            return brelan
        elif double_paire != None : 
            return double_paire
        elif paire!= None : 
            return paire
        else : 
            return carte_haute 

    def __detecte_quinte_flush(self, combinaison: Iterator[Carte]) :
        return self.quinte_flush_detecteur.detecte_quinte_flush(combinaison)
    
    def __detecte_carre(self, combinaison: Iterator[Carte]) :
        return self.carre_detecteur.detecte_carre(combinaison)
    
    def __detecte_full(self, combinaison: Iterator[Carte]) :
        return self.full_detecteur.detecte_full(combinaison)
    
    def __detecte_couleur(self, combinaison: Iterator[Carte]) : 
        return self.couleur_detecteur.trouve_couleur(combinaison)
    
    def __detecte_suite(self, combinaison: Iterator[Carte]) : 
        return self.suite_detecteur.detecte_suite(combinaison)
        
    def __detecte_brelan(self, combinaison: Iterator[Carte]) : 
        return self.brelan_detecteur.detecte_brelan(combinaison)
        
    def __detecte_double_paires(self, combinaison: Iterator[Carte]) : 
        return self.double_paires_detecteur.trouve_double_paire(combinaison)
        
    def __detecte_paire(self, combinaison: Iterator[Carte]) :
        return self.paire_detecteur.detecte_paire(combinaison)
        
    def __detecte_carte_haute(self, combinaison: Iterator[Carte]) : 
        return self.carte_haute_detecteur.detecte_carte_haute(combinaison)