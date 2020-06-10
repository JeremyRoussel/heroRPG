import random
from char import char

class Hero(char):
    def attack(self, opponent):
        
        if random.randint(1,20) > 15:
            damage = self.power*2
            print('Critical Hit!')
        else:
            damage = self.power
        
        opponent.health -= damage
        print(f'The {self.__class__.__name__} deals {damage} damage to the {opponent.__class__.__name__}.')
    pass