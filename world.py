from dataclasses import dataclass, field

@dataclass
class Room:
    name: str
    description: str
    items: list = field(default_factory=list)
    exits: dict = field(default_factory=dict)
    def remove_item(self, item: str) -> bool:
        if item in self.items:
            self.items.remove(item)
            return True
        return False

def build_world():
    hall = Room("Saguão", "Um saguão silencioso com um cartaz luminoso ao fundo.", ["bilhete"], {"norte":"Biblioteca","leste":"Atelier"})
    biblioteca = Room("Biblioteca", "Prateleiras altas e um leve cheiro de poeira.", ["chave"], {"sul":"Saguão","leste":"Laboratório"})
    atelier = Room("Atelier", "Telas, cores e um baú trancado.", [], {"oeste":"Saguão","norte":"Laboratório"})
    lab = Room("Laboratório", "Bancadas metálicas. Um painel com uma fechadura.", [], {"oeste":"Biblioteca","sul":"Atelier"})
    rooms = {"Saguão":hall,"Biblioteca":biblioteca,"Atelier":atelier,"Laboratório":lab}
    return hall, rooms
