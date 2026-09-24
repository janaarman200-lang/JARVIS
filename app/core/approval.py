from dataclasses import dataclass

@dataclass(frozen=True)
class ApprovalDecision:
    required: bool
    approved: bool = False

class ApprovalManager:
    CONSEQUENTAL_KEYWORDS = (
        "pay", "purchase", "buy", "delete", "remove",
        "publish", "send", "post", "security", "password",
        "account settings", "advertisement", "ad campaign",
    )

    def requires_approval(self, command: str) -> bool:
        text = command.lower()
        return any(keyword in text for keyword in self.CONSEQUENTAL_KEYWORDS)

    def request(self, command: str) -> ApprovalDecision:
        print(f"JARVIS: This may have a consequential effect: {command}")
        answer = input("JARVIS: Approve this action? [yes/no]: ").strip().lower()
        return ApprovalDecision(required=True, approved=answer in {"yes", "y"})

    def check(self, command: str) -> ApprovalDecision:
        if not self.requires_approval(command):
            return ApprovalDecision(required=False, approved=True)
        return self.request(command)
