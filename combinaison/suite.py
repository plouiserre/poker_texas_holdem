from dataclasses import dataclass
from carte import ValeurCarte
from typing import ClassVar

@dataclass(frozen=True)
class Suite : 
    valeur : ValeurCarte
    points : ClassVar[int] = 50