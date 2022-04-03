from dataclasses import dataclass


@dataclass
class Character:
    name: str
    hp: int
    level: int = 1

    def print(self):
        return f'Name: {self.name}\nLevel: {self.level}\nHP: {self.hp}'
