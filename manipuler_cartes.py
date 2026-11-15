
class ManipulerCartes : 
    def __init__(self):
        pass

    def compter_cartes(self, combinaison):
        comptage_cartes = {}
        for carte in combinaison : 
            if carte.valeur in comptage_cartes : 
                comptage_cartes[carte.valeur] += 1
            else : 
                comptage_cartes[carte.valeur] = 1
        return comptage_cartes

    def regrouper_par_couleur(self, combinaison):
        couleur_cartes = {}
        for carte in combinaison : 
            if carte.couleur in couleur_cartes : 
                couleur_cartes[carte.couleur] += 1
            else : 
                couleur_cartes[carte.couleur] = 1
        return couleur_cartes
