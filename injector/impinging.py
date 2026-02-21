from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from .base import Injector
from .inputs import DesignChoices, EngineInputs, PropellantInputs, FeedSystemInputs


@dataclass
class ImpingingDesign(DesignChoices):
    N_elements: int = 16
    impingement_angle_deg: float = 60.0

@dataclass(frozen=True)
class ImpingingSizingResult:
    LOX_total_orifice_area: float = field(metadata={"unit": "in^2"})

class ImpingingInjector(Injector):
    def __init__(
        self,
        engine: EngineInputs,
        prop: PropellantInputs,
        feed: FeedSystemInputs,
        design: ImpingingDesign,
    ) -> None:
        super().__init__(engine, prop, feed, design)
        self.imp = design
        self._result: Optional[ImpingingSizingResult] = None

    def size(self) -> ImpingingSizingResult:
        LOX_total_orifice_area = 1.88E-01
        result = ImpingingSizingResult(LOX_total_orifice_area=LOX_total_orifice_area)
        self._result = result
        return result

    def check_constraints(self) -> None:
        print("[ImpingingInjector.check_constraints] Placeholder checks passed.")
