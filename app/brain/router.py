class BrainRouter:
    def __init__(self, ai_client):
        self.ai = ai_client

    def answer(self, message: str) -> str:
        return self.ai.ask(message)
