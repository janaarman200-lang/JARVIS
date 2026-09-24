class SkillRegistry:
    def __init__(self) -> None:
        self._skills: dict[str, str] = {}

    def register(self, name: str, description: str) -> None:
        self._skills[name] = description

    def names(self) -> list[str]:
        return sorted(self._skills)
