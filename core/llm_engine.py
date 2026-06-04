"""Semeru Alert AI - ROCm LLM Engine"""

import os
from langchain_community.llms import Ollama


def get_llm():
    return Ollama(
        model=os.getenv("LLM_MODEL", "mistral"),
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        temperature=0.3,  # Low temp for factual emergency messages
    )
