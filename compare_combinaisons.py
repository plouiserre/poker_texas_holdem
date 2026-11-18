from compare_meme_type_combinaison import CompareMemeTypeCombinaison
from gagnant import GAGNANT

class CompareCombinaisons():
    def __init__(self, combinaison_par_joueur):
        self.combinaison_par_joueur = combinaison_par_joueur
        self.compare_meme_type_combinaison = CompareMemeTypeCombinaison()

    def trouver_meilleurs_joueurs_avec_meilleure_combinaison(self):
        meilleure_combinaison = self.__trouver_meilleure_combinaison_parmi_celles_joueurs()
        meilleurs_joueurs = self.__trouver_joueurs_avec_meilleure_combinaison(meilleure_combinaison)
        return meilleurs_joueurs


    def __trouver_meilleure_combinaison_parmi_celles_joueurs(self):
        meilleures_combinaisons = []
        for nom_joueur in self.combinaison_par_joueur : 
            combinaison = self.combinaison_par_joueur[nom_joueur]
            if len(meilleures_combinaisons) == 0 : 
                meilleures_combinaisons.append(combinaison)
                continue
            combinaisons_a_comparer = [combinaison, meilleures_combinaisons[0]]
            winner = self.__determiner_gagnant(combinaisons_a_comparer)
            if winner == GAGNANT.PREMIERE_COMBINAISON :
                meilleures_combinaisons = []
                meilleures_combinaisons.append(combinaison)
            elif winner == GAGNANT.EGALITE : 
                meilleures_combinaisons.append(combinaison)
        return meilleures_combinaisons

    def __determiner_gagnant(self, combinaisons): 
            PREMIERE_COMBINAISON = combinaisons[0]
            SECONDE_COMBINAISON = combinaisons[1]
            if PREMIERE_COMBINAISON.points < SECONDE_COMBINAISON.points : 
                return GAGNANT.SECONDE_COMBINAISON
            elif SECONDE_COMBINAISON.points < PREMIERE_COMBINAISON.points : 
                return GAGNANT.PREMIERE_COMBINAISON
            else : 
                return self.compare_meme_type_combinaison.compare_combinaisons(PREMIERE_COMBINAISON, SECONDE_COMBINAISON)

    def __trouver_joueurs_avec_meilleure_combinaison(self, meilleures_combinaisons):
        meilleurs_joueurs = []
        for nom_joueur in self.combinaison_par_joueur : 
            combinaison = self.combinaison_par_joueur[nom_joueur] 
            for meilleure_combinaison in meilleures_combinaisons : 
                if meilleure_combinaison == combinaison : 
                    meilleurs_joueurs.append(nom_joueur)
        return meilleurs_joueurs