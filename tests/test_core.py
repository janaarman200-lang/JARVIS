import tempfile
import unittest
from pathlib import Path

from app.core.approval import ApprovalManager
from app.memory.store import MemoryStore

class CoreTests(unittest.TestCase):
    def test_safe_command_does_not_require_approval(self):
        self.assertFalse(ApprovalManager().requires_approval("what is the weather"))

    def test_consequential_command_requires_approval(self):
        self.assertTrue(ApprovalManager().requires_approval("delete this file"))

    def test_memory_persists(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "memory.json"
            store = MemoryStore(str(path))
            store.add("JARVIS test")
            restored = MemoryStore(str(path))
            self.assertEqual(restored.all(), ["JARVIS test"])

if __name__ == "__main__":
    unittest.main()
