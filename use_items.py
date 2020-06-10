def use_items(char):
    while len(char.items) > 0:
        print('Use item:')
        for n in char.items:
            print(n)
        print('None')
        use = input('> ')

        if use == "Sword":
            char.power += 2
            char.items.remove(use)
        
        if use == "Tonic":
            char.health += 10
            char.items.remove(use)
        
        if use == "Armor":
            char.armor += 2
            char.items.remove(use)

        if use == "Boots":
            char.evade -= 2
            if char.evade < 10:
                char.evade = 10
                print('Evade cannot be increased further!\n')
            else:
                char.items.remove(use)

        if use == "None":
            return

    print('You have no items to use!')
