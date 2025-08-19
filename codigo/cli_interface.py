def ask_choice(options: dict):
    print("\n📌 Escolha uma opção:\n")
    for key, label in options.items():
        print(f"  {key} - {label}")
    choice = input("\n➡️  Digite a opção: ").strip()
    return choice if choice in options else None

def ask_input(prompt: str, default=None):
    value = input(f"{prompt} ").strip()
    return value or default

def confirm(prompt: str) -> bool:
    ans = input(f"{prompt} (s/n): ").strip().lower()
    return ans == "s"

def banner():
    print("=" * 40)
    print("   🐍 AUTODOC DEMO - CLI INTERFACE   ")
    print("=" * 40)

def help_menu():
    print("\nAjuda:\n")
    print("1 - Clona um repositório remoto (simulado)")
    print("2 - Atualiza um repositório existente")
    print("3 - Lista arquivos Python de uma pasta")
    print("4 - Baixa arquivos externos simulados")
    print("5 - Resumo da pasta")
    print("6 - Sai do programa\n")

if __name__ == "__main__":
    banner()
    help_menu()
