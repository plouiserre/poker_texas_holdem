from dataclasses import dataclass
from carte import ValeurCarte
from typing import ClassVar

@dataclass(frozen=True)
class Paire : 
    valeur : ValeurCarte
    carte_haute_valeur_hors_paire: ValeurCarte
    points : ClassVar[int] = 20