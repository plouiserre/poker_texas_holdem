from carte import Carte
from combinaison.quinte_flush import QuinteFlush
from detecteur.quinte_flush_detecteur import QuinteFlushDetecteur
from detecteur.suite_detecteur import SuiteDetecteur
from manipuler_cartes import ManipulerCartes

def test_detecteur_quinte_flush_reine_pique():
    (DetecteurQuinteFlushTest()
            .ajouter_carte("2♣")
            .ajouter_carte("Q♠")
            .ajouter_carte("9♠")
            .ajouter_carte("10♠")
            .ajouter_carte("K♠")
            .ajouter_carte("3♥")
            .ajouter_carte("J♠")
            .detecte_quinte_flush()
            .valide_quinte("K", "♠"))
    
    
class DetecteurQuinteFlushTest(): 
    def __init__(self):
        self.toutes_les_cartes = []
        manipuler_cartes = ManipulerCartes()
        suite_detecteur = SuiteDetecteur(manipuler_cartes)
        self.quinte_flush_detecteur = QuinteFlushDetecteur(manipuler_cartes, suite_detecteur)
        self.quinte_flush_detecte = None

    def ajouter_carte(self, carte_chiffre):
        carte = Carte.parse(carte_chiffre)
        self.toutes_les_cartes.append(carte)
        return self
    
    def detecte_quinte_flush(self):
        self.quinte_flush_detecte = self.quinte_flush_detecteur.detecte_quinte_flush(self.toutes_les_cartes)
        return self

    def valide_quinte(self, valeur_quinte_flush, couleur_quinte_flush):
        quinte_flush_attendu = QuinteFlush(Carte.parse_valeur(valeur_quinte_flush), Carte.parse_couleur(couleur_quinte_flush)) 
        egal = self.quinte_flush_detecte.valeur == quinte_flush_attendu.valeur and self.quinte_flush_detecte.couleur == quinte_flush_attendu.couleur 
        assert(egal == True)