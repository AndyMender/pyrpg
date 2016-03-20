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
            self.x,self.y = self.pc_loc   # when pc location is known,
                                          # x,y have known values
            if self.map_array[self.x][self.y] not in (0, 1):
                self.map_marker = self.map_array[self.x][self.y]
                # saving map marker - literal value other than 0 or 1,
                # hence map marker position
            self.map_array[self.x][self.y] = 1
            # noted player position as 1

    def __north__(self):
        if self.map_marker:
            self.map_array[self.x][self.y] = self.map_marker
            # reinstating map marker (if existed) to current player position
        else:
            self.map_array[self.x][self.y] = 0
            # if no map marker, default 0 is reinstated
        if self.map_array[self.x-1][self.y] != 0:
            self.map_marker = self.map_array[self.x-1][self.y]
            # checking if next movement position is a map marker; save if yes
        else:
            self.map_marker = None
            # clearing map marker information, otherwise first movement
            # condition will fail for all subsequent movements
        self.x -= 1
        self.map_array[self.x][self.y] = 1

    def __west__(self):
        if self.map_marker:
            self.map_array[self.x][self.y] = self.map_marker
        else:
            self.map_array[self.x][self.y] = 0

        if self.map_array[self.x][self.y-1] != 0:
            self.map_marker = self.map_array[self.x][self.y-1]
        else:
            self.map_marker = None

        self.y -= 1
        self.map_array[self.x][self.y] = 1

    def __south__(self):
        if self.map_marker:
            self.map_array[self.x][self.y] = self.map_marker
        else:
            self.map_array[self.x][self.y] = 0

        if self.map_array[self.x+1][self.y] != 0:
            self.map_marker = self.map_array[self.x+1][self.y]
        else:
            self.map_marker = None

        self.x += 1
        self.map_array[self.x][self.y] = 1

    def __east__(self):
        if self.map_marker:
            self.map_array[self.x][self.y] = self.map_marker
        else:
            self.map_array[self.x][self.y] = 0

        if self.map_array[self.x][self.y+1] != 0:
            self.map_marker = self.map_array[self.x][self.y+1]
        else:
            self.map_marker = None
        self.y += 1
        self.map_array[self.x][self.y] = 1

    def __toloc__(self):
        if self.map_marker:
            self.map_array[self.x][self.y] = self.map_marker
        else:
            self.map_array[self.x][self.y] = 0

        self.x, self.y = input('State the coordinates, separated with a comma: ').split(',')
        if self.map_array[self.x][self.y] != 0:
            self.map_marker = self.map_array[self.x][self.y]
        else:
            self.map_marker = None

        self.map_array[self.x][self.y] = 1

    def __toplace__(self):
        if self.map_marker:
            self.map_array[self.x][self.y] = self.map_marker
        else:
            self.map_array[self.x][self.y] = 0

        next_loc = input('Where would you like to go? ')
        for row in self.map_array:
            if next_loc in row:
                self.y = row.index(next_loc)
                self.x = self.map_array.index(row)
                break

        if self.map_array[self.x][self.y] != 0:
            self.map_marker = self.map_array[self.x][self.y]
        else:
            self.map_marker = None

        self.map_array[self.x][self.y] = 1