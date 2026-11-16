from carte import Carte, CouleurCarte, ValeurCarte
from combinaison.quinte_flush import QuinteFlush
from manipuler_cartes import TypesClassement

from typing import Iterator


class QuinteFlushDetecteur():
    def __init__(self):
        pass

    def __init__(self, manipuler_cartes, quinte_detecteur):
        self.manipuler_cartes = manipuler_cartes 
        self.quinte_detecteur = quinte_detecteur
        self.couleur_carte = CouleurCarte.INDEFINI
        self.suite = None
        self.carte_mini = ValeurCarte.INDEFINI

    def detecte_quinte_flush(self, combinaison: Iterator[Carte]):
        meme_couleur = True
        self.suite = self.quinte_detecteur.detecte_suite(combinaison)
        self.carte_mini = self.suite.valeur - 4
        if self.suite != None : 
            self.couleur_carte = self.__trouve_couleur_majoritaire(combinaison)
            toutes_cartes_dans_suite = self.__trouve_cartes_compatibles_avec_quinte_flush(combinaison)
            if toutes_cartes_dans_suite == None : 
                return None
            toutes_cartes_dans_suite_sans_doublon = self.manipuler_cartes.trier_cartes(toutes_cartes_dans_suite, 5, TypesClassement.AUCUN_DOUBLON)
            meme_couleur = self.voir_si_cartes_meme_couleur(toutes_cartes_dans_suite_sans_doublon)
            if meme_couleur == False : 
                return None
            else : 
                if len(toutes_cartes_dans_suite_sans_doublon[0]) == 5 : 
                    return QuinteFlush(self.suite.valeur, self.couleur_carte)
                else : 
                    return self.__identifier_quinte_flush(toutes_cartes_dans_suite_sans_doublon, toutes_cartes_dans_suite)
        else :
            return None    

    def __trouve_cartes_compatibles_avec_quinte_flush(self, combinaison):
        toutes_cartes_dans_suite = []        
        for carte in combinaison : 
            if carte.valeur >= self.carte_mini and carte.couleur == self.couleur_carte : 
                toutes_cartes_dans_suite.append(carte)
        if len(toutes_cartes_dans_suite) < 5 : 
            return None
        else : 
            return toutes_cartes_dans_suite

    def __trouve_couleur_majoritaire(self, combinaison):
        toutes_cartes_couleurs = {}
        for carte in combinaison : 
            if carte.couleur in toutes_cartes_couleurs : 
                toutes_cartes_couleurs[carte.couleur] += 1
            else : 
                toutes_cartes_couleurs[carte.couleur] = 1
        couleur_carte_max = CouleurCarte.INDEFINI
        comptage_couleur = 0
        for couleur in toutes_cartes_couleurs :
            count_this_couleur = toutes_cartes_couleurs[couleur]            
            if comptage_couleur < count_this_couleur : 
                comptage_couleur = count_this_couleur
                couleur_carte_max = couleur
        return couleur_carte_max

    def voir_si_cartes_meme_couleur(self, toutes_cartes_dans_suite_sans_doublon):
        meme_couleur = True
        for carte in toutes_cartes_dans_suite_sans_doublon[0] : 
            meme_couleur = self.__determine_meme_couleur_is_ok_for_this_carte(self.suite.valeur, carte, self.couleur_carte)
            if meme_couleur == False : 
                break
        return meme_couleur
                        
    def __determine_meme_couleur_is_ok_for_this_carte(self, suite_valeur, carte, couleur_carte):
        meme_couleur = True
        difference_carte_valeur = suite_valeur - carte.valeur
        if difference_carte_valeur < 4 and difference_carte_valeur > 0 and carte.couleur != couleur_carte : 
            meme_couleur = False
        return meme_couleur    

    def __verifie_si_doublon_a_couleur_majoritaire(self, doublon_cartes): 
        meme_couleur = False
        for carte in doublon_cartes : 
            if carte.valeur >= self.carte_mini and carte.couleur == self.couleur_carte : 
                meme_couleur = True 
                if meme_couleur: 
                    break
        return meme_couleur

    def __identifier_quinte_flush(self, toutes_cartes_dans_suite_sans_doublon, toutes_cartes_dans_suite):
        if len(toutes_cartes_dans_suite_sans_doublon[0]) == 5 : 
            return QuinteFlush(self.suite.valeur, self.couleur_carte)
        else : 
            doublon_cartes = self.manipuler_cartes.trier_cartes(toutes_cartes_dans_suite, 5, TypesClassement.UNIQUEMENT_DOUBLONS)
            meme_couleur = self.__verifie_si_doublon_a_couleur_majoritaire(doublon_cartes)
            if meme_couleur : 
                return QuinteFlush(self.suite.valeur, self.couleur_carte)
            else : 
                return None