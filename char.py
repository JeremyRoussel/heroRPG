import random

class char():
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.wallet = 0
        self.armor = 0
        self.evade = 20
        self.items = []
 
    def attack(self, opponent):
        opponent.defense(self.power)

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def status(self):
        print(f'The {self.__class__.__name__} has {self.health} health and {self.power} power.')

    def defense(self, damage):
        evade_chance = random.randint(1,20)
        if evade_chance < self.evade:
            if damage - self.armor < 0:
                fd = 0
            else:
                fd = damage - self.armor
            self.health -= fd
            print(f'The {self.__class__.__name__} took {fd} damage')
        else:
            print('Damage Evaded!')