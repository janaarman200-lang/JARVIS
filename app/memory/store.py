import json
from pathlib import Path

class MemoryStore:
    def __init__(self, path: str = "data/memory/memory.json") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._items = self._load()

    def _load(self) -> list[str]:
        if not self.path.exists():
            return []
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            return data if isinstance(data, list) else []
        except (OSError, json.JSONDecodeError):
            return []

    def _save(self) -> None:
        self.path.write_text(
            json.dumps(self._items, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def add(self, value: str) -> None:
        self._items.append(value)
        self._save()

    def all(self) -> list[str]:
        return list(self._items)
