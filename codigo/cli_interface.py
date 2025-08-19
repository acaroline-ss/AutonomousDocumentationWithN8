def ask_choice(options: dict):
    print("\n📌 Choose an option:\n")
    for key, label in options.items():
        print(f"  {key} - {label}")
    choice = input("\n➡️  Enter your choice: ").strip()
    return choice if choice in options else None

def ask_input(prompt: str, default=None):
    value = input(f"{prompt} ").strip()
    return value or default

def confirm(prompt: str) -> bool:
    ans = input(f"{prompt} (y/n): ").strip().lower()
    return ans == "y"

def banner():
    print("=" * 40)
    print("   🐍 AUTODOC DEMO - CLI INTERFACE   ")
    print("=" * 40)

def help_menu():
    print("\nHelp:\n")
    print("1 - Clone a remote repository (simulated)")
    print("2 - Update an existing repository")
    print("3 - List Python files in a folder")
    print("4 - Download external files (simulated)")
    print("5 - Folder summary")
    print("6 - Exit program\n")

if __name__ == "__main__":
    banner()
    help_menu()
