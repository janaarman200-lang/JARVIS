class ComputerController:
    def __init__(self, enabled: bool = False):
        self.enabled = enabled

    def type_text(self, text: str) -> str:
        if not self.enabled:
            return "Computer control is disabled."
        try:
            import pyautogui
            pyautogui.write(text, interval=0.01)
            return "Text entered."
        except Exception as exc:
            return f"Computer-control error: {exc}"

    def press(self, key: str) -> str:
        if not self.enabled:
            return "Computer control is disabled."
        try:
            import pyautogui
            pyautogui.press(key)
            return f"Pressed {key}."
        except Exception as exc:
            return f"Computer-control error: {exc}"
