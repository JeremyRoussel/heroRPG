def shop(char):
    
    item_list = {"Sword":[1, 10], "Tonic":[1, 5], "Armor":[1,8], "Boots":[1,2]}

    # try:
    #     item_list
    # except:
    #     item_list = {"Sword":[1, 10], "Tonic":[1, 5]}
    # finally:
    #     pass

    selection = "0"
    while True:
        print(f'You have {char.wallet} coins. What would you like to buy?')

        for key in item_list:
            print(f'{key} ({item_list[key][1]} coins)')
        print(f'Nothing')
        selection = input('> ')

        try:
            if char.wallet >= item_list[selection][1]:
                    
                item_list[selection][0] -= 1
                char.wallet -= item_list[selection][1]
                char.items.append(selection)
                if item_list[selection][0] == 0:
                    del item_list[selection]
            else:
                print('Not enough money!')
        except:
            pass
        finally:
            pass

        if selection.lower() == 'nothing':
            break