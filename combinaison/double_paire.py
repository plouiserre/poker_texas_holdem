from dataclasses import dataclass
from carte import ValeurCarte
from typing import ClassVar, Self


@dataclass(frozen=True)
class DoublePaire :
    valeur_premiere_paire : ValeurCarte
    valeur_seconde_paire : ValeurCarte
    haute_valeur_reste_carte : ValeurCarte
    points : ClassVar[int] = 30