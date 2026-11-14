from enum import IntEnum, Enum
from typing import Self


class CouleurCarte(Enum) : 
    INDEFINI = 0
    TREFLES = 15
    CARREAUX = 16
    COEURS = 17
    PIQUES = 18

class ValeurCarte(IntEnum) : 
    INDEFINI = 0
    DEUX = 2
    TROIS = 3
    QUATRE = 4
    CINQ = 5
    SIX = 6
    SEPT = 7
    HUIT = 8
    NEUF = 9
    DIX = 10
    VALET = 11
    DAME = 12
    ROI = 13
    AS = 14

class Carte: 
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __eq__(self, autre):
        return self.valeur == autre.valeur and self.couleur == autre.couleur

    def __hash__(self):
        return hash((self.valeur, self.couleur))
    
    def render(self) -> str: 
        transcription = ""
        number = ""
        couleur = ""
        if self.valeur == ValeurCarte.AS: 
            number = "A"
        elif self.valeur == ValeurCarte.ROI : 
            number = "K"
        elif self.valeur == ValeurCarte.DAME :
            number = "Q"
        elif self.valeur == ValeurCarte.VALET : 
            number = "J"
        else : 
            number = str(self.valeur)
        if self.couleur == CouleurCarte.PIQUES :
            couleur = "♠"
        elif self.couleur == CouleurCarte.COEURS : 
            couleur = "♥"
        elif self.couleur == CouleurCarte.CARREAUX : 
            couleur = "♦"
        else : 
            couleur = "♣"
        transcription = number+couleur
        return transcription        
    
    @staticmethod
    def parse(str) -> Self:
        couleur_carte = CouleurCarte.INDEFINI
        valeur_carte = ValeurCarte.INDEFINI
        couleur_carte = Carte.parse_couleur(str)
        valeur_carte = Carte.parse_valeur(str)
        return Carte(valeur_carte, couleur_carte)
    
    @staticmethod
    def parse_couleur(str) -> CouleurCarte :
        couleur_carte = CouleurCarte.INDEFINI
        if "♠" in str : 
            couleur_carte = CouleurCarte.PIQUES
        elif "♥" in str : 
            couleur_carte = CouleurCarte.COEURS
        elif "♦" in str :
            couleur_carte = CouleurCarte.CARREAUX
        elif "♣" in str : 
            couleur_carte = CouleurCarte.TREFLES
        return couleur_carte
    
    @staticmethod
    def parse_valeur(str) -> ValeurCarte : 
        if "2" in str : 
            valeur_carte = ValeurCarte.DEUX
        elif "3" in str : 
            valeur_carte = ValeurCarte.TROIS
        elif "4" in str : 
            valeur_carte = ValeurCarte.FOUR
        elif "5" in str : 
            valeur_carte = ValeurCarte.CINQ
        elif "6" in str : 
            valeur_carte = ValeurCarte.SIX
        elif "7" in str : 
            valeur_carte = ValeurCarte.SEPT
        elif "8" in str : 
            valeur_carte = ValeurCarte.HUIT
        elif "9" in str : 
            valeur_carte = ValeurCarte.NEUF
        elif "10" in str : 
            valeur_carte = ValeurCarte.DIX
        elif "J" in str : 
            valeur_carte = ValeurCarte.VALET
        elif "Q" in str : 
            valeur_carte = ValeurCarte.DAME
        elif "K" in str : 
            valeur_carte = ValeurCarte.ROI
        elif "A" in str : 
            valeur_carte = ValeurCarte.AS
        else : 
            valeur_carte = ValeurCarte.INDEFINI
        return valeur_carte