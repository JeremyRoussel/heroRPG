# Use items function, takes character as input
import time

def use_items(char):
    # Loop while items available to use
    while len(char.items) > 0:
        time.sleep(.2)
        # Print all available items
        print('\nUse item:')
        for n in char.items:
            time.sleep(.2)
            print(n)
        time.sleep(.2)
        print('None')
        # Ask for item to use
        use = input('> ')

        # Sword improves attack power
        if use == "Sword":
            char.power += 2
            char.items.remove(use)
            print('Attack increased by two!')
            time.sleep(.3)
        
        # Tonic heals (can currently overfill health beyond initial value)
        if use == "Tonic":
            char.health += 10
            char.items.remove(use)
            print('Health increased by ten!')
            time.sleep(.3)

        # Armor attribute for damage reduction
        if use == "Armor":
            char.armor += 2
            char.items.remove(use)
            print('Armor increased by two!')
            time.sleep(.3)

        # Boots improve the evade ability
        if use == "Boots":
            char.evade -= 2
            # Evade limit at 50% evade chance
            if char.evade < 10:
                char.evade = 10
                print('Evade cannot be increased further!\n')
                time.sleep(.5)
            else:
                char.items.remove(use)
                print('Evade increased by two!')
                time.sleep(.3)


        # Exit Item usage routine
        if use == "None":
            return

    print('\nYou have no items to use!')
    time.sleep(.5)
