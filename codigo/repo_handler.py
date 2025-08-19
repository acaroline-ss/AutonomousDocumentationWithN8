import os
from urllib.parse import urlparse
from pathlib import Path

class RepoHandler:
    def __init__(self, repo_url: str, branch: str = "main", dest: str = None):
        self.repo_url = repo_url
        self.branch = branch
        self.dest = dest or self.get_repo_name(repo_url)

    @staticmethod
    def get_repo_name(repo_url: str) -> str:
        path = urlparse(repo_url).path
        return os.path.basename(path).replace(".git", "") or "repo_demo"

    def clone(self):
        if os.path.exists(self.dest):
            print(f"📂 Repository already exists at {self.dest}")
            return
        Path(self.dest).mkdir(exist_ok=True)
        Path(self.dest, "README.md").write_text(
            f"# Cloned from {self.repo_url} (branch {self.branch})", encoding="utf-8"
        )
        print(f"✅ Repository cloned at {self.dest}")

    def pull(self):
        if not os.path.exists(self.dest):
            print(f"❌ {self.dest} does not exist to update.")
            return
        with open(Path(self.dest, "README.md"), "a", encoding="utf-8") as f:
            f.write("\nUpdated remotely (simulated).")
        print(f"🔄 Repository {self.dest} updated (simulated).")
