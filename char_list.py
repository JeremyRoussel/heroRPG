import random
from char import char

class Goblin(char):
    def __init__(self, health, power):
        self.bounty = 5
        super(Goblin, self).__init__(health, power)
    pass

class Zombie(char):
    def __init__(self, health, power):
        self.bounty = 10
        super(Zombie, self).__init__(health, power)

    def alive(self):
        return True

class Warrior(char):
    def attack(self, opponent):
        
        if random.randint(1,20) > 15:
            damage = self.power*2
            print('Critical Hit!')
        else:
            damage = self.power
        
        opponent.health -= damage
        print(f'The {self.__class__.__name__} deals {damage} damage to the {opponent.__class__.__name__}.')
    pass

class Medic(char):

    def defense(self, damage):
        self.health -= damage
        # Medic's chance to heal
        chance = random.randint(1,20)
        if self.health > 0 and chance > 15:
            print('Cleric healed!')
            self.health += 2

class Shadow(char):

    def defense(self, damage):
        #Shadow can only be hit 1/10 times
        chance = random.randint(1,20)
        if chance < 3:
            self.health -= damage

class Wizard(char):
    def __init__(self, health, power):
        self.mana = 5
        super(Wizard, self).__init__(health, power)

class Elf(char):
    def __init__(self, health, power):
        self.arrows = 10
        super(Elf, self).__init__(health, power)

