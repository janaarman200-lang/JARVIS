from pathlib import Path

class FileManager:
    def list_files(self, folder: str) -> list[str]:
        return [str(p) for p in Path(folder).iterdir()]

    def create_folder(self, folder: str) -> str:
        Path(folder).mkdir(parents=True, exist_ok=True)
        return f"Created folder: {folder}"

    def delete(self, path: str) -> str:
        # Deletion must be gated by the approval layer before this method is called.
        target = Path(path)
        if target.is_dir():
            target.rmdir()
        else:
            target.unlink()
        return f"Deleted: {path}"
