from typing import Literal

from .inputs import EngineInputs, PropellantInputs, FeedSystemInputs, DesignChoices
from .base import Injector
from .impinging import ImpingingInjector, ImpingingDesign
from .pintle import PintleInjector, PintleDesign
from .coax import CoaxInjector, CoaxDesign

InjectorType = Literal["impinging", "pintle", "coax"]


class InjectorFactory:
    @staticmethod
    def create(
        injector_type: InjectorType,
        engine: EngineInputs,
        prop: PropellantInputs,
        feed: FeedSystemInputs,
        design: DesignChoices,
    ) -> Injector:
        print(f"[InjectorFactory.create] Creating injector_type={injector_type}")

        if injector_type == "impinging":
            if not isinstance(design, ImpingingDesign):
                raise TypeError("design must be ImpingingDesign for impinging")
            return ImpingingInjector(engine, prop, feed, design)

        if injector_type == "pintle":
            if not isinstance(design, PintleDesign):
                raise TypeError("design must be PintleDesign for pintle")
            return PintleInjector(engine, prop, feed, design)

        if injector_type == "coax":
            if not isinstance(design, CoaxDesign):
                raise TypeError("design must be CoaxDesign for coax")
            return CoaxInjector(engine, prop, feed, design)

        raise ValueError(f"Unknown injector_type: {injector_type}")
