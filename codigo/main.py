import os
import sys
sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")

from cli_interface import ask_choice, ask_input, confirm, banner
from repo_handler import RepoHandler
from file_utils import list_python_files, save_to_file, summarize_directory
from async_tasks import run_fake_downloads

def main():
    banner()
    options = {
        "1": "Clonar repositório (simulado)",
        "2": "Atualizar repositório existente (simulado)",
        "3": "Listar arquivos Python",
        "4": "Baixar arquivos externos (simulado, async)",
        "5": "Resumo da pasta",
        "6": "Sair"
    }

    while True:
        choice = ask_choice(options)
        if choice == "1":
            repo_url = ask_input("📎 Digite o link do repositório GitHub:")
            branch = ask_input("🌿 Nome da branch (default: main):", "main")
            repo = RepoHandler(repo_url, branch)
            repo.clone()
        elif choice == "2":
            repo_name = ask_input("📂 Nome da pasta do repositório local:")
            repo = RepoHandler("fake_url", "main", repo_name)
            repo.pull()
        elif choice == "3":
            path = ask_input("📂 Pasta para listar arquivos:", os.getcwd())
            py_files = list_python_files(path)
            print("\nArquivos encontrados:")
            for f in py_files:
                print(" -", f)
            if confirm("Deseja salvar em um arquivo?"):
                save_to_file("python_files.txt", "\n".join(py_files))
                print("✅ Arquivo salvo em python_files.txt")
        elif choice == "4":
            urls = []
            while True:
                u = ask_input("Digite a URL (ENTER para terminar):")
                if not u:
                    break
                urls.append(u)
            if urls:
                results = run_fake_downloads(urls)
                print("✅ Downloads concluídos:", results)
        elif choice == "5":
            path = ask_input("📂 Pasta para resumir:", os.getcwd())
            summary = summarize_directory(path)
            print("\nResumo da pasta:")
            for k, v in summary.items():
                print(f" - {k}: {v}")
        elif choice == "6":
            print("👋 Encerrando programa.")
            break
        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    main()
