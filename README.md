# 🌋 Semeru Alert AI

> **Autonomous AI agent for emergency volcanic alert broadcasting via WhatsApp — powered by AMD ROCm**

[![ROCm](https://img.shields.io/badge/AMD-ROCm%206.x-ED1C24?logo=amd&logoColor=white)](https://rocm.docs.amd.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.2.x-1C3C3C)](https://langchain-ai.github.io/langgraph/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🚨 What is Semeru Alert AI?

Semeru Alert AI is an **autonomous emergency broadcasting system** built for volcanic monitoring posts. When volcanic activity escalates, the system instantly broadcasts SOS alerts to all registered residents via WhatsApp — without delay, without manual effort.

**The problem it solves:** Monitoring teams at active volcanoes like Mount Semeru often struggle to relay emergency information quickly enough to surrounding communities. This AI agent automates the entire alert chain.

```
Monitoring Team → [Input: Alert Level + Message] → Semeru Alert AI → WhatsApp Broadcast
                                                          ↓
                                              All registered residents notified
                                              in seconds, not minutes
```

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 📱 **Mass WhatsApp Broadcast** | Instantly sends SOS to all registered resident numbers |
| 🧠 **AI-Assisted Alert Drafting** | LLM helps compose clear, calm emergency messages |
| 📋 **Resident Registry** | Simple system to collect & manage resident phone numbers |
| 🔴 **Alert Level System** | Levels 1–4 matching PVMBG volcanic activity scale |
| 📍 **Zone-based Targeting** | Broadcast to specific radius zones (3km, 5km, 10km) |
| ⚡ **ROCm Accelerated** | LLM inference runs locally on AMD GPU |
| 🗂️ **Offline-ready** | Core broadcast works even with limited connectivity |

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────┐
│             Semeru Alert AI Core             │
│                                              │
│  ┌─────────────┐      ┌──────────────────┐   │
│  │  Alert      │      │  Registry        │   │
│  │  Agent      │      │  Agent           │   │
│  └──────┬──────┘      └────────┬─────────┘   │
│         │                     │              │
│         └──────────┬──────────┘              │
│                    │                         │
│          ┌─────────▼──────────┐              │
│          │   Orchestrator     │              │
│          │   (LangGraph)      │              │
│          └─────────┬──────────┘              │
│                    │                         │
│          ┌─────────▼──────────┐              │
│          │  ROCm LLM Engine   │              │
│          │  (Ollama)          │              │
│          └────────────────────┘              │
└──────────────────────────────────────────────┘
              │
    ┌─────────▼──────────┐
    │  WhatsApp Broadcast │
    │  (Mock / WA API)   │
    └────────────────────┘
```

---

## 🔴 Alert Level Reference (PVMBG Scale)

| Level | Status | Action |
|---|---|---|
| 1 | Normal | No broadcast |
| 2 | Waspada | Info broadcast to zone 3km |
| 3 | Siaga | Alert broadcast to zone 5km |
| 4 | Awas | **SOS broadcast to ALL zones** |

---

## 🗂️ Project Structure

```
semeru-alert/
├── agents/
│   ├── orchestrator.py      # LangGraph pipeline
│   ├── alert_agent.py       # Compose & broadcast alerts
│   └── registry_agent.py    # Manage resident numbers
├── core/
│   ├── llm_engine.py        # AMD ROCm / Ollama interface
│   ├── state.py             # Shared state schema
│   └── config.py            # Alert zones & settings
├── mock/
│   ├── whatsapp_mock.py     # Terminal WA simulator
│   └── mock_data.py         # Sample resident data
├── tools/
│   ├── broadcast_tool.py    # Mass message sender
│   └── registry_tool.py    # Phone number CRUD
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/semeru-alert.git
cd semeru-alert
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### Run Demo

```bash
python main.py --level 4 --zone all
```

**Sample output:**
```
[ALERT] Level 4 - AWAS detected
[LLM] Drafting emergency message...
[BROADCAST] Sending to 847 registered residents...
✅ Delivered to zone 3km: 312 residents
✅ Delivered to zone 5km: 289 residents
✅ Delivered to zone 10km: 246 residents
Total delivered: 847 | Failed: 0
```

---

## 🗺️ Roadmap

- [x] Core alert broadcasting architecture
- [x] Resident registry system
- [x] Alert level classification (PVMBG scale)
- [x] Mock WhatsApp interface
- [ ] Real WhatsApp Business API
- [ ] Web dashboard for monitoring post
- [ ] Auto-detect alert level from seismic sensor data
- [ ] Multi-volcano support
- [ ] SMS fallback for no-internet zones

---

## 🤝 Use Case Context

This project is developed in collaboration with volcanic monitoring post volunteers at Mount Semeru, East Java, Indonesia. The goal is to reduce emergency notification lag from minutes to seconds using AI-assisted broadcasting on affordable local hardware powered by AMD ROCm.

---

## 📄 License

MIT License
