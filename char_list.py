import random
from char import char

class Warrior(char):
    
    # Redefine attack method in child to enable critical hit option of Warrior class
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

    # Redefine defense method in child to enable heal option of Medic class (no evade as a result)
    def defense(self, damage):
        self.health -= damage
        # Medic's chance to heal
        chance = random.randint(1,20)
        if self.health > 0 and chance > 15:
            print('Cleric healed!')
            self.health += 2

class Shadow(char):

    # Redefine defense method in child to enable evade chance option of Shadow class (no evade from char parent class as a result)
    def defense(self, damage):
        #Shadow can only be hit 1/10 times
        chance = random.randint(1,20)
        if chance < 3:
            self.health -= damage

class Wizard(char):

    # Wizard has a mana abilty that limits fighting to mana until rested, when mana regens (not yet implemented)
    def __init__(self, health, power):
        self.mana = 5
        super(Wizard, self).__init__(health, power)

class Elf(char):
    
    # Elf has an arrows atribute that limits fighting to max arrow capacity until refill when rested (not yet implemented)
    def __init__(self, health, power):
        self.arrows = 10
        super(Elf, self).__init__(health, power)

