def mapGenerator(dimension,**coord_dict):
    '''Generates and populates a map matrix in-place with coordinates of map markers.
dimension - the dimension of the generated unidimensional map matrix
**coord_dict - dictionary or sequence of map_marker = (x,y) assignments
               to populate the map matrix
'''
    map_matrix= [dimension * [0] for i in range(dimension)]
    for map_marker,coords in coord_dict.items():
        x,y = coords
        map_matrix[x][y] = map_marker
    return map_matrix

class Move():
    '''Handles player movement across a matrix-based map. Takes 2 arguments:
map_array - matrix defining map dimensions and containing special map markers
pc_loc - player location coordinates if they're known
         (optional tuple argument)
'''

    def __init__(self, map_array, pc_loc = None):
        self.map_array = map_array
        self.map_marker = None        # needs to be tracked internally to link
                                      # different movement directions
        self.x = 0                    # same reason as above
        self.y = 0

        if pc_loc is None:
            for row in map_array:
                if 'e' in row:
                    self.y = row.index('e')
                    self.x = map_array.index(row)
                    break             # prevents exhaustive searches
            self.pc_loc = (self.x,self.y)
            self.map_marker = self.map_array[self.x][self.y]
            self.map_array[self.x][self.y] = 1
            # player arrives at map 'exit' - saved map marker and noted player
            # position as 1 afterwards
        else:
            self.pc_loc = pc_loc
            self.x,self.y = self.pc_loc   # unpacking player location into
                                          # individual coordinates
            try:
                if self.map_array[self.x][self.y] not in (0, 1):
                    self.map_marker = self.map_array[self.x][self.y]
                    # saving map marker - literal value, other than 0 or 1,
                    # hence map marker position
            except IndexError:
                print('Illegal player location or out of map bounds')
                return
                # exits function call if given player location coordinates are
                # outside of the map
            self.map_array[self.x][self.y] = 1
            # noted player position as 1

    def __showmap__(self):
        for row in self.map_array:
            print(row)

    def __north__(self):
        self.map_array[self.x][self.y] = self.map_marker if self.map_marker else 0
            # reinstating map marker to current player position if exists,
            # if no map marker, default 0 is reinstated
        if 0 > self.x-1:
            print('Illegal player location or out of map bounds')
            self.map_array[self.x][self.y] = 1
            # restoring player position after out-of-bounds movement
            return
            # cancelling move via 'return' - no other option exists
        elif self.map_array[self.x-1][self.y] != 0:
            self.map_marker = self.map_array[self.x-1][self.y]
            # checking if next movement position is a map marker; save if yes
        else:
            self.map_marker = None
            # clearing map marker information, otherwise first movement
            # condition will fail for all subsequent movements
        self.x -= 1
        self.map_array[self.x][self.y] = 1

    def __west__(self):
        self.map_array[self.x][self.y] = self.map_marker if self.map_marker else 0
        if 0 > self.y-1:
            print('Illegal player location or out of map bounds')
            self.map_array[self.x][self.y] = 1
            return
        elif self.map_array[self.x][self.y-1] != 0:
            self.map_marker = self.map_array[self.x][self.y-1]
        else:
            self.map_marker = None
        self.y -= 1
        self.map_array[self.x][self.y] = 1

    def __south__(self):
        self.map_array[self.x][self.y] = self.map_marker if self.map_marker else 0
        try:
            if self.map_array[self.x+1][self.y] != 0:
                self.map_marker = self.map_array[self.x+1][self.y]
            else:
                self.map_marker = None
        except IndexError:
           print('Illegal player location or out of map bounds')
           self.map_array[self.x][self.y] = 1
           return
        self.x += 1
        self.map_array[self.x][self.y] = 1

    def __east__(self):
        self.map_array[self.x][self.y] = self.map_marker if self.map_marker else 0
        try:
            if self.map_array[self.x][self.y+1] != 0:
                self.map_marker = self.map_array[self.x][self.y+1]
            else:
                self.map_marker = None
        except IndexError:
            print('Illegal player location or out of map bounds')
            self.map_array[self.x][self.y] = 1
            return

        self.y += 1
        self.map_array[self.x][self.y] = 1

    def __toloc__(self):
        self.map_array[self.x][self.y] = self.map_marker if self.map_marker else 0
        self.x, self.y = input('State the coordinates, separated with a comma: ').split(',')
        try:
            if self.map_array[self.x][self.y] != 0:
                self.map_marker = self.map_array[self.x][self.y]
            else:
                self.map_marker = None
        except IndexError:
            print('Illegal player location or out of map bounds')
            self.map_array[self.x][self.y] = 1
            return
        self.map_array[self.x][self.y] = 1

    def __toplace__(self):
        self.map_array[self.x][self.y] = self.map_marker if self.map_marker else 0
        next_loc = input('Where would you like to go? ')
        for row in self.map_array:
            if next_loc in row:
                self.y = row.index(next_loc)
                self.x = self.map_array.index(row)
                break
        else:
            print('I am afraid this city does not have that facility.')
        try:
           if self.map_array[self.x][self.y] != 0:
               self.map_marker = self.map_array[self.x][self.y]
           else:
               self.map_marker = None
        except IndexError:
            print('Illegal player location or out of map bounds')
            self.map_array[self.x][self.y] = 1
            return
        self.map_array[self.x][self.y] = 1

if __name__ == '__main__':

    # Generating a 5x5 map using list comprehensions:
    molag_ker = [5 * [0] for i in range(5)]

    # Placing items on the map by directly addressing x,y coordinates:
    molag_ker[0][1] = 'b'            # b - blacksmith
    molag_ker[0][4] = 'g'            # g - general store
    molag_ker[4][4] = 'e'            # e - village/town/city exit
    # For procedurally generated maps, markers will be placed randomly within map
    # bounds (try...except: raise IndexError for handling?)

    # Drawing map for checking:
    for row in molag_ker:
        print(row)

    molag_ker_map = Move(molag_ker)

    for i in range(6):
        molag_ker_map.__showmap__()
        molag_ker_map.__east__()
        molag_ker_map.__south__()
        molag_ker_map.__north__()