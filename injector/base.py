from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple

from .inputs import EngineInputs, PropellantInputs, FeedSystemInputs, DesignChoices


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
        #Catch errors or missing data BEFORE running size()
        print("[Injector.validate_inputs] This is the base validation (placeholder).")

    @abstractmethod
    def size(self) -> Dict[str, Any]:
        #Main method to size the injector
        raise NotImplementedError

    @abstractmethod
    def check_constraints(self) -> None:
        #Validate the results AFTER running size(). Sanity check and manufacturable
        raise NotImplementedError

    def report(self, geometry: Dict[str, Any]) -> Dict[str, Any]:
        #Output results. Print, CSV, plots, etc.
        print("[Injector.report] Returning placeholder report dict.")
        return {
            "injector_type": self.__class__.__name__,
            "geometry": geometry,
            "sanity": 3 + 2,
        }