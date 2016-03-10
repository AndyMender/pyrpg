def levelUp(player_atts):
    '''Evaluates player experience point gain and increases player level. 
Also, allows the player to increase any attribute by 1 point, up to 5 times.
''' 
    exp_caps = {500: 2, 1000: 3, 2000: 4, 3000: 5, 4500: 6, 
                             6000: 7, 8000: 8, 10000: 9, 13000: 10}
    
    # Assigning player current level to variable:
    prior_level = player_atts['Level']
    
    # Adjusting player level in respect to gained experience points:
    for cap in sorted(exp_caps.keys()):
        if player_atts['Experience'] >= cap:
            player_atts['Level'] = exp_caps[cap]
        else:
            break

    # Check - has the player gained a level?
    if player_atts['Level'] > prior_level:
        print('''Congratulations! You have gained an experience level!
You now have 3 attribute points at your disposal. Distribute them wisely...''')
        att_points = 3
        
        # Spending attribute points:
        while att_points > 0:
            print('Which attribute would you like to increase?')
            player_atts[input('')] += 1
            att_points -= 1
            player_atts['Hitpoints'] = player_atts['Fortitude'] * 2
            player_atts['Mana'] = player_atts['Wisdom'] * 2
            print('Your current attributes look as follows:')
            for key, value in sorted(player_atts.items()):
                print('%s: %s' % (key, value))
            continue

        return player_atts

def gameover():
    '''Triggered when player makes a 'bad choice' or dies.
    '''
    print('''
Thus, ends your journey...
Many treasures still await. Perhaps another time?''')
    quit()