import yaml
import os

class LLMConfig:
    def __init__(self, config_path: str = "config/settings.yaml"):
        with open(config_path, "r") as f:
            self._raw = yaml.safe_load(f)
        self._models = self._raw.get("llm", {}).get("models", {})

    def get_model_config(self, purpose: str) -> dict:
        if purpose not in self._models:
            raise ValueError(f"No model config found for purpose '{purpose}'")
        return self._models[purpose]

    @property
    def vector_store_path(self) -> str:
        return self._raw.get("vector_store", {}).get("db_path", "./vector_db")
    
    @property
    def search_api_config(self) -> dict:
        return self._raw.get("search_config", {})
