from dataclasses import dataclass
from carte import ValeurCarte
from typing import ClassVar

@dataclass(frozen=True)
class Full : 
    deux_fois : ValeurCarte
    trois_fois : ValeurCarte
    points : ClassVar[int] = 70