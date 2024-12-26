from config.llm_config import LLMConfig
from .base_llm_agent import BaseLLMAgent

class SummarizeAgent(BaseLLMAgent):
    def __init__(self, config: LLMConfig):
        super().__init__(config, purpose="summarization")

    def summarize_text(self, text: str) -> str:
        prompt = f"Please summarize this text:\n\n{text}\n\nShort summary:"
        return self.run(prompt)
