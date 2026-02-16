from dataclasses import dataclass
from typing import Optional


@dataclass
class EngineInputs:
    Pc: float
    Dc: float
    mdot_total: Optional[float] = None
    MR_target: Optional[float] = None


@dataclass
class PropellantInputs:
    rho_o: float
    rho_f: float
    mu_o: float
    mu_f: float


@dataclass
class FeedSystemInputs:
    dP_o: Optional[float] = None
    dP_f: Optional[float] = None
    Pin_o: Optional[float] = None
    Pin_f: Optional[float] = None


@dataclass
class DesignChoices:
    Cd_o: float = 0.85
    Cd_f: float = 0.85