from dataclasses import dataclass
from typing import Any, Dict

from .base import Injector
from .models import DesignChoices, EngineInputs, PropellantInputs, FeedSystemInputs


@dataclass
class ImpingingDesign(DesignChoices):
    N_elements: int = 16
    impingement_angle_deg: float = 60.0


class ImpingingInjector(Injector):
    def __init__(
        self,
        engine: EngineInputs,
        prop: PropellantInputs,
        feed: FeedSystemInputs,
        design: ImpingingDesign,
    ) -> None:
        super().__init__(engine, prop, feed, design)
        self.imp = design  # convenience alias

    def size(self) -> Dict[str, Any]:
        print("[ImpingingInjector.size] Placeholder sizing.")
        # Return a minimal geometry dict to show wiring works
        return {
            "N_elements": self.imp.N_elements,
            "impingement_angle_deg": self.imp.impingement_angle_deg,
            "example_orifice_diameter_m": 0.001,  # placeholder
        }

    def check_constraints(self) -> None:
        print("[ImpingingInjector.check_constraints] Placeholder checks passed.")
