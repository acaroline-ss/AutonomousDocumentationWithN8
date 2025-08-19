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
            print(f"📂 Repositório já existe em {self.dest}")
            return
        Path(self.dest).mkdir(exist_ok=True)
        Path(self.dest, "README.md").write_text(
            f"# Clonado de {self.repo_url} (branch {self.branch})", encoding="utf-8"
        )
        print(f"✅ Repositório clonado em {self.dest}")

    def pull(self):
        if not os.path.exists(self.dest):
            print(f"❌ {self.dest} não existe para atualizar.")
            return
        with open(Path(self.dest, "README.md"), "a", encoding="utf-8") as f:
            f.write("\nAtualizado remotamente (simulado).")
        print(f"🔄 Repositório {self.dest} atualizado (simulado).")
