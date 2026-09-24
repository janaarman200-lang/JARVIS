class Researcher:
    """Research adapter. Web search integration is intentionally isolated here."""

    def research(self, query: str) -> str:
        return (
            "Research connector is not enabled yet. "
            "This module is the extension point for web research."
        )
