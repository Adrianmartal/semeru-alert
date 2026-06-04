"""Semeru Alert AI - Registry Agent (manage resident phone numbers)"""

from tools.registry_tool import RegistryTool
from core.state import Zone


class RegistryAgent:

    def __init__(self):
        self.tool = RegistryTool()

    def register(self, name: str, phone: str, zone: Zone):
        self.tool.add(name, phone, zone)
        print(f"[Registry] Registered: {name} ({phone}) - Zone {zone.value}")

    def list_all(self):
        return self.tool.list_all()

    def total(self) -> int:
        return len(self.tool.list_all())
