import copy

from carte import Carte, CouleurCarte, ValeurCarte
from enum import Enum
class ManipulerCartes : 
    def __init__(self):
        pass

    def compter_cartes(self, combinaison):
        comptage_cartes = {}
        for carte in combinaison : 
            if carte.valeur in comptage_cartes : 
                comptage_cartes[carte.valeur] += 1
            else : 
                comptage_cartes[carte.valeur] = 1
        return comptage_cartes

    def regrouper_par_couleur(self, combinaison):
        couleur_cartes = {}
        for carte in combinaison : 
            if carte.couleur in couleur_cartes : 
                couleur_cartes[carte.couleur] += 1
            else : 
                couleur_cartes[carte.couleur] = 1
        return couleur_cartes

    def trier_cartes(self, combinaison, limite, type_classement): 
        combinaisons_complements_triees = self.__trier_toutes_les_cartes(combinaison, type_classement)
        if len(combinaisons_complements_triees) <= limite : 
            return [combinaisons_complements_triees]
        else : 
            return self.__avoir_toutes_combinaisons_cartes_triees(combinaisons_complements_triees, limite)

    def __trier_toutes_les_cartes(self, combinaison, type_classement):
        toutes_les_cartes = copy.deepcopy(combinaison)
        combinaison_triees = []
        derniere_carte = Carte(ValeurCarte.INDEFINI, CouleurCarte.INDEFINI)
        seulement_doublons = []
        while(len(toutes_les_cartes) > 0) :
            min_Carte = self.__retourner_plus_petite_carte(toutes_les_cartes)                            
            if ((type_classement == TypesClassement.UNIQUEMENT_DOUBLONS or type_classement == TypesClassement.AUCUN_DOUBLON) and derniere_carte.valeur == min_Carte.valeur ):
                seulement_doublons.append(derniere_carte)
                seulement_doublons.append(min_Carte)
            elif (type_classement == TypesClassement.GARDER_UN_DOUBLON and derniere_carte.valeur == min_Carte.valeur) == False : 
                combinaison_triees.append(min_Carte)
            derniere_carte = min_Carte
            toutes_les_cartes.remove(min_Carte)
        if type_classement == TypesClassement.UNIQUEMENT_DOUBLONS :
            return seulement_doublons
        elif type_classement == TypesClassement.AUCUN_DOUBLON :
            pas_de_doublon_liste = self.__supprime_tous_doublons(combinaison_triees, seulement_doublons)
            return pas_de_doublon_liste
        else : 
            return combinaison_triees

    def __supprime_tous_doublons(self, sorted_list, seulement_doublons):
        liste_finale = copy.deepcopy(sorted_list)
        for doublon in seulement_doublons : 
            for element in sorted_list : 
                if (doublon.valeur == element.valeur and doublon.couleur == element.couleur ):
                    liste_finale.remove(element)
        return liste_finale

    def __retourner_plus_petite_carte(self, toutes_les_cartes):
        min_Carte = Carte(ValeurCarte.INDEFINI, CouleurCarte.INDEFINI)
        for idx, _ in enumerate(toutes_les_cartes) : 
                carte_analyse = toutes_les_cartes[idx]
                if min_Carte == Carte(ValeurCarte.INDEFINI, CouleurCarte.INDEFINI) :
                    min_Carte = carte_analyse
                    continue
                else : 
                    if min_Carte.valeur > carte_analyse.valeur : 
                        min_Carte = carte_analyse
        return min_Carte
    
    def __avoir_toutes_combinaisons_cartes_triees(self, combinaisons_complements_triees, limite):
        toutes_cartes_triees = []
        is_limite_atteinte = False 
        i = 0
        while is_limite_atteinte == False : 
            nouvelle_limite = i + limite
            parties_cartes_triees = combinaisons_complements_triees[i :nouvelle_limite]
            toutes_cartes_triees.append(parties_cartes_triees)
            i += 1
            if nouvelle_limite == len(combinaisons_complements_triees):
                is_limite_atteinte = True
        return toutes_cartes_triees


class TypesClassement(Enum):
    NORMAL = 0
    AUCUN_DOUBLON = 1
    GARDER_UN_DOUBLON = 2
    UNIQUEMENT_DOUBLONS = 3
