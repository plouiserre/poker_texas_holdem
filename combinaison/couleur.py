from dataclasses import dataclass
from typing import ClassVar
from carte import CouleurCarte, ValeurCarte

@dataclass(frozen=True)
class Couleur : 
    couleur : CouleurCarte
    valeur_haute : ValeurCarte
    points : ClassVar[int] = 60