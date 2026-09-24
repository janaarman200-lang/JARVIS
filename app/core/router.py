from app.memory.store import MemoryStore
from app.skills.registry import SkillRegistry
from app.core.approval import ApprovalManager

class CommandRouter:
    def __init__(
        self,
        memory: MemoryStore,
        approval: ApprovalManager,
        skills: SkillRegistry,
    ) -> None:
        self.memory = memory
        self.approval = approval
        self.skills = skills

    def handle(self, command: str) -> str:
        lowered = command.lower().strip()

        if lowered == "help":
            return self.help_text()

        if lowered == "memory":
            items = self.memory.all()
            if not items:
                return "Memory is empty."
            return "\n".join(f"- {item}" for item in items)

        if lowered.startswith("remember "):
            value = command[9:].strip()
            if not value:
                return "Tell me what you want me to remember."
            self.memory.add(value)
            return "Saved to local memory."

        if lowered == "skills":
            names = self.skills.names()
            return "Skills: " + (", ".join(names) if names else "none")

        decision = self.approval.check(command)
        if decision.required and not decision.approved:
            return "Action cancelled."

        return (
            "I received your command. The core foundation is working, "
            "but this capability has not been connected yet. "
            "The next stages will add the AI brain, research, browser and computer control."
        )

    @staticmethod
    def help_text() -> str:
        return (
            "Commands:\n"
            "- help — show commands\n"
            "- remember <text> — save local memory\n"
            "- memory — view local memory\n"
            "- skills — list installed skills\n"
            "- exit — close JARVIS"
        )
