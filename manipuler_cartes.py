
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
