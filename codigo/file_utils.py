import os
from pathlib import Path
import hashlib

def ensure_dir(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)
    return path

def list_python_files(directory: str):
    files = []
    for p in Path(directory).rglob("*.py"):
        files.append(str(p.resolve()))
    return files

def file_hash(filepath: str):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def save_to_file(filepath: str, content: str):
    ensure_dir(str(Path(filepath).parent))
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def read_file(filepath: str):
    if not os.path.exists(filepath):
        return ""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def compare_files(file1: str, file2: str) -> bool:
    return file_hash(file1) == file_hash(file2)

def summarize_directory(directory: str):
    summary = {"files": 0, "lines": 0, "chars": 0}
    for p in Path(directory).rglob("*"):
        if p.is_file():
            summary["files"] += 1
            try:
                txt = p.read_text(encoding="utf-8", errors="ignore")
                summary["lines"] += txt.count("\n") + 1
                summary["chars"] += len(txt)
            except Exception:
                continue
    return summary
