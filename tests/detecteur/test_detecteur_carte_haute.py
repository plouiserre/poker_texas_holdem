from carte import Carte
from combinaison.carte_haute import CarteHaute
from detecteur.carte_haute_detecteur import CarteHauteDetecteur

#♣♥♦♠    
def test_detecte_carte_haute_reine():
    (DetecteurCarteHauteTest()
        .ajouter_carte("2♣")
        .ajouter_carte("3♦")
        .ajouter_carte("9♦")
        .ajouter_carte("10♥")
        .ajouter_carte("Q♠")
        .ajouter_carte("3♣")
        .ajouter_carte("7♠")
        .detecte_carte_haute()
        .valide_carte_haute("Q"))

class DetecteurCarteHauteTest : 
    def __init__(self):
        self.toutes_les_cartes = []
        self.carte_haute_detecte = None
        self.carte_haute_detecteur = CarteHauteDetecteur()

    def ajouter_carte(self, carte_chiffre):
        carte = Carte.parse(carte_chiffre)
        self.toutes_les_cartes.append(carte)
        return self

    def detecte_carte_haute(self):
        self.carte_haute_detecte = self.carte_haute_detecteur.detecte_carte_haute(self.toutes_les_cartes)
        return self

    def valide_carte_haute(self, valeur_carte_haute):
        valeur_carte_haute_attendu = CarteHaute(Carte.parse_valeur(valeur_carte_haute))
        egal = self.carte_haute_detecte.valeur == valeur_carte_haute_attendu.valeur
        assert(egal == True)