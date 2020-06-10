# Use items function, takes character as input

def use_items(char):
    # Loop while items available to use
    while len(char.items) > 0:
        # Print all available items
        print('Use item:')
        for n in char.items:
            print(n)
        print('None')
        # Ask for item to use
        use = input('> ')

        # Sword improves attack power
        if use == "Sword":
            char.power += 2
            char.items.remove(use)
        
        # Tonic heals (can currently overfill health beyond initial value)
        if use == "Tonic":
            char.health += 10
            char.items.remove(use)
        
        # Armor attribute for damage reduction
        if use == "Armor":
            char.armor += 2
            char.items.remove(use)

        # Boots improve the evade ability
        if use == "Boots":
            char.evade -= 2
            # Evade limit at 50% evade chance
            if char.evade < 10:
                char.evade = 10
                print('Evade cannot be increased further!\n')
            else:
                char.items.remove(use)

        # Exit Item usage routine
        if use == "None":
            return

    print('You have no items to use!')
