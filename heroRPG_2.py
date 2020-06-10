#!/usr/bin/env python3

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random
from char import char
from char_list import *
from baddies import Goblin
from shop import shop
from cave import cave
from use_items import *


heros = {'1':1, '2':2, '3':3, '4':4, '5':5, '10':10}
hero_choice = '0'
while hero_choice not in heros:
    print('You awake in a tavern and look upon yourself in the mirror. What do you see?')
    hero_choice = input('''
1. Warrior
2. Wizard
3. Elf
4. Medic
5. Shadow
> ''')

h_in = 10
p_in = 5

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

def main():

    while True:
        direction = input('''\nWhat do you want to do?
1. Talk to Tavern Barkeep
2. Shop
3. Explore Cave
4. Use items
5. Sleep
6. Quit
> ''')

        if direction == '1':
            print('\nWelcome visitor! Here you can use items, go shopping, take a rest, or go explore the abandoned cave outside of town!\n')
        
        if direction == '2':
            shop(hero)
        
        if direction == '3':
            cave(hero)
        
        if direction == '4':
            use_items(hero)
        
        if direction == '5':
            pass
        
        if direction == '6':
            break


    pass
    
main()
