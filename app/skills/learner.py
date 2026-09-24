from pathlib import Path
import json

class SkillLearner:
    def __init__(self, directory: str = "data/skills"):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)

    def save_workflow(self, name: str, steps: list[str]) -> Path:
        safe = "".join(c for c in name if c.isalnum() or c in "-_").strip()
        if not safe:
            raise ValueError("Invalid skill name.")
        path = self.directory / f"{safe}.json"
        path.write_text(
            json.dumps({"name": name, "steps": steps}, indent=2),
            encoding="utf-8",
        )
        return path
