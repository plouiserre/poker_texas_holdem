from carte import Carte
from combinaison.paire import Paire
from detecteur.paire_detecteur import PaireDetecteur
from manipuler_cartes import ManipulerCartes

def test_detecte_pair_reine():
    (DetecteurPaireTest()
        .ajouter_carte("2♣")
        .ajouter_carte("Q♦")
        .ajouter_carte("9♦")
        .ajouter_carte("10♥")
        .ajouter_carte("Q♠")
        .ajouter_carte("3♣")
        .ajouter_carte("A♠")
        .detecte_paire()
        .valide_paire("Q", "A"))

class DetecteurPaireTest : 
    def __init__(self):
        manipuler_cartes = ManipulerCartes()
        self.paire_detecteur = PaireDetecteur(manipuler_cartes)
        self.toutes_les_cartes = []
        self.paire_detecte = None

    def ajouter_carte(self, carte_chiffre):
        carte = Carte.parse(carte_chiffre)
        self.toutes_les_cartes.append(carte)
        return self

    def detecte_paire(self):
        self.paire_detecte = self.paire_detecteur.detecte_paire(self.toutes_les_cartes)
        return self

    def valide_paire(self, valeur_paire, valeur_carte_haute):
        paire_attendue = Paire(Carte.parse_valeur(valeur_paire), Carte.parse_valeur(valeur_carte_haute))
        egal = self.paire_detecte.valeur == paire_attendue.valeur and self.paire_detecte.carte_haute_valeur_hors_paire == paire_attendue.carte_haute_valeur_hors_paire
        assert(egal == True)