from dataclasses import dataclass
from carte import ValeurCarte
from typing import ClassVar

@dataclass
class Brelan : 
    valeur : ValeurCarte
    carte_haute_hors_brelan : ValeurCarte
    points : ClassVar[int] = 40