class Integration:
    name = "base"

    def enabled(self) -> bool:
        return False

    def status(self) -> str:
        return f"{self.name}: not configured"
