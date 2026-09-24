import os
from dataclasses import dataclass

@dataclass
class Settings:
    ai_provider: str = "openai"
    ai_model: str = "gpt-5.6-mini"
    openai_api_key: str | None = None
    browser_enabled: bool = False
    computer_enabled: bool = False
    voice_enabled: bool = False

    @classmethod
    def load(cls) -> "Settings":
        return cls(
            ai_provider=os.getenv("JARVIS_AI_PROVIDER", "openai"),
            ai_model=os.getenv("JARVIS_AI_MODEL", "gpt-5.6-mini"),
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            browser_enabled=os.getenv("JARVIS_BROWSER_ENABLED", "false").lower() == "true",
            computer_enabled=os.getenv("JARVIS_COMPUTER_ENABLED", "false").lower() == "true",
            voice_enabled=os.getenv("JARVIS_VOICE_ENABLED", "false").lower() == "true",
        )
