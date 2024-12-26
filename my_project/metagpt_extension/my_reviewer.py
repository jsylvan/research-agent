"""
my_reviewer.py
Chain-of-thought code review approach
"""
import openai
import asyncio
from config.llm_config import LLMConfig
from metagpt.roles.review import Reviewer
from metagpt.logs import logger

class MyReviewer(Reviewer):
    def __init__(self, config_path="config/settings.yaml", purpose="summarization"):
        super().__init__()
        self._llm_config = LLMConfig(config_path)
        self._model_info = self._llm_config.get_model_config(purpose)
        self.purpose = purpose

        openai.api_key = self._model_info.get("api_key")
        openai.api_base = self._model_info.get("base_url")

    async def review_code(self, code_snippets: dict) -> dict:
        logger.info("[MyReviewer] chain-of-thought code review.")
        code_text = code_snippets.get("content", "No code provided")
        system_prompt = "You are a code reviewer. Use chain-of-thought internally, but final response is a short review."
        user_prompt = f"Review this code:\n{code_text}\nGive suggestions for improvement."

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
            return {"role": "Reviewer", "content": final_text}
        except Exception as e:
            logger.error(f"[MyReviewer] LLM error: {str(e)}")
            return {"error": str(e)}
