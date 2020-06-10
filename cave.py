import random
from char import char
from baddies import *
from use_items import *

def cave(hero):

    enemy_selector = random.randint(1,20)

    if enemy_selector > 18:
        enemy = Zombie(-1, 1)
    elif enemy_selector > 12:
        enemy = Goblin(6, 2)
    elif enemy_selector > 6:
        enemy = Slime(12, 1)
    else:
        enemy = Skeleton(8, 3)

    print(f'\nYou encounter a {enemy.__class__.__name__}!')


    while enemy.alive() and hero.alive():
        print()
        hero.status()
        enemy.status()
        print("\nWhat do you want to do?")
        print(f"1. Fight {enemy.__class__.__name__}")
        print("2. Use Item")
        print("3. Do nothing")
        print("4. Flee")
        print("> ", end=' ')
        raw_input = input()

        if raw_input == "1":
            hero.attack(enemy)

        elif raw_input == "2":
            use_items(hero)

        elif raw_input == "3":
            pass

        elif raw_input == "4":
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