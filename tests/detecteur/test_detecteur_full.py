from carte import Carte
from combinaison.full import Full
from detecteur.full_detecteur import DetecteurFull
from manipuler_cartes import ManipulerCartes

#♣♥♦♠    
def test_detecte_facilement_full_se_suivant(): 
    (DetecteurFullTest()
            .ajouter_carte("6♦")
            .ajouter_carte("8♠")
            .ajouter_carte("Q♦")
            .ajouter_carte("6♥")
            .ajouter_carte("Q♥")
            .ajouter_carte("2♥")
            .ajouter_carte("Q♠")
            .detecte_full()
            .valide_full("6", "Q"))
    
def test_detecte_full_avec_deux_valeurs_trois_exemplaires(): 
    (DetecteurFullTest()
            .ajouter_carte("6♦")
            .ajouter_carte("Q♦")
            .ajouter_carte("6♥")
            .ajouter_carte("Q♥")
            .ajouter_carte("2♥")
            .ajouter_carte("6♠")
            .ajouter_carte("Q♠")
            .detecte_full()
            .valide_full("6", "Q"))

class DetecteurFullTest():
    def __init__(self):
        self.toutes_les_cartes = []
        manipuler_cartes = ManipulerCartes()
        self.detecteur_full = DetecteurFull(manipuler_cartes)
        self.full_detecte = None

    def ajouter_carte(self, carte_chiffre): 
        carte = Carte.parse(carte_chiffre)
        self.toutes_les_cartes.append(carte)
        return self

    def detecte_full(self):
        self.full_detecte = self.detecteur_full.detecte_full(self.toutes_les_cartes)
        return self

    def valide_full(self, valeur_presente_deux_fois, valeur_presente_trois_fois):
        full_attendu = Full(Carte.parse_valeur(valeur_presente_deux_fois), Carte.parse_valeur(valeur_presente_trois_fois))
        egal = full_attendu.deux_fois == self.full_detecte.deux_fois and full_attendu.trois_fois == self.full_detecte.trois_fois
        assert(egal == True)