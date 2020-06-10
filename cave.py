import random
from char import char
from char_list import Zombie, Goblin

def cave(hero):

    enemy_selector = random.randint(1,20)

    if enemy_selector == 20:
        enemy = Zombie(-1, 1)
    else:
        enemy = Goblin(6, 2)


    while enemy.alive() and hero.alive():
        print()
        hero.status()
        enemy.status()
        print("\nWhat do you want to do?")
        print(f"1. Fight {enemy.__class__.__name__}")
        print("2. Do nothing")
        print("3. Flee")
        print("> ", end=' ')
        raw_input = input()

        if raw_input == "1":
            hero.attack(enemy)

        elif raw_input == "2":
            pass

        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if enemy.health > 0:
            enemy.attack(hero)

        if hero.health <= 0:
            print("You are dead.")
        if enemy.health <= 0:
            print("The enemy is dead.")

    hero.wallet += enemy.bounty