import random
from char import char
from baddies import *
from use_items import *
import time

def cave(hero):

    cont = True
    while cont == True:

        # Select a random enemy to fight in the cave

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

        # Main fighting loop

        while enemy.alive() and hero.alive():
            print()
            time.sleep(.3)
            hero.status()
            time.sleep(.3)
            enemy.status()
            time.sleep(.3)
            print('*********************************************************************')
            time.sleep(.3)
            print('*    What do you want to do?                                        *')
            time.sleep(.3)
            print('* 1. Fight                        />                                *')
            time.sleep(.3)
            print('* 2. Use Item            (       /---------------------------\      *')
            time.sleep(.3)
            print('* 3. Do nothing         (*)OXOXO(*>    -------                \     *')
            time.sleep(.3)
            print('* 4. Flee                (       \-----------------------------\    *')
            time.sleep(.3)
            print('*                                 \>                                *')
            time.sleep(.3)
            print('*********************************************************************')
            print('>', end=' ')
            raw_input = input()

            if raw_input == "1":
                # Call on attack method for hero against enemy
                time.sleep(.3)
                hero.attack(enemy)

            elif raw_input == "2":
                # Open items usage menu
                use_items(hero)

            elif raw_input == "3":
                # Wait!
                pass

            elif raw_input == "4":
                # Run!
                time.sleep(.3)
                print("You run away scared!")
                break
            else:
                # Error handling
                print(f"Invalid input {raw_input}")

            
            # Does enemy attack back?
            if enemy.alive():
                # Call attack method for enemy against hero
                time.sleep(.3)
                enemy.attack(hero)

            # Are you dead?

            if hero.health <= 0:
                # Permadeath
                time.sleep(.3)
                print("You are dead.")
            if enemy.health <= 0:
                #Enemy death and victory?
                time.sleep(.3)
                if enemy.__class__.__name__ == 'Zombie':
                    print("\nThe enemy is still dead? Why are you still here!")
                else:
                    print("\nThe enemy is dead.")

        # Add bounty to wallet attribute
        hero.wallet += enemy.bounty
        time.sleep(.3)
        print('\nContinue exploring cave? (Yes/No)')
        
        cont_test = input('>  ')
        if cont_test.lower() == 'no':
            cont = False
