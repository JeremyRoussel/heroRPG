def shop(char):
    
    # Future shop improvements: use file load from outside list at start to manage total items available
    # to buy instead of reloading same list at start of shop routine

    item_list = {"Sword":[1, 10], "Tonic":[1, 5], "Armor":[1,8], "Boots":[1,2]}

    # try:
    #     item_list
    # except:
    #     item_list = {"Sword":[1, 10], "Tonic":[1, 5]}
    # finally:
    #     pass

    selection = "0"
    while True:
        # How many coins available?
        print(f'You have {char.wallet} coins. What would you like to buy?')

        # Print available items, then select an item

        for key in item_list:
            print(f'{key} ({item_list[key][1]} coins)')
        print(f'Nothing')
        selection = input('> ')

        # Error handling for item usage algorithm
        try:
            # Purchase only with enough coins
            if char.wallet >= item_list[selection][1]:
                # Item handling
                item_list[selection][0] -= 1
                # Decrement wallet by item cost
                char.wallet -= item_list[selection][1]
                # Append item to character item list
                char.items.append(selection)
                # Delete item from purchase list if quantity is zero
                if item_list[selection][0] == 0:
                    del item_list[selection]
            # Not enough money
            else:
                print('Not enough money!')
        except:
            pass
        finally:
            pass
        
        # End store routine
        if selection.lower() == 'nothing':
            break