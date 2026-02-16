from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple

from .models import EngineInputs, PropellantInputs, FeedSystemInputs, DesignChoices


class Injector(ABC):
    """Abstract base injector class."""

    def __init__(
        self,
        engine: EngineInputs,
        prop: PropellantInputs,
        feed: FeedSystemInputs,
        design: DesignChoices,
    ) -> None:
        self.engine = engine
        self.prop = prop
        self.feed = feed
        self.design = design

    def run(self) -> Dict[str, Any]:
        """
        Skeleton pipeline:
        validate -> size -> check -> report
        """
        print(f"[Injector.run] Running {self.__class__.__name__}")
        self.validate_inputs()
        geom = self.size()
        self.check_constraints()
        return self.report(geom)

    def validate_inputs(self) -> None:
        """Placeholder validation."""
        print("[Injector.validate_inputs] This is the base validation (placeholder).")

    @abstractmethod
    def size(self) -> Dict[str, Any]:
        """Compute geometry (type-specific)."""
        raise NotImplementedError

    @abstractmethod
    def check_constraints(self) -> None:
        """Type-specific constraint checks (placeholder)."""
        raise NotImplementedError

    def report(self, geometry: Dict[str, Any]) -> Dict[str, Any]:
        """Return a dict that proves the pipeline ran."""
        print("[Injector.report] Returning placeholder report dict.")
        return {
            "injector_type": self.__class__.__name__,
            "geometry": geometry,
            "sanity": 3 + 2,  # placeholder proof-of-life
        }