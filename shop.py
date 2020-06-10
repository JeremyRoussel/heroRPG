def shop(char):
    
    item_list = {"Sword":[1, 10], "Tonic":[1, 5]}

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
                if selection == 'Sword':
                    char.power += 2
                    print(f'{char.__class__.__name__}\'s power increased by 2')

                if selection == 'Tonic':
                    char.health += 10
                    print(f'{char.__class__.__name__}\'s health increased by 10')
                    
                item_list[selection][0] -= 1
                char.wallet -= item_list[selection][1]
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