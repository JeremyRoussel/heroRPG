#!/usr/bin/env python3

# Dependencies and imports
import random
from char import char
from char_list import *
from baddies import Goblin
from shop import shop
from cave import cave
from use_items import *
import time

# Hero selection!
heros = {'1':1, '2':2, '3':3, '4':4, '5':5, '10':10}
hero_choice = '0'
while hero_choice not in heros:
    print('\nYou awake in a tavern and look upon yourself in the mirror. What do you see?')
    time.sleep(.3)
    print('*************************************')
    time.sleep(.3)
    print('* 1. Warrior      ____              *')
    time.sleep(.3)
    print('* 2. Wizard      /\  .\    _____    *')
    time.sleep(.3)
    print('* 3. Elf        /: \___\  / .  /\   *')
    time.sleep(.3)
    print("* 4. Medic      \ '/.. / /____/..\  *")
    time.sleep(.3)
    print("* 5. Shadow      \/___/  \ '' \ '/  *")
    time.sleep(.3)
    print("*                         \_''_\/   *")
    time.sleep(.3)
    print("*************************************")
    time.sleep(.3)
    hero_choice = input('> ')

# Default values, future difficulty adjustments?
h_in = 10
p_in = 5

# Instantiate hero choice
if hero_choice == '1':
    hero = Warrior(h_in,p_in)
if hero_choice == '2':
    hero = Wizard(h_in - 3, p_in + 3)
if hero_choice == '3':
    hero = Elf(h_in + 3, p_in - 1)
if hero_choice == '4':
    hero = Medic(h_in + 6, p_in - 3)
if hero_choice == '5':
    hero = Shadow(1 , p_in - 2)
if hero_choice == '10':
    hero = Goblin(h_in, p_in - 2)

# Main Function Definition
def main():

    # Wat do?
    while True:
        time.sleep(.3)
        print()
        print('**********************************')
        time.sleep(.3)
        print('* What do you want to do?        *')
        time.sleep(.3)
        print('* 1. Talk to Tavern Barkeep      *')
        time.sleep(.3)
        print('* 2. Shop                        *')
        time.sleep(.3)
        print('* 3. Explore Cave                *')
        time.sleep(.3)
        print('* 4. Use Items                   *')
        time.sleep(.3)
        print('* 5. Quit                        *')
        time.sleep(.3)
        print('**********************************')
        direction = input('> ')

        # Game info
        if direction == '1':
            time.sleep(.3)
            print('\nWelcome visitor! Here you can use items, go shopping, take a rest, or go explore the abandoned cave outside of town!\n')
            time.sleep(1)
            print('''Have a drink on the house!

    _.._..,_,_
   (          )
    ]~,"-.-~~[
  .=])' (;  ([
  | ]:: '    [
  .=]): .)  ([
    |:: '    |
     ~~----~~
     ''')
            time.sleep(1)

        # Go shopping
        if direction == '2':
            time.sleep(.3)
            shop(hero)
        
        # Go fighting
        if direction == '3':
            time.sleep(.3)
            cave(hero)
        
        # Use items
        if direction == '4':
            time.sleep(.3)
            use_items(hero)
        
        # Leave (sad face)
        if direction == '5':
            break


    pass

# Run the thing
main()
