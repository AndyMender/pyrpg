############################ Core Game Script #################################
###############################################################################
# author: Andy Mender - astralnysledz@gmail.com
# version: 0.1
# license: GPL/BSD

# This game was created to test the object-oriented (OO) capabilities 
# of Python3 and see how efficiently it fares in text-based game design.

# All of the game files are either redistributed with Python3 or provided
# on the GitHub repository: https://github.com/AndyMender/pyrpg
###############################################################################
######################### Library Import Section ##############################
from pyrpg_charstat import pcStatGen, charAttGen
from pyrpg_charclass import NPC, Shopkeeper
from pyrpg_events import gameover, levelUp
###############################################################################
########################### Main Game Section #################################

# First story entry - part of later game journal?
print('''
It is Mondag, Januer 3rd, year 388...
You arrive by boat at a tiny fishing village of Molag Ker. Upon disembarking, 
you are approached by a townsguard and guided to a nearby shanty. Inside, clad 
in dingy robes sits a beared man. He seems extremely old, though his eyes hide 
life and eagerness of a youngster.
''')

# First player choice - showing impact of key game decisions on plot progress:
pc_choice = input('''
Welcome, traveler, Secundus Augustus greets you. You are... *cough!* *cough!* 
the person we have been awaiting, yes? ''')
if pc_choice.lower() in ('no', 'n'):
    print('No? Disappointing...Leave at once, fool!')
    gameover()
del pc_choice       # Removing temporary variable for later reuse
print('Very well, then.')
# Generating and recording initial player details like name, age and birthsign:
player_stats = pcStatGen()

# Generating player attributes based on level (current = 1) and class:
player_atts = charAttGen(player_stats['Occupation'])

while True:
    print('Interesting! These are the details I have written down:')
    for key, value in sorted(player_stats.items()):
        print('%s: %s' % (key, value))
    pc_choice = input('Did I understand everything correctly? [yes/no]')

    if pc_choice.lower() in ('yes', 'y'):
        print('Very well. I will try to *remember* everything.')
        break
    elif pc_choice.lower() in ('no', 'n'):
        print('*sigh* Let us start from the very beginning.\n')
        player_stats = pcStatGen()
        player_atts = charAttGen(player_stats['Occupation'])
        continue

# Level-up test:
player_atts = levelUp(player_atts)

print('You can go now. I hope you like our village...*cough* *cough*.Hehe...')