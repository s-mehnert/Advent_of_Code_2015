#***** ADVENT OF CODE 2015 *****
#************ DAY 3 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("03_delivery_instructions_input.txt") as input:
    input_data = input.readlines()[0]

# create grid in which Santa moves

class Grid():
    def __init__(self, rows, cols):
        self.matrix = [[(i, j) for j in range(cols)] for i in range(rows)]
        self.santa_pos = self.matrix[rows//2][cols//2]
        self.robo_pos = self.matrix[rows//2][cols//2]
        self.matrix[self.santa_pos[0]][self.santa_pos[1]] = "  X "
        self.visited = [self.santa_pos]

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
    def move_north(self, who):
        if who == "santa":
            self.santa_pos = (self.santa_pos[0]-1, self.santa_pos[1])
        else:
            self.robo_pos = (self.robo_pos[0]-1, self.robo_pos[1])
    
    def move_south(self, who):
        if who == "santa":
            self.santa_pos = (self.santa_pos[0]+1, self.santa_pos[1])
        else:
            self.robo_pos = (self.robo_pos[0]+1, self.robo_pos[1])
    
    def move_west(self, who):
        if who == "santa":
            self.santa_pos = (self.santa_pos[0], self.santa_pos[1]-1)
        else:
            self.robo_pos = (self.robo_pos[0], self.robo_pos[1]-1)
    
    def move_east(self, who):
        if who == "santa":
            self.santa_pos = (self.santa_pos[0], self.santa_pos[1]+1)
        else:
            self.robo_pos = (self.robo_pos[0], self.robo_pos[1]+1)

# count houses that received at least one present
    def count_visited(self):
        return len(self.visited)


# decipher instructions

def decipher_instructions(grid, instruction_string): 
    who = None
    for i in range(len(instruction_string)):
        if i % 2 == 0:
            who = "santa"
        else:
            who = "robo"
        if instruction_string[i] == "^":
            grid.move_north(who)
        elif instruction_string[i] == "v":
            grid.move_south(who)
        elif instruction_string[i] == "<":
            grid.move_west(who)
        elif instruction_string[i] == ">":
            grid.move_east(who)
        else:
            print("Invalid instruction.")
        if i % 2 == 0:
            grid.mark_visited(grid.santa_pos)
        else:
            grid.mark_visited(grid.robo_pos)


# Testing

house_grid = Grid(1000, 1000)
decipher_instructions(house_grid, input_data)
print(f"\n{house_grid.count_visited()} houses have received at least one present.")


#****************** Part 2 *****

# create class variable robo_santa_pos
# change move methods to account for 2 possible santas moving
# change decipher instructions method to account for 2 santas delivering presents