"""Semeru Alert AI - Registry Tool"""

from core.state import Zone

# Mock resident data — replace with DB in production
_REGISTRY: list[dict] = [
    {"name": "Pak Slamet",  "phone": "+6281111000001", "zone": Zone.KM3},
    {"name": "Bu Wati",     "phone": "+6281111000002", "zone": Zone.KM3},
    {"name": "Pak Darto",   "phone": "+6281111000003", "zone": Zone.KM5},
    {"name": "Bu Yanti",    "phone": "+6281111000004", "zone": Zone.KM5},
    {"name": "Pak Rudi",    "phone": "+6281111000005", "zone": Zone.KM10},
]


class RegistryTool:

    def add(self, name: str, phone: str, zone: Zone):
        _REGISTRY.append({"name": name, "phone": phone, "zone": zone})

    def list_all(self) -> list[dict]:
        return _REGISTRY

    def get_by_zones(self, zones: list[Zone]) -> list[str]:
        return [r["phone"] for r in _REGISTRY if r["zone"] in zones]
