from carte import Carte
from combinaison.suite import Suite
from detecteur.suite_detecteur import SuiteDetecteur
from manipuler_cartes import ManipulerCartes

def test_detecte_suite_reine():
    (DetecteurSuiteTest()
        .ajouter_carte("2♣")
        .ajouter_carte("Q♦")
        .ajouter_carte("9♦")
        .ajouter_carte("10♥")
        .ajouter_carte("K♠")
        .ajouter_carte("3♣")
        .ajouter_carte("J♠")
        .detecte_suite()
        .valide_suite("K"))


class DetecteurSuiteTest: 
    def __init__(self):
        self.toutes_les_cartes = []
        manipuler_cartes = ManipulerCartes()
        self.suite_detecteur = SuiteDetecteur(manipuler_cartes)

    def ajouter_carte(self, carte_chiffre):
        carte = Carte.parse(carte_chiffre)
        self.toutes_les_cartes.append(carte)
        return self
    
    def detecte_suite(self):
        self.suite_detecte = self.suite_detecteur.detecte_suite(self.toutes_les_cartes)
        return self

    def valide_suite(self, valeur_suite):
        suite_attendu = Suite(Carte.parse_valeur(valeur_suite)) 
        egal = self.suite_detecte.valeur == suite_attendu.valeur 
        assert(egal == True)