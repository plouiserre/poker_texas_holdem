from dataclasses import dataclass
from carte import ValeurCarte
from typing import ClassVar

@dataclass(frozen=True)
class CarteHaute : 
    valeur : ValeurCarte
    points : ClassVar[int] = 10