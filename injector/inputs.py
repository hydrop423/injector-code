from dataclasses import dataclass
from typing import Optional


@dataclass
class EngineInputs:
    Pc = 21.6, #bar
    Dc = 0.105, #m
    MR = 2, # LOX/fuel


@dataclass
class PropellantInputs:
    LOX_density = 1.141, #kg/L
    LOX_temperature = 90, #K
    LOX_m_dot = 3.24, #kg/s
    LOX_volume_flow = 2.8396, #L/s

    fuel_density = 0.8, #kg/L
    fuel_temperature = 293, #K
    fuel_m_dot = 1.62, #kg/s
    fuel_volume_flow = 2.0250, #L/s


@dataclass
class FeedSystemInputs:
    LOX_inlet_pressure = 25.92, #bar
    LOX_pressure_drop = 4.32, #bar

    fuel_inlet_pressure = 25.92, #bar
    fuel_pressure_drop = 4.32, #bar


@dataclass
class DesignChoices:
    pass