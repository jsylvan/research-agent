"""
my_researcher.py

Extends the built-in MetaGPT `Researcher` role, hooking in your multi-model config.
"""

import asyncio
from metagpt.roles.researcher import Researcher
from config.llm_config import LLMConfig

class MyResearcher(Researcher):
    def __init__(self, config_path="config/settings.yaml", purpose="summarization"):
        super().__init__()
        self._llm_config = LLMConfig(config_path)
        self._model_info = self._llm_config.get_model_config(purpose)
        self.purpose = purpose

    async def run_my_custom_research(self, topic: str) -> dict:
        await asyncio.sleep(0.1)
        summary = f"[{self._model_info.get('model_name')}] Summaries about {topic}..."
        confidence = 0.9 if self.purpose == "advanced_reasoning" else 0.7
        return {
            "topic": topic,
            "summary": summary,
            "confidence": confidence,
            "model_used": self._model_info.get('model_name')
        }
