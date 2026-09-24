from app.config import Settings

class AIClient:
    def __init__(self, settings: Settings):
        self.settings = settings
        self._client = None
        if settings.ai_provider == "openai" and settings.openai_api_key:
            try:
                from openai import OpenAI
                self._client = OpenAI(api_key=settings.openai_api_key)
            except ImportError:
                pass

    def available(self) -> bool:
        return self._client is not None

    def ask(self, message: str, system: str = "") -> str:
        if not self._client:
            return (
                "AI provider is not configured yet. Set OPENAI_API_KEY locally "
                "and install the optional AI dependency."
            )
        response = self._client.responses.create(
            model=self.settings.ai_model,
            instructions=system or "You are JARVIS, a safe personal AI assistant.",
            input=message,
        )
        return response.output_text
