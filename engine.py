from world import build_world

class GameEngine:
    def __init__(self):
        self.current, self.rooms = build_world()
        self.inventory = []
        self.unlocked = False

    def handle(self, raw: str) -> str:
        text = raw.strip()
        if not text:
            return "Use 'ajuda'."
        parts = text.split()
        cmd, arg = parts[0], " ".join(parts[1:]).strip()
        if cmd == "olhar":
            return self.look()
        if cmd == "ir":
            return self.go(arg)
        if cmd == "pegar":
            return self.take(arg)
        if cmd == "usar":
            return self.use(arg)
        if cmd == "inventario":
            return self.inventory_list()
        if cmd == "ajuda":
            return self.help_text()
        if cmd == "sair":
            return "sair"
        return "Comando desconhecido."

    def look(self) -> str:
        r = self.current
        lines = [r.name, r.description]
        if r.items:
            lines.append("Itens: " + ", ".join(r.items))
        if r.exits:
            lines.append("Saídas: " + ", ".join(f"{d}->{n}" for d, n in r.exits.items()))
        if r.name == "Laboratório":
            lines.append("Painel: " + ("desbloqueado" if self.unlocked else "trancado"))
        return "\n".join(lines)

    def go(self, direction: str) -> str:
        if not direction:
            return "Diga: ir <direção>."
        dest_name = self.current.exits.get(direction)
        if not dest_name:
            return "Sem saída nessa direção."
        self.current = self.rooms[dest_name]
        return self.look()

    def take(self, item: str) -> str:
        if not item:
            return "Diga: pegar <item>."
        if self.current.remove_item(item):
            self.inventory.append(item)
            return f"Você pegou {item}."
        return "Não encontrei esse item aqui."

    def use(self, target: str) -> str:
        if not target:
            return "Diga: usar <algo>."
        if target == "baú" and self.current.name == "Atelier":
            if "chave" in self.inventory:
                if "amuleto" in self.inventory:
                    return "O baú está vazio."
                self.inventory.append("amuleto")
                return "Você abriu o baú e encontrou um amuleto."
            return "O baú está trancado."
        if target == "painel" and self.current.name == "Laboratório":
            if "amuleto" in self.inventory and not self.unlocked:
                self.unlocked = True
                return "O painel reconheceu o amuleto. Sistema desbloqueado. Você venceu!"
            return "Nada acontece."
        return "Não sei como usar isso agora."

    def inventory_list(self) -> str:
        return "Inventário vazio." if not self.inventory else "Inventário: " + ", ".join(self.inventory)

    def help_text(self) -> str:
        return "Comandos: olhar | ir <direção> | pegar <item> | usar <alvo> | inventario | ajuda | sair"
