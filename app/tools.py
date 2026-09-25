from pathlib import Path
import webbrowser

class ToolBox:
    def __init__(self, browser_enabled=False, computer_enabled=False):
        self.browser_enabled = browser_enabled
        self.computer_enabled = computer_enabled

    def open_url(self, url: str) -> str:
        if not self.browser_enabled:
            return "Browser control is disabled. Enable JARVIS_BROWSER_ENABLED=true."
        if not (url.startswith("https://") or url.startswith("http://")):
            return "Only http:// and https:// URLs are allowed."
        webbrowser.open(url)
        return f"Opened {url}"

    def list_files(self, folder: str) -> str:
        p = Path(folder).expanduser().resolve()
        if not p.exists() or not p.is_dir():
            return f"Folder not found: {p}"
        items = list(p.iterdir())
        if not items:
            return "(empty)"
        return "\n".join(("DIR  " if x.is_dir() else "FILE ") + x.name for x in items[:200])

    def create_folder(self, folder: str) -> str:
        p = Path(folder).expanduser()
        p.mkdir(parents=True, exist_ok=True)
        return f"Created folder: {p.resolve()}"

    def delete_path(self, path: str) -> str:
        p = Path(path).expanduser()
        if not p.exists():
            return f"Not found: {p}"
        if p.is_dir():
            p.rmdir()
        else:
            p.unlink()
        return f"Deleted: {p.resolve()}"

    def computer_press(self, key: str) -> str:
        if not self.computer_enabled:
            return "Computer control is disabled. Enable JARVIS_COMPUTER_ENABLED=true."
        try:
            import pyautogui
            pyautogui.press(key)
            return f"Pressed {key}."
        except Exception as exc:
            return f"Computer-control error: {exc}"
