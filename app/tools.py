from pathlib import Path
import webbrowser

class ToolBox:
    def __init__(self,browser_enabled=False,computer_enabled=False): self.browser_enabled=browser_enabled; self.computer_enabled=computer_enabled
    def open_url(self,url):
        if not self.browser_enabled:return 'Browser control is disabled.'
        if not url.startswith(('http://','https://')):return 'Only http(s) URLs are allowed.'
        webbrowser.open(url); return f'Opened {url}'
    def list_files(self,folder):
        p=Path(folder).expanduser().resolve()
        if not p.is_dir():return f'Folder not found: {p}'
        return '\n'.join(('DIR  ' if x.is_dir() else 'FILE ')+x.name for x in list(p.iterdir())[:200]) or '(empty)'
    def create_folder(self,folder):
        p=Path(folder).expanduser(); p.mkdir(parents=True,exist_ok=True); return f'Created folder: {p.resolve()}'
    def delete_path(self,path):
        p=Path(path).expanduser()
        if not p.exists():return f'Not found: {p}'
        if p.is_dir():p.rmdir()
        else:p.unlink()
        return f'Deleted: {p.resolve()}'
    def computer_press(self,key):
        if not self.computer_enabled:return 'Computer control is disabled.'
        try:
            import pyautogui; pyautogui.press(key); return f'Pressed {key}.'
        except Exception as e:return f'Computer-control error: {e}'
