from pathlib import Path
import webbrowser

class ToolBox:
    def __init__(self,browser_enabled=False,computer_enabled=False):
        self.browser_enabled=browser_enabled; self.computer_enabled=computer_enabled
    def open_url(self,url):
        if not self.browser_enabled:return 'Browser control is disabled.'
        if not url.startswith(('http://','https://')):return 'Only http(s) URLs are allowed.'
        webbrowser.open(url); return f'Opened {url}'
    def list_files(self,folder):
        p=Path(folder).expanduser().resolve()
        if not p.is_dir():return f'Folder not found: {p}'
        return '\n'.join(('DIR  ' if x.is_dir() else 'FILE ')+x.name for x in list(p.iterdir())[:200]) or '(empty)'
