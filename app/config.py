import os
from dataclasses import dataclass

@dataclass
class Settings:
    ai_provider:str='openai'; ai_model:str='gpt-5.6-luna'; openai_api_key:str|None=None
    browser_enabled:bool=False; computer_enabled:bool=False; voice_enabled:bool=False
    @classmethod
    def load(cls):
        return cls(os.getenv('JARVIS_AI_PROVIDER','openai'),os.getenv('JARVIS_AI_MODEL','gpt-5.6-luna'),os.getenv('OPENAI_API_KEY'),os.getenv('JARVIS_BROWSER_ENABLED','false').lower()=='true',os.getenv('JARVIS_COMPUTER_ENABLED','false').lower()=='true',os.getenv('JARVIS_VOICE_ENABLED','false').lower()=='true')
