import argparse
from engine import GameEngine

def play_script(engine, commands):
    for c in commands:
        out = engine.handle(c)
        print(f">> {c}")
        print(out)
        if "venceu" in out or out == "sair":
            break

def interactive_loop():
    eng = GameEngine()
    print(eng.look())
    while True:
        try:
            cmd = input(">> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAté logo!")
            return
        out = eng.handle(cmd)
        if out == "sair":
            print("Até logo!")
            return
        print(out)

def demo_script():
    return [
        "olhar",
        "pegar bilhete",
        "ir norte",
        "pegar chave",
        "ir leste",
        "usar painel",
        "ir sul",
        "ir oeste",
        "ir leste",
        "usar baú",
        "inventario",
        "ir norte",
        "usar painel",
        "sair",
    ]

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--script", action="store_true")
    args = p.parse_args()
    if args.script:
        play_script(GameEngine(), demo_script())
    else:
        interactive_loop()
