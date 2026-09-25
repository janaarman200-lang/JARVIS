from app.config import Settings
from app.core.approval import ApprovalManager
from app.core.router import CommandRouter
from app.memory.store import MemoryStore
from app.skills.registry import SkillRegistry
from app.brain.llm import AIClient
from app.tools import ToolBox

class Jarvis:
    def __init__(self):
        self.settings=Settings.load(); self.memory=MemoryStore(); self.approval=ApprovalManager(); self.skills=SkillRegistry(); self.ai=AIClient(self.settings)
        self.tools=ToolBox(self.settings.browser_enabled,self.settings.computer_enabled)
        self.router=CommandRouter(self.memory,self.approval,self.skills,self.ai,self.tools)
    def handle(self,command): return self.router.handle(command)
    def status(self): return 'AI: '+('connected' if self.ai.available() else 'not configured')+' | Browser: '+('on' if self.settings.browser_enabled else 'off')+' | Computer: '+('on' if self.settings.computer_enabled else 'off')
    def run(self):
        print('JARVIS online.'); print(self.status())
        while True:
            try:c=input('\nYou: ').strip()
            except (EOFError,KeyboardInterrupt): break
            if not c: continue
            if c.lower() in {'exit','quit'}: break
            print('JARVIS:',self.handle(c))
