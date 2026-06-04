"""
Semeru Alert AI - Main Entry Point

Usage:
  python main.py --level 4 --message "Terjadi erupsi besar, lava mengalir ke arah selatan"
  python main.py --level 2 --message "Peningkatan aktivitas kegempaan"
"""

import argparse
from core.state import AlertState, AlertLevel
from agents.alert_agent import AlertAgent


def main():
    parser = argparse.ArgumentParser(description="Semeru Alert AI")
    parser.add_argument("--level",   type=int, required=True, help="Alert level 1-4")
    parser.add_argument("--message", type=str, required=True, help="Raw message from monitoring team")
    args = parser.parse_args()

    print("\n" + "█"*55)
    print("  🌋  Semeru Alert AI — Emergency Broadcast System")
    print("  Powered by AMD ROCm + LangGraph + Ollama")
    print("█"*55 + "\n")

    state = AlertState(
        level=AlertLevel(args.level),
        raw_message=args.message,
    )

    agent = AlertAgent()
    result = agent.run(state)

    print(f"\n{'─'*55}")
    print(f"✅ Broadcast complete!")
    print(f"   Delivered : {result.delivered}")
    print(f"   Failed    : {result.failed}")
    print(f"   Zones     : {[z.value for z in result.target_zones]}")
    print(f"{'─'*55}\n")


if __name__ == "__main__":
    main()
