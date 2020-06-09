#!/usr/bin/env python3

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class char():
    def __init__(self, health, power):
        self.health = health
        self.power = power
 
    def __repr__(self):
        return "character"

    def attack(self, opponent):
        opponent.health -= self.power
        print(f'The {self.__class__.__name__} deals {self.power} damage to the {opponent.__class__.__name__}.')

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def status(self):
        print(f'The {self.__class__.__name__} has {self.health} health and {self.power} power.')

class Hero(char):
    def __repr__(self):
        return "Hero"
    
class Goblin(char):
    def __repr__(self):
        return "goblin"


hero = Hero(10, 5)
goblin = Goblin(6, 2)



def main():

    while goblin.alive() and hero.alive():
        print()
        hero.status()
        goblin.status()
        print("\nWhat do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()

        if raw_input == "1":
            hero.attack(goblin)

        elif raw_input == "2":
            pass

        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if goblin.health > 0:
            goblin.attack(hero)

    if hero.health <= 0:
        print("You are dead.")
    if goblin.health <= 0:
        print("The goblin is dead.")

main()
