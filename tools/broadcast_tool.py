"""Semeru Alert AI - Broadcast Tool (mock)"""

import time


class BroadcastTool:

    def send_bulk(self, recipients: list[str], message: str) -> dict:
        delivered, failed = 0, 0
        for number in recipients:
            # TODO: replace with real WA Business API call
            print(f"  📲 Sending to {number}... ✅")
            time.sleep(0.05)
            delivered += 1
        return {"delivered": delivered, "failed": failed}
