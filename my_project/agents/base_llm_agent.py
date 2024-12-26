import openai
from config.llm_config import LLMConfig

class BaseLLMAgent:
    """
    Base class that picks a model from LLMConfig based on 'purpose',
    then runs a minimal openai call.
    """
    def __init__(self, config: LLMConfig, purpose: str = "summarization"):
        self.config = config
        self.purpose = purpose
        model_info = self.config.get_model_config(purpose)

        self.api_type = model_info.get("api_type", "openai")
        self.model_name = model_info.get("model_name", "gpt-3.5-turbo")
        self.base_url = model_info.get("base_url", "https://api.openai.com/v1")
        self.api_key = model_info.get("api_key", None)

        if self.api_type == "openai":
            openai.api_base = self.base_url
            openai.api_key = self.api_key

    def run(self, prompt: str) -> str:
        """
        Minimal ChatCompletion call
        """
        if self.api_type == "openai":
            response = openai.ChatCompletion.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )
            return response.choices[0].message["content"]
        else:
            raise NotImplementedError(f"API type '{self.api_type}' not implemented.")
