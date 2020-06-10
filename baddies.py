import random
from char import char

# Enemy list, all have a bounty value
# could make enemy class with bounty in initialization to reduce duplication

class Goblin(char):
    def __init__(self, health, power):
        self.bounty = 5
        super(Goblin, self).__init__(health, power)
    pass

class Zombie(char):
    def __init__(self, health, power):
        self.bounty = 10
        super(Zombie, self).__init__(health, power)

    # Zombie cannot die, alive method is redefined in this child class to always return True
    def alive(self):
        return True

class Slime(char):
    def __init__(self, health, power):
        self.bounty = 8
        super(Slime, self).__init__(health, power)

class Skeleton(char):
    def __init__(self, health, power):
        self.bounty = 7
        super(Skeleton, self).__init__(health, power)