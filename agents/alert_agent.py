"""Semeru Alert AI - Alert Agent"""

from core.state import AlertState, AlertLevel, ZONE_BY_LEVEL
from core.llm_engine import get_llm
from tools.broadcast_tool import BroadcastTool
from tools.registry_tool import RegistryTool


COMPOSE_PROMPT = """Kamu adalah asisten penyusun pesan darurat bencana.
Susun pesan SOS yang jelas, singkat, dan tidak menimbulkan kepanikan berlebihan.
Gunakan Bahasa Indonesia yang mudah dipahami warga desa.

Level siaga: {level}
Informasi dari tim pemantau: {message}

Format pesan:
🚨 PERINGATAN GUNUNG SEMERU
Status: [level]
[isi pesan singkat, maks 3 kalimat]
Ikuti arahan petugas setempat."""


class AlertAgent:

    def __init__(self):
        self.broadcast = BroadcastTool()
        self.registry  = RegistryTool()

    def run(self, state: AlertState) -> AlertState:
        if state.level == AlertLevel.NORMAL:
            print("[AlertAgent] Level Normal, no broadcast needed.")
            return state

        # 1. Tentukan zona target
        state.target_zones = ZONE_BY_LEVEL.get(state.level, [])

        # 2. Compose pesan via LLM
        llm = get_llm()
        state.composed_message = llm.invoke(COMPOSE_PROMPT.format(
            level=state.level.name,
            message=state.raw_message,
        ))
        print(f"[AlertAgent] Message composed:\n{state.composed_message}")

        # 3. Ambil nomor berdasarkan zona
        state.recipients = self.registry.get_by_zones(state.target_zones)
        print(f"[AlertAgent] Recipients: {len(state.recipients)}")

        # 4. Broadcast
        result = self.broadcast.send_bulk(state.recipients, state.composed_message)
        state.delivered = result["delivered"]
        state.failed    = result["failed"]
        state.broadcast_done = True

        return state
