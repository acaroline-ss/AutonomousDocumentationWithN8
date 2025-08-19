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
        "1": "Clone repository (simulated)",
        "2": "Update existing repository (simulated)",
        "3": "List Python files",
        "4": "Download external files (simulated, async)",
        "5": "Folder summary",
        "6": "Exit"
    }

    while True:
        choice = ask_choice(options)
        if choice == "1":
            repo_url = ask_input("📎 Enter the GitHub repository link:")
            branch = ask_input("🌿 Branch name (default: main):", "main")
            repo = RepoHandler(repo_url, branch)
            repo.clone()
        elif choice == "2":
            repo_name = ask_input("📂 Name of the local repository folder:")
            repo = RepoHandler("fake_url", "main", repo_name)
            repo.pull()
        elif choice == "3":
            path = ask_input("📂 Folder to list files:", os.getcwd())
            py_files = list_python_files(path)
            print("\nFiles found:")
            for f in py_files:
                print(" -", f)
            if confirm("Do you want to save to a file?"):
                save_to_file("python_files.txt", "\n".join(py_files))
                print("✅ File saved to python_files.txt")
        elif choice == "4":
            urls = []
            while True:
                u = ask_input("Enter URL (press ENTER to finish):")
                if not u:
                    break
                urls.append(u)
            if urls:
                results = run_fake_downloads(urls)
                print("✅ Downloads completed:", results)
        elif choice == "5":
            path = ask_input("📂 Folder to summarize:", os.getcwd())
            summary = summarize_directory(path)
            print("\nFolder summary:")
            for k, v in summary.items():
                print(f" - {k}: {v}")
        elif choice == "6":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
