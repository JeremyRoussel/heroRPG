class char():
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.wallet = 0
        self.armor = 0
        self.items = []
 
    def attack(self, opponent):
        opponent.defense(self.power)
        # print(f'The {self.__class__.__name__} deals {self.power} damage to the {opponent.__class__.__name__}.')

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def status(self):
        print(f'The {self.__class__.__name__} has {self.health} health and {self.power} power.')

    def defense(self, damage):
        self.health -= damage - self.armor