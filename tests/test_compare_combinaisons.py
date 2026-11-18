from carte import ValeurCarte
from combinaison.brelan import Brelan
from combinaison.carte_haute import CarteHaute
from combinaison.full import Full
from compare_combinaisons import CompareCombinaisons

def test_compare_albert_einstein_brelan_avec_marie_curie_full():
    (CompareDeuxJoueursCombinaisonsCartes()
        .ajouter_joueurs("Albert Einstein")
        .ajouter_joueurs("Marie Curie")
        .ajouter_combinaison("Albert Einstein", Brelan(ValeurCarte.DAME, ValeurCarte.HUIT))
        .ajouter_combinaison("Marie Curie", Full(ValeurCarte.SIX, ValeurCarte.DAME))
        .comparer_combinaisons()
        .confirme_joueur_gagnant(["Marie Curie"]))

def test_compare_allan_turing_carte_haute_avec_margaret_hamilton_full():
    (CompareDeuxJoueursCombinaisonsCartes()
        .ajouter_joueurs("Allan Turing")
        .ajouter_joueurs("Margaret Hamilton")
        .ajouter_combinaison("Allan Turing", CarteHaute(ValeurCarte.ROI))
        .ajouter_combinaison("Margaret Hamilton", Full(ValeurCarte.DAME, ValeurCarte.SIX))
        .comparer_combinaisons()
        .confirme_joueur_gagnant(["Margaret Hamilton"]))

def test_compare_marie_curie_full_avec_margaret_hamilton_full():
    (CompareDeuxJoueursCombinaisonsCartes()
        .ajouter_joueurs("Margaret Hamilton")
        .ajouter_joueurs("Marie Curie")
        .ajouter_combinaison("Margaret Hamilton", Full(ValeurCarte.DAME, ValeurCarte.SIX))
        .ajouter_combinaison("Marie Curie", Full(ValeurCarte.SIX, ValeurCarte.DAME))
        .comparer_combinaisons()
        .confirme_joueur_gagnant(["Marie Curie"]))

def test_compare_marie_curie_full_avec_margaret_hamilton_full():
    (CompareDeuxJoueursCombinaisonsCartes()
        .ajouter_joueurs("Margaret Hamilton")
        .ajouter_joueurs("Marie Curie")
        .ajouter_combinaison("Marie Curie", Full(ValeurCarte.SIX, ValeurCarte.DAME))
        .ajouter_combinaison("Margaret Hamilton", Full(ValeurCarte.SIX, ValeurCarte.DAME))
        .comparer_combinaisons()
        .confirme_joueur_gagnant(["Marie Curie", "Margaret Hamilton"]))

class CompareDeuxJoueursCombinaisonsCartes():
    def __init__(self):
        self.joueurs_avec_combinaisons = {}
        self.meilleurs_joueurs = []

    def ajouter_joueurs(self, nom_joueur):
        self.joueurs_avec_combinaisons[nom_joueur] = None
        return self

    def ajouter_combinaison(self, nom_joueur, combinaison):
        self.joueurs_avec_combinaisons[nom_joueur] = combinaison
        return self

    def comparer_combinaisons(self):
        compare_combinaison = CompareCombinaisons(self.joueurs_avec_combinaisons)
        self.meilleurs_joueurs = compare_combinaison.trouver_meilleurs_joueurs_avec_meilleure_combinaison()
        return self

    def confirme_joueur_gagnant(self, noms_joueurs_gagnants):
        if len(noms_joueurs_gagnants) == 1:
            meilleur_joueur_confirme = noms_joueurs_gagnants[0] in self.meilleurs_joueurs
            assert(meilleur_joueur_confirme == True)
        else : 
            is_ok = True 
            for nom in noms_joueurs_gagnants : 
                is_ok = nom in self.meilleurs_joueurs
                if is_ok == False : 
                    break
            assert(is_ok == True)