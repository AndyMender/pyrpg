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

# Creating city cell with markers:
molag_ker = {'cell name': 'Molag Ker',
'cell layout': mapGenerator(5, b=(3,4), t=(0,0), e=(2,4))}

# Creating world cell with 1 marker for subcell molag_ker:
world_cell = {'cell name': 'World',
'cell layout': mapGenerator(20, mk = (4,5))}

for row in world_cell['cell layout']:
    print(row)

# How to reference 'mk' to the molag_ker cell? External dictionary?
world_cell_refs = {'mk': molag_ker}
# For each cell generation event a *_refs dictionary? Other solutions?

# Getting cell layout for the molag_ker cell - simple:
print(world_cell_refs['mk']['cell layout'])
# The molag_ker variable can still be addressed
