from gagnant import GAGNANT

class CompareCombinaisons():
    def __init__(self, combinaison_par_joueur):
        self.combinaison_par_joueur = combinaison_par_joueur

    def trouver_meilleurs_joueurs_avec_meilleure_combinaison(self):
        meilleure_combinaison = self.__trouver_meilleure_combinaison_parmi_celles_joueurs()
        meilleurs_joueurs = self.__trouver_joueurs_avec_meilleure_combinaison(meilleure_combinaison)
        return meilleurs_joueurs


    def __trouver_meilleure_combinaison_parmi_celles_joueurs(self):
        meilleure_combinaison = None
        for nom_joueur in self.combinaison_par_joueur : 
            combinaison = self.combinaison_par_joueur[nom_joueur]
            if meilleure_combinaison == None : 
                meilleure_combinaison = combinaison
                continue
            combinaisons_a_comparer = [combinaison, meilleure_combinaison]
            winner = self.__determiner_gagnant(combinaisons_a_comparer)
            if winner == GAGNANT.PREMIERE_COMBINAISON :
                meilleure_combinaison = combinaison
        return meilleure_combinaison

    def __determiner_gagnant(self, combinaisons): 
            PREMIERE_COMBINAISON = combinaisons[0]
            SECONDE_COMBINAISON = combinaisons[1]
            if PREMIERE_COMBINAISON.points < SECONDE_COMBINAISON.points : 
                return GAGNANT.SECONDE_COMBINAISON
            elif SECONDE_COMBINAISON.points < PREMIERE_COMBINAISON.points : 
                return GAGNANT.PREMIERE_COMBINAISON
            else : 
                return GAGNANT.EGALITE

    def __trouver_joueurs_avec_meilleure_combinaison(self, meilleure_combinaison):
        meilleurs_joueurs = []
        for nom_joueur in self.combinaison_par_joueur : 
            combinaison = self.combinaison_par_joueur[nom_joueur] 
            if meilleure_combinaison == combinaison : 
                meilleurs_joueurs.append(nom_joueur)
        return meilleurs_joueurs