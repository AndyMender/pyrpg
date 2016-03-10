def pcStatGen():
    '''Generates player details, like name, age, occupation, etc. This data is
stored in a save file afterwards.
'''
    player_stats = {'Name': '', 'Age': '', 'Birthsign': '', 'Occupation': ''}
    
    player_name = input('What is your name, traveler? ')
    player_stats['Name'] = player_name

    player_age = int(input('What is your age? '))
    player_stats['Age'] = player_age
    # Later role for player age - conversation remarks, quests, etc.?
    
    player_sign = input('Many people claim a birthsign. What is yours? ')
    player_stats['Birthsign'] = player_sign

    player_class = input('What is your occupation? ')
    player_stats['Occupation'] = player_class
    
    return player_stats
    
    
def charAttGen(char_class, level=1):
    '''Generates character attribute values based on character class 
and experience level.
Also used to generate NPC and monster attribute values.
Race dependency will be added at a later stage.
'''
    from random import choice
    
    # Empty default values as templates for attribute calculation:
    attributes = {'Strength': 0, 'Dexterity': 0, 'Fortitude': 0, 'Wisdom': 0, 
                  'Intelligence': 0, 'Hitpoints': 0, 'Mana': 0, 'Level': 1, 
                  'Experience': 0}

    # Attributes added based on character class. If list expands, move data to
    # a separate text file or module for storage:
    if char_class.lower() == 'warrior':
        attributes['Strength'] = 40
        attributes['Dexterity'] = 30
        attributes['Fortitude'] = 40
        attributes['Wisdom'] = 15
        attributes['Intelligence'] = 15
    elif char_class.lower() == 'rogue':
        attributes['Strength'] = 20
        attributes['Dexterity'] = 50
        attributes['Fortitude'] = 30
        attributes['Wisdom'] = 20
        attributes['Intelligence'] = 20
    elif char_class.lower() == 'mage':
        attributes['Strength'] = 20
        attributes['Dexterity'] = 20
        attributes['Fortitude'] = 30
        attributes['Wisdom'] = 35
        attributes['Intelligence'] = 35
    else:
        # Undefined character class attribute distribution:
        attributes['Strength'] = 30
        attributes['Dexterity'] = 25
        attributes['Fortitude'] = 30
        attributes['Wisdom'] = 30
        attributes['Intelligence'] = 25

    # Hitpoint and Mana calculation post attribute assignment:
    attributes['Hitpoints'] = attributes['Fortitude'] * 2
    attributes['Mana'] = attributes['Wisdom'] * 2
    
    # Applying 3 attribute points per level at random to generate NPC attributes:
    for i in range(0, (level-1) * 3):
        attributes[choice(list(attributes.keys()))] += 1

    return attributes