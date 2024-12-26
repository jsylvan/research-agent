from config.llm_config import LLMConfig
from .base_llm_agent import BaseLLMAgent

class AdvancedAgent(BaseLLMAgent):
    def __init__(self, config: LLMConfig):
        super().__init__(config, purpose="advanced_reasoning")

    def reason_about(self, query: str) -> str:
        prompt = f"Consider this request needing deep reasoning:\n\n{query}\n\nProvide a logical, detailed answer:"
        return self.run(prompt)
