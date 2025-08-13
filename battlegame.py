# BATTLESHIP GAME - GROUP PROJECT
# Team Members: Edrick, Jane, Felsal, Kiptoo

# EDRICK'S SECTION - Task 1: Game Setup & Variables
class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

class Dragon:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage

def setup_game_stats():
    
    characters = {
        "wizard": Character("Wizard", 70, 150),
        "elf": Character("Elf", 100, 100),
        "human": Character("Human", 150, 20)
    }
    dragon = Dragon(300, 50)
    return characters, dragon

