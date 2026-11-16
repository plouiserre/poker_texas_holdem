from carte import Carte, CouleurCarte, ValeurCarte
from combinaison.full import Full
from combinaison.quinte_flush import QuinteFlush
from detecteur.carre_detecteur import CarreDetecteur
from detecteur.brelan_detecteur import BrelanDetecteur
from detecteur.carte_haute_detecteur import CarteHauteDetecteur
from detecteur.couleur_detecteur import CouleurDetecteur
from detecteur.double_paire_detecteur import DoublePairDetecteur
from detecteur.full_detecteur import DetecteurFull
from detecteur.paire_detecteur import PaireDetecteur
from detecteur.quinte_flush_detecteur import QuinteFlushDetecteur
from detecteur.suite_detecteur import SuiteDetecteur
from detecteur.meilleure_combinaison_detecteur import MeilleureCombinaisonDetecteur
from manipuler_cartes import ManipulerCartes

#♣♥♦♠    
def test_trouve_full_dame_par_six_meilleure_combinaison():
    (CombinaisonTest()
        .ajouter_carte("6♦")
        .ajouter_carte("6♥")
        .ajouter_carte("Q♠")
        .ajouter_carte("Q♦")
        .ajouter_carte("Q♥")
        .ajouter_carte("8♠")
        .ajouter_carte("2♥")
        .identifier_meilleure_combinaison()
        .confirmer_full(Full(ValeurCarte.SIX, ValeurCarte.DAME)))
    
def test_trouve_quinte_flush_roi_coeur():
    (CombinaisonTest()
        .ajouter_carte("J♥")
        .ajouter_carte("9♥")
        .ajouter_carte("10♥")
        .ajouter_carte("6♦")
        .ajouter_carte("3♠")
        .ajouter_carte("K♥")
        .ajouter_carte("Q♥")
        .identifier_meilleure_combinaison()
        .confirmer_quinte_flush(QuinteFlush(ValeurCarte.ROI, CouleurCarte.COEURS)))

class CombinaisonTest():
    def __init__(self):
        self.toutes_les_cartes = []
        manipuler_carte = ManipulerCartes()
        carte_haute_detecteur = CarteHauteDetecteur()
        paire_detecteur = PaireDetecteur(manipuler_carte)
        double_paire_detecteur = DoublePairDetecteur(manipuler_carte)
        brelan_detecteur = BrelanDetecteur(manipuler_carte)
        suite_detecteur = SuiteDetecteur(manipuler_carte)
        couleur_detecteur = CouleurDetecteur(manipuler_carte)
        full_detecteur = DetecteurFull(manipuler_carte)
        carre_detecteur =  CarreDetecteur(manipuler_carte)
        quinte_flush_detecteur = QuinteFlushDetecteur(manipuler_carte, suite_detecteur)
        self.meilleure_combinaison_detecteur = MeilleureCombinaisonDetecteur(carte_haute_detecteur, paire_detecteur, double_paire_detecteur, brelan_detecteur, suite_detecteur, couleur_detecteur, full_detecteur, carre_detecteur, quinte_flush_detecteur)
        self.meilleure_combinaison = None

    def ajouter_carte(self, carte_chiffre):
        carte = Carte.parse(carte_chiffre)
        self.toutes_les_cartes.append(carte)
        return self

    def identifier_meilleure_combinaison(self):
        self.meilleure_combinaison = self.meilleure_combinaison_detecteur.detecte_meilleure_combinaison(self.toutes_les_cartes)
        return self

    def confirmer_full(self, meilleure_combinaison_attendue):
        is_equal = meilleure_combinaison_attendue.deux_fois == self.meilleure_combinaison.deux_fois and meilleure_combinaison_attendue.trois_fois == self.meilleure_combinaison.trois_fois
        assert(is_equal == True)

    def confirmer_quinte_flush(self, meilleure_combinaison_attendue):
        is_equal = meilleure_combinaison_attendue.valeur == self.meilleure_combinaison.valeur and meilleure_combinaison_attendue.couleur == self.meilleure_combinaison.couleur
        assert(is_equal == True)