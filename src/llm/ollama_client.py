import ollama
from src.logger import Logger

log = Logger()


class Ollama:
    def __init__(self):
        try:
            self.client = ollama.Client()
            log.info("Ollama available")
        except:
            self.client = None
            log.warning("Ollama not available")
            log.warning("run ollama server to use ollama models otherwise use other models")

    def list_models(self) -> list[dict]:
        models = self.client.list()["models"]
        return models

    def inference(self, model_id: str, prompt: str) -> str:
        response = self.client.generate(
            model=model_id,
            prompt=prompt.strip()
        )
        return response['response']
