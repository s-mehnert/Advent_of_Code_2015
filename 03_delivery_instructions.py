#***** ADVENT OF CODE 2015 *****
#************ DAY 3 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("03_delivery_instructions_input.txt") as input:
    input_data = input.readlines()[0]

print(input_data)

# create grid in which Santa moves

class Grid():
    def __init__(self, rows, cols):
        self.matrix = [[(i, j) for j in range(cols)] for i in range(rows)]
        self.santa_pos = self.matrix[rows//2][cols//2]
        self.visited = [self.santa_pos]
        self.matrix[self.santa_pos[0]][self.santa_pos[1]] = "  X "

# create method to mark houses as visited
    def mark_visited(self, position):
        if position not in self.visited:
            self.visited.append(position)
            self.matrix[position[0]][position[1]] = "  X "

# create method to visualize the grid
    def visualize(self):
        print()
        for row in self.matrix:
            print(row)

# create method to move Santa around
    def move_north(self):
        self.santa_pos = (self.santa_pos[0]-1, self.santa_pos[1])
    
    def move_south(self):
        self.santa_pos = (self.santa_pos[0]+1, self.santa_pos[1])
    
    def move_west(self):
        self.santa_pos = (self.santa_pos[0], self.santa_pos[1]-1)
    
    def move_east(self):
        self.santa_pos = (self.santa_pos[0], self.santa_pos[1]+1)

# count houses that received at least one present


# decipher instructions

def decipher_instructions(grid, instruction_string): # in progress, correct error
    for instr in instruction_string:
        if instr == "^":
            grid.move_north()
        elif instr == "v":
            grid.move_south()
        elif instr == "<":
            grid.move_west()
        elif instr == ">":
            grid.move_east()
        else:
            print("Invalid instruction.")
        grid.mark_visited(grid.santa_pos)


# Testing

house_grid = Grid(10, 10)
house_grid.visualize()

decipher_instructions(house_grid, input_data)
house_grid.visualize()
print(house_grid.visited)