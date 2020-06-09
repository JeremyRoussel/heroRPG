#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class char():
    def __init__(self, health, power):
        self.health = health
        self.power = power
 
    def attack(self, opponent):
        opponent.health -= self.power

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False


hero = char(10, 5)
goblin = char(6, 2)



def main():

    while goblin.alive() and hero.alive():
        print(f"\nYou have {hero.health} health and {hero.power} power.")
        print(f"The goblin has {goblin.health} health and {goblin.power} power.")
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()

        if raw_input == "1":
            hero.attack(goblin)
            print(f"You do {hero.power} damage to the goblin.")

        elif raw_input == "2":
            pass

        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if goblin.health > 0:
            goblin.attack(hero)
            print(f"The goblin does {goblin.power} damage to you.")

    if hero.health <= 0:
        print("You are dead.")
    if goblin.health <= 0:
        print("The goblin is dead.")

main()
