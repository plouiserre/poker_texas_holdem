from dataclasses import dataclass
from carte import CouleurCarte, ValeurCarte

from typing import ClassVar

@dataclass(frozen=True)
class QuinteFlush : 
    valeur : ValeurCarte
    couleur : CouleurCarte
    points : ClassVar[int] = 90