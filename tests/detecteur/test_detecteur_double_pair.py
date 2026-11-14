from carte import Carte, ValeurCarte
from combinaison.double_paire import DoublePaire
from detecteur.double_paire_detecteur import DoublePairDetecteur
from manipuler_cartes import ManipulerCartes

#♣♥♦♠    
def test_detecte_facilement_double_pairs_se_suivant():
    (DetectorDoublePairTest()
        .ajouter_carte("6♦")
        .ajouter_carte("6♥")
        .ajouter_carte("Q♠")
        .ajouter_carte("Q♦")
        .ajouter_carte("Q♥")
        .ajouter_carte("8♠")
        .ajouter_carte("2♥")
        .detecte_double_paires()
        .valide_double_paires("Q", "6", "8"))

def test_ne_detecte_aucune_double_pairs():
    (DetectorDoublePairTest()
        .ajouter_carte("6♦")
        .ajouter_carte("K♥")
        .ajouter_carte("Q♠")
        .ajouter_carte("Q♦")
        .ajouter_carte("10♥")
        .ajouter_carte("8♠")
        .ajouter_carte("2♥")
        .detecte_double_paires()
        .trouve_aucune_double_paires())
    
def test_detecte_double_pairs_bien_melanges():
            (DetectorDoublePairTest()
                .ajouter_carte("6♦")
                .ajouter_carte("8♠")
                .ajouter_carte("Q♦")
                .ajouter_carte("6♥")
                .ajouter_carte("Q♠")
                .ajouter_carte("2♥")
                .ajouter_carte("Q♥")
                .detecte_double_paires()
                .valide_double_paires("Q", "6", "8"))

class DetectorDoublePairTest():
    def __init__(self):
        self.toutes_les_cartes = []
        self.double_paires_detecte = None
        manipuler_cartes = ManipulerCartes()
        self.double_paire_detecteur = DoublePairDetecteur(manipuler_cartes)

    def ajouter_carte(self, card_crypted):
        card = Carte.parse(card_crypted)
        self.toutes_les_cartes.append(card)
        return self

    def detecte_double_paires(self):
        self.double_paires_detecte = self.double_paire_detecteur.trouve_double_paire(self.toutes_les_cartes)
        return self

    def valide_double_paires(self, valeur_premiere_paire, valeur_seconde_paire, valeur_haute_carte):
        double_paires_attendues = DoublePaire(Carte.parse_valeur(valeur_premiere_paire), Carte.parse_valeur(valeur_seconde_paire), Carte.parse_valeur(valeur_haute_carte))
        egal = self.double_paires_detecte.valeur_premiere_paire == double_paires_attendues.valeur_premiere_paire and self.double_paires_detecte.valeur_seconde_paire == double_paires_attendues.valeur_seconde_paire and self.double_paires_detecte.haute_valeur_reste_carte == double_paires_attendues.haute_valeur_reste_carte
        assert(egal == True)

    def trouve_aucune_double_paires(self):
        assert(self.double_paires_detecte == None)