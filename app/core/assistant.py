from app.core.approval import ApprovalManager
from app.core.router import CommandRouter
from app.memory.store import MemoryStore
from app.skills.registry import SkillRegistry

class Jarvis:
    def __init__(self) -> None:
        self.memory = MemoryStore()
        self.approval = ApprovalManager()
        self.skills = SkillRegistry()
        self.router = CommandRouter(self.memory, self.approval, self.skills)

    def run(self) -> None:
        print("JARVIS online.")
        print("Type 'help' for commands. Type 'exit' to quit.")
        while True:
            try:
                command = input("\nYou: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nJARVIS: Goodbye.")
                break

            if not command:
                continue

            if command.lower() in {"exit", "quit"}:
                print("JARVIS: Goodbye.")
                break

            response = self.router.handle(command)
            print(f"JARVIS: {response}")
