from dataclasses import dataclass
from carte import ValeurCarte
from typing import ClassVar

@dataclass(frozen=True)
class Carre : 
    valeur : ValeurCarte
    valeur_carte_hors_carre: ValeurCarte
    points : ClassVar[int] = 80