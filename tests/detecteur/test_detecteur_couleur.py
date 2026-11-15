from carte import Carte, CouleurCarte, ValeurCarte
from combinaison.couleur import Couleur
from detecteur.couleur_detecteur import CouleurDetecteur

#♣♥♦♠    
def test_detecte_facilement_couleur_se_suivant():
    (DetectorCouleurTest()
        .ajouter_carte("6♦")
        .ajouter_carte("8♥")
        .ajouter_carte("J♥")
        .ajouter_carte("6♥")
        .ajouter_carte("2♥")
        .ajouter_carte("Q♥")
        .ajouter_carte("9♣")
        .detecte_couleur()
        .valide_couleur("♥", "Q"))


def test_ne_trouve_aucune_couleur():
    (DetectorCouleurTest()
        .ajouter_carte("6♦")
        .ajouter_carte("8♠")
        .ajouter_carte("Q♦")
        .ajouter_carte("6♥")
        .ajouter_carte("2♥")
        .ajouter_carte("Q♥")
        .ajouter_carte("Q♠")
        .detecte_couleur()
        .trouve_aucune_couleur())


class DetectorCouleurTest : 
    def __init__(self):
        self.toutes_les_cartes = []
        self.couleur_trouve = Couleur(CouleurCarte.INDEFINI, ValeurCarte.INDEFINI)
        self.couleur_detecteur = CouleurDetecteur()

    def ajouter_carte(self, carte_chiffre): 
        carte = Carte.parse(carte_chiffre)
        self.toutes_les_cartes.append(carte)
        return self

    def detecte_couleur(self):
        self.couleur_trouve = self.couleur_detecteur.trouve_couleur(self.toutes_les_cartes)
        return self

    def valide_couleur(self, couleur_chiffre, valeur_haute_chiffre):
        couleur_carte  = Carte.parse_couleur(couleur_chiffre)
        valeur_haute = Carte.parse_valeur(valeur_haute_chiffre)
        couleur_attendu = Couleur(couleur_carte, valeur_haute)
        egal = self.couleur_trouve.couleur == couleur_attendu.couleur and self.couleur_trouve.valeur_haute == couleur_attendu.valeur_haute
        assert(egal == True)

    def trouve_aucune_couleur(self): 
        assert(self.couleur_trouve == None)
