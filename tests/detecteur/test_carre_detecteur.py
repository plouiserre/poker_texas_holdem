from carte import Carte
from combinaison.carre import Carre
from detecteur.carre_detecteur import CarreDetecteur
from manipuler_cartes import ManipulerCartes

def test_detecte_carre_king():
    (DetecteurCarreTest()
             .ajouter_carte("K♣")
             .ajouter_carte("Q♦")
             .ajouter_carte("K♦")
             .ajouter_carte("K♥")
             .ajouter_carte("K♠")
             .ajouter_carte("3♣")
             .ajouter_carte("A♠")
             .detecte_carre()
             .valide_carre("K", "A"))

class DetecteurCarreTest: 
    def __init__(self):
        self.toutes_les_cartes = []
        manipuler_cartes = ManipulerCartes()
        self.carre_detecteur = CarreDetecteur(manipuler_cartes)
        self.carre_detecte = None
    
    def ajouter_carte(self, carte_chiffre):
        carte = Carte.parse(carte_chiffre)
        self.toutes_les_cartes.append(carte)
        return self
    
    def detecte_carre(self):
        self.carre_detecte = self.carre_detecteur.detecte_carre(self.toutes_les_cartes)
        return self

    def valide_carre(self, valeur_carre, valeur_carte_haute_hors_carre):
        carre_attendu = Carre(Carte.parse_valeur(valeur_carre), Carte.parse_valeur(valeur_carte_haute_hors_carre)) 
        egal = self.carre_detecte.valeur == carre_attendu.valeur and self.carre_detecte.valeur_carte_hors_carre == carre_attendu.valeur_carte_hors_carre
        assert(egal == True)