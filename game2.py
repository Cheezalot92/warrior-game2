class Warrior:
    def __init__(self, characterName, health=60, power=10):
        self.characterName = characterName
        self.health = health
        self.power = power


class Hero(Warrior):
    def __init__(self, characterName, characterType, health=60, power=15):
        super().__init__(characterName, health, power)
        self.characterType = characterType

    def greet(self, otherCharacter):
        print(f"Hey my name is {self.characterName} and I'm a Z fighter!")

    def announce(self, otherFighter):
        print(f"Stop the games {otherFighter.characterName}, you can't win!")

    def kamehameha(self, hitCell):
        hit = self.power
        hitCell.health -= 10
        print(hitCell.health)

    def spiritBomb(self, hitCell):
        hit = self.power
        hitCell.health -= 20
        print(hitCell.health)


class Villain(Warrior):
    def __init__(self, characterName, characterType, health=50, power=10):
        super().__init__(characterName, health, power)
        self.characterType = characterType

    def greetAgain(self, otherFighter):
        print(f"Yeah, I know who you are {self.characterName}. I know who you are. I know everything about you. I'm {otherFighter.characterName} part of me, came from you. I am the ultimate being and I will take over the universe.")

    def specialBeamCannon(self, fireGoku):
        fire = self.power
        fireGoku.health -= 5
        print(fireGoku.health)

    def taunt(self, otherCharacter, taunt=False):
        if not taunt:
            print(f"HaHa {otherCharacter.characterName}, you and your puny bunch of Z Fighters could never hope to defeat me 😂")
        else:
            print(f"You think that's enough to defeat me? {otherCharacter.characterName}, you better bring the heat or your friends are DEAD!")


class ZombieMinion(Warrior):
    def __init__(self, characterName, characterType, health=float('inf'), power=10):
        super().__init__(characterName, health, power)
        self.characterType = characterType


Goku = Hero('Goku', 'Sayian', 60, 10)
Cell = Villain('Cell', 'Android', 50, 10)
Minion1 = ZombieMinion('MiniCell1', 'null', 3)

Goku.greet(Cell)
Cell.greetAgain(Goku)
Goku.kamehameha(Cell)
Cell.specialBeamCannon(Goku)
Goku.announce(Cell)
Cell.taunt(Goku, True)
Goku.kamehameha(Cell)
Cell.taunt(Goku, True)