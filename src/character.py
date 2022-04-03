from dataclasses import dataclass


@dataclass
class Character:
    name: str
    hp: int
    level: int = 1

    def to_string(self):
        return f'*Name:*  {self.name}\n*Level:*  {self.level}\n*HP:*  {self.hp}'
