# Maps as matrices so that the player can move in all directions.
# Issue - event triggers when player encounters an object he/she can interact 
# with.

# For map related capabilities use classes? Movement, triggers, etc.

# Generating a 5x5 map using list comprehensions:
molag_ker = [5 * [0] for i in range(5)]

# Placing items on the map by directly addressing x,y coordinates:
molag_ker[0][1] = 'b'            # b - blacksmith
molag_ker[0][4] = 'g'            # g - general store
molag_ker[4][4] = 'e'            # e - village/town/city exit (gates)
for row in molag_ker:
    print(row)

# Initial player position:
molag_ker[0][0] = 1
for row in molag_ker:
    print(row)
    
# Trick - storing former position separately and putting back onto map on 
# movement. Checks for map markers needed and remembering position from BEFORE
# player movement needed also!

# Player location on map:
x, y = 0, 0

# Movement east:
f_x, f_y = x, y                  # storing current location coordinates    
y += 1                           # movement - changing y coordinate
molag_ker[x][y] = 1              # new player location
molag_ker[f_x][f_y] = 0          # refreshing former field

for row in molag_ker:
    print(row)

# Movement east again:
f_x, f_y = x, y                  # storing current location coordinates    
y += 1                           # movement - changing y coordinate
molag_ker[x][y] = 1              # new player location
molag_ker[f_x][f_y] = 0          # refreshing former field

for row in molag_ker:
    print(row)
# Issue - remembering map markers for recursive movement
# Temporary copy of whole map with map marker still present?