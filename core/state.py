"""Semeru Alert AI - Shared State"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class AlertLevel(int, Enum):
    NORMAL = 1
    WASPADA = 2
    SIAGA = 3
    AWAS = 4


class Zone(str, Enum):
    KM3  = "3km"
    KM5  = "5km"
    KM10 = "10km"
    ALL  = "all"


ZONE_BY_LEVEL = {
    AlertLevel.WASPADA: [Zone.KM3],
    AlertLevel.SIAGA:   [Zone.KM3, Zone.KM5],
    AlertLevel.AWAS:    [Zone.KM3, Zone.KM5, Zone.KM10],
}


@dataclass
class AlertState:
    level: AlertLevel
    raw_message: str              # Input dari tim pemantau
    composed_message: str = ""    # Hasil AI drafting
    target_zones: list[Zone] = field(default_factory=list)
    recipients: list[str] = field(default_factory=list)
    delivered: int = 0
    failed: int = 0
    broadcast_done: bool = False
