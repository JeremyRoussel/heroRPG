import random
import time

# Main character class defintion and functions

class char():
    def __init__(self, health, power):
        # Attributes
        self.health = health
        self.power = power
        self.wallet = 0
        self.armor = 0
        self.evade = 20
        self.items = []
    
    # Attack method
    def attack(self, opponent):
        opponent.defense(self.power)

    # Alive method
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    # Status method to display attributes
    def status(self):
        time.sleep(.4)
        print(f'The {self.__class__.__name__} has {self.health} health, {self.power} power, {self.wallet} coins, {self.armor} armor, {20 - self.evade} evade points and {self.items} items.')

    # Defense method to determine how damage applies
    # Should probably make a higher order evade function that is called first to prevent having to add evade to subclasses that redefine defense
    def defense(self, damage):
        # Evade chance definition
        # Evade is easier as evade points decrease, max of 10 points
        evade_chance = random.randint(1,20)
        # Damage calculation with armor reduction, with a minimum of zero to prevent damage healing
        if evade_chance < self.evade:
            if damage - self.armor < 0:
                fd = 0
            else:
                fd = damage - self.armor
            self.health -= fd
            time.sleep(.4)
            print(f'The {self.__class__.__name__} took {fd} damage')
        else:
            time.sleep(.4)
            print('Damage Evaded!')