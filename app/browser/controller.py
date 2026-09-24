from urllib.parse import urlparse

class BrowserController:
    def __init__(self, enabled: bool = False):
        self.enabled = enabled

    def validate_url(self, url: str) -> bool:
        parsed = urlparse(url)
        return parsed.scheme in {"http", "https"} and bool(parsed.netloc)

    def open(self, url: str) -> str:
        if not self.enabled:
            return "Browser control is disabled."
        if not self.validate_url(url):
            return "Invalid URL."
        try:
            import webbrowser
            webbrowser.open(url)
            return f"Opened {url}"
        except Exception as exc:
            return f"Browser error: {exc}"
