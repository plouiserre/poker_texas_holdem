from carte  import Carte
from combinaison.brelan import Brelan
from detecteur.brelan_detecteur import BrelanDetecteur
from manipuler_cartes import ManipulerCartes

def test_detecte_brelan_reine():
     (DetecteurBrelanTest()
            .ajouter_carte("2♣")
            .ajouter_carte("Q♦")
            .ajouter_carte("9♦")
            .ajouter_carte("Q♥")
            .ajouter_carte("Q♠")
            .ajouter_carte("3♣")
            .ajouter_carte("A♠")
            .detecte_brelan()
            .valide_brelan("Q", "A"))


class DetecteurBrelanTest : 
    def __init__(self):
        manipuler_cartes = ManipulerCartes()
        self.brelan_detecteur = BrelanDetecteur(manipuler_cartes)
        self.toutes_les_cartes = []
        self.brelan_detecte = None

    def ajouter_carte(self, carte_chiffre):
        carte = Carte.parse(carte_chiffre)
        self.toutes_les_cartes.append(carte)
        return self

    def detecte_brelan(self):
        self.brelan_detecte = self.brelan_detecteur.detecte_brelan(self.toutes_les_cartes)
        return self

    def valide_brelan(self, valeur_brelan, valeur_carte_haute):
        brelan_attendue = Brelan(Carte.parse_valeur(valeur_brelan), Carte.parse_valeur(valeur_carte_haute))
        egal = self.brelan_detecte.valeur == brelan_attendue.valeur and self.brelan_detecte.carte_haute_hors_brelan == brelan_attendue.carte_haute_hors_brelan
        assert(egal == True)