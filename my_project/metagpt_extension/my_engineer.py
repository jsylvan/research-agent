"""
my_engineer.py
Now real chain-of-thought openai calls for code stubs.
"""
import openai
import asyncio
from config.llm_config import LLMConfig
from metagpt.roles.engineer import Engineer
from metagpt.logs import logger

class MyEngineer(Engineer):
    def __init__(self, config_path="config/settings.yaml", purpose="advanced_reasoning"):
        super().__init__()
        self._llm_config = LLMConfig(config_path)
        self._model_info = self._llm_config.get_model_config(purpose)
        self.purpose = purpose

        openai.api_key = self._model_info.get("api_key")
        openai.api_base = self._model_info.get("base_url")

    async def implement_code(self, architecture: dict) -> dict:
        logger.info("[MyEngineer] chain-of-thought code generation.")
        arch_text = architecture.get("content", "No arch design")
        system_prompt = "You are a senior engineer. Use chain-of-thought to figure out an implementation approach. Present final code idea only."
        user_prompt = f"Architecture:\n{arch_text}\nGenerate some code stubs in Node.js and React."

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
            return {"role": "Engineer", "content": final_text}
        except Exception as e:
            logger.error(f"[MyEngineer] LLM error: {str(e)}")
            return {"error": str(e)}
