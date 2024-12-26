"""
my_architect.py
Real LLM approach with chain-of-thought
"""

import openai
import asyncio
from config.llm_config import LLMConfig
from metagpt.roles.architect import Architect
from metagpt.logs import logger

class MyArchitect(Architect):
    def __init__(self, config_path="config/settings.yaml", purpose="advanced_reasoning"):
        super().__init__()
        self._llm_config = LLMConfig(config_path)
        self._model_info = self._llm_config.get_model_config(purpose)
        self.purpose = purpose

        openai.api_key = self._model_info.get("api_key")
        openai.api_base = self._model_info.get("base_url")

    async def produce_architecture(self, plan: str) -> dict:
        logger.info("[MyArchitect] calling real LLM chain-of-thought for architecture.")
        system_prompt = "You are an expert software architect. Provide a chain-of-thought internally, but present final design only."
        user_prompt = f"Plan: {plan}\nPropose an architecture in detail."

        try:
            resp = openai.ChatCompletion.create(
                model=self._model_info.get("model_name"),
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.7,
            )
            final_text = resp.choices[0].message["content"]
            return {"role": "Architect", "content": final_text}
        except Exception as e:
            logger.error(f"[MyArchitect] LLM error: {str(e)}")
            return {"error": str(e)}
