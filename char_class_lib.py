class NPC():
    '''NPC parent class. Contains information on NPC name and cell coordinates,
generated during initial game setup. To be inherited by specialized NPC classes.'''
    npc_occupation = None
    # NPC parent class has no occupation. Variable exists as a filler.
    
    def __init__(self, npc_name, cell_location):
        '''Names and places NPC in a game world cell.'''
        self.name = npc_name
        self.cell = cell_location
    
    def greet(self):
        '''Basic greetings. May/will be updated in child classes to align 
with the lore of an NPC.'''
        print('Greetings, wanderer!\nHow may I help you?')
    
    def conversation(self):
        '''Basic set of conversation options. NPC type specific options will be
added in the future.'''
        pc_choice = input(
'''News
Gossip
Occupation
Leave
''')
        if pc_choice in ('News', 'news'):
            print('Nothing interesting recently.')
            # Stub. Will be expanded properly with game event triggers later.
        elif pc_choice in ('Gossip', 'gossip'):
            print('Did you know that the queen was found running around naked in the townsquare?!')
            # Random gossip responses generated from a gossip list. To be added later.
        elif pc_choice in ('Occupation', 'occupation'):
            if self.npc_occupation == None:
                print('My name is %s and I come from %s.\n' % (self.name, self.cell),
                      'Alas, I have no job and nothing to do...')
        elif pc_choice in ('Leave', 'leave'):
            self.farewell()
        else:
            print('I beg your pardon, could you repeat that?')
            self.conversation()
            # Self-reference inside a method should be avoided!
            # Handle recursion via an out-of-class while loop? 
    
    def farewell(self):
        '''Standard NPC 'goodbye' method.'''
        print('I bid you farewell, wanderer!\nMay your water flask never run dry.')
        # Different farewell() for NPC types?
        
class Shopkeeper(NPC):
    '''Shopkeeper class. Inherited from parent NPC class with added features.'''
    npc_occupation = 'shopkeeper'
    # Relevant to a conversation option - Occupation. 
    
    def conversation(self):
        '''Basic set of conversation options. Shopkeeper options added. Speech style
changes planned.'''
        pc_choice = input(
'''News
Gossip
Occupation
Buy
Sell
Leave
''')
        if pc_choice in ('News', 'news'):
            print('Nothing interesting recently.')
            # Stub. Will be expanded properly with game event triggers later.
        elif pc_choice in ('Gossip', 'gossip'):
            print('Did you know that the queen was found running around naked in the townsquare?!')
            # Random gossip responses generated from a gossip list. To be added later.
        elif pc_choice in ('Occupation', 'occupation'):
            if self.npc_occupation == None:
                print('My name is %s and I come from %s.\n' % (self.name, self.cell),
                      'Alas, I have no job and nothing to do...')
            else:
                print('My name is %s and I come from %s.\n' % (self.name, self.cell),
                       'I am a %s, just like my father.' % (self.npc_occupation))   
        elif pc_choice in ('Buy', 'buy'):
            print('What would you like to purchase?')
            # Separate 'Buy' class to be added later. With item selection, etc.
        elif pc_choice in ('Sell', 'sell'):
            print('What would you like to sell?')
            # Same as above.
        elif pc_choice in ('Leave', 'leave'):
            self.farewell()
        else:
            print('I beg your pardon, could you repeat that?')
            self.conversation()
            # Self-reference inside a method should be avoided!
            # Handle recursion via an out-of-class while loop? 
