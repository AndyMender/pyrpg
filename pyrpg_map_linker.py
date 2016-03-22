# Current world cell building process involves embedding matrix/array cells into
# each other. Topmost level is the world cell (1000x1000 or bigger), which
# contains reference points to subcells - towns.

# How to create and map references? The standard output needs to present only
# empty locations (value 0) and special map markers:
# > NPCs in shop cells
# > shops in town/city cells
# > towns/cities in world cell

# **KISS is important - only clarity comes over simplicity and performance**

from pyrpg_mapper import mapGenerator
from pyrpg_charclass import Shopkeeper

# Creating NPCs for Molag Ker - Blacksmith (level 0 - building cell):
astesius_kies = Shopkeeper('Astesius Kies', 'Molag Ker - Blacksmith')
marius_kusas = Shopkeeper('Marius Kusas', 'Molag Ker - Blacksmith')
# Two identifiers are generated - NPC name and cell name.
# Both can be used for later tracking of the NPCs for player-NPC interactions.

# Creating level 0 cell - building/room:
molag_ker_b = {'cell name': 'Molag Ker - Blacksmith',
'cell space': mapGenerator(6, npc_1=(3,4), npc_2=(2,3)),
'npc_1': astesius_kies,
'npc_2': marius_kusas}
# Each level 0 cell map marker has its x,y coordinates in the cell space matrix
# and refers directly to the NPC class instances through level 0 map marker key.

# Calling NPC by name and cell name:
print('Calling NPC by name and cell name from level 0 cell:')
print('NPC 1: ', molag_ker_b['npc_1'].name, molag_ker_b['npc_1'].cell)
print('NPC 2: ', molag_ker_b['npc_2'].name, molag_ker_b['npc_2'].cell)

# Calling NPC name by level 0 coordinates - the juicy part:
print('Calling NPC name by level 0 coordinates:')
print(molag_ker_b[molag_ker_b['cell space'][3][4]].name)

# Creating level 1 cell - city with markers:
molag_ker = {'cell name': 'Molag Ker',
'cell space': mapGenerator(5, b=(3,4), t=(0,0), e=(2,4)),
'b': molag_ker_b}
# Each level 1 cell map marker has its x,y coordinates in the cell space matrix
# and refers to a level 0 cell dictionary through a level 1 map marker key.

# Calling NPC by name and cell name from level 1 cell:
print('Callling NPC by name and cell name from level 1 cell:')
print('NPC 1: ', molag_ker['b']['npc_1'].name, molag_ker['b']['npc_1'].cell)
print('NPC 2: ', molag_ker['b']['npc_2'].name, molag_ker['b']['npc_2'].cell)

# Creating world cell with 1 marker for subcell molag_ker:
world_cell = {'cell name': 'World',
'cell space': mapGenerator(20, mk = (4,5)),
'mk': molag_ker}
# Each level 2 cell map marker has its x,y coordinates in the cell space matrix
# and refers to a level 1 cell dictionary through a level 2 map marker key.

# Calling NPC by name and cell name from level 2 cell:
print('Callling NPC by name and cell name from level 2 cell:')
print('NPC 1: ', world_cell['mk']['b']['npc_1'].name, world_cell['mk']['b']['npc_1'].cell)
print('NPC 2: ', world_cell['mk']['b']['npc_2'].name, world_cell['mk']['b']['npc_2'].cell)

# Issue #1 - how to automate addressing variable values between cell levels?
# Issue #2 - build a matrix class (addressing indices, finding values, etc.)